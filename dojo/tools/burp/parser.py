import base64
import logging
import re
import html2text
from defusedxml import ElementTree as etree
from dojo.models import Endpoint, Finding

logger = logging.getLogger(__name__)


class BurpParser(object):
    """
    The objective of this class is to parse an xml file generated by the burp tool.

    TODO Handle errors.
    TODO Test burp output version. Handle what happens if the parser doesn't support it.
    """

    def get_scan_types(self):
        return ["Burp Scan"]

    def get_label_for_scan_types(self, scan_type):
        return "Burp Scan"

    def get_description_for_scan_types(self, scan_type):
        return (
            "When the Burp report is generated, the recommended option is Base64 encoding both the request and "
            "response fields. These fields will be processed and made available in the 'Finding View' page."
        )

    def get_findings(self, xml_output, test, parser_custom_setting=None):
        tree = etree.parse(xml_output, etree.XMLParser())
        return self.get_items(tree, test)

    def get_items(self, tree, test):
        items = {}
        for node in tree.findall("issue"):
            item = get_item(node, test)
            dupe_key = item.vuln_id_from_tool
            if dupe_key in items:
                items[dupe_key].unsaved_endpoints = (
                    items[dupe_key].unsaved_endpoints + item.unsaved_endpoints
                )
                items[dupe_key].unsaved_req_resp = (
                    items[dupe_key].unsaved_req_resp + item.unsaved_req_resp
                )

                # Description details of the finding are added
                items[dupe_key].description = (
                    item.description + items[dupe_key].description
                )

                # Parameters of the finding are added
                if item.param:
                    items[dupe_key].param = (
                        item.param + ", " + str(items[dupe_key].param)
                    )
            else:
                items[dupe_key] = item

        return list(items.values())


def get_attrib_from_subnode(xml_node, subnode_xpath_expr, attrib_name):
    """
    Finds a subnode in the item node and the retrieves a value from it

    @return An attribute value
    """
    global ETREE_VERSION
    node = None

    if ETREE_VERSION[0] <= 1 and ETREE_VERSION[1] < 3:
        match_obj = re.search(
            r"([^\@]+?)\[\@([^=]*?)=\'([^\']*?)\'", subnode_xpath_expr
        )
        if match_obj is not None:
            node_to_find = match_obj.group(1)
            xpath_attrib = match_obj.group(2)
            xpath_value = match_obj.group(3)
            for node_found in xml_node.findall(node_to_find):
                if node_found.attrib[xpath_attrib] == xpath_value:
                    node = node_found
                    break
        else:
            node = xml_node.find(subnode_xpath_expr)

    else:
        node = xml_node.find(subnode_xpath_expr)

    if node is not None:
        return node.get(attrib_name)

    return None


def do_clean(value):
    myreturn = ""
    if value is not None:
        if len(value) > 0:
            for x in value:
                if x.text is not None:
                    myreturn += x.text
    return myreturn


def get_clean_base64(value):
    if value is None:
        return ""
    try:
        return base64.b64decode(value).decode(
            "utf-8", "replace"
        )  # wouldn't this be cleaner than below?
    except UnicodeDecodeError:
        # decoding of UTF-8 fail when you have a binary payload in the HTTP response
        # so we just cut it to have only the header and add fake body
        return "\r\n\r\n".join(
            [
                base64.b64decode(value).split(b"\r\n\r\n")[0].decode(),
                "<Binary Redacted Data>",
            ]
        )


def do_clean_cwe(value):
    if value is None:
        return list()
    cwes = list()
    if len(value) > 0:
        for x in value:
            if x.text is not None:
                for detected in re.findall(r"CWE-(\d+)", x.text):
                    cwes.append(int(detected))
    return cwes


def get_item(item_node, test):
    serial_number = item_node.findall("serialNumber")[0].text
    vuln_id_from_tool = item_node.findall("type")[0].text
    url = item_node.get("url")
    path = item_node.findall("path")[0].text
    location = item_node.findall("location")[0].text
    rparameter = re.search(r"(?<=\[)(.*)(\])", location)
    parameter = None
    if rparameter:
        parameter = rparameter.group(1)

    unsaved_req_resp = list()
    for request_response in item_node.findall("./requestresponse"):
        request = get_clean_base64(request_response.findall("request")[0].text)
        if request_response.findall("response"):
            response = get_clean_base64(
                request_response.findall("response")[0].text
            )
        else:
            response = ""
            # This case happens when a request_response pair doesn't have
            # a response at all
        unsaved_req_resp.append({"req": request, "resp": response})

    collab_text = ""
    for event in item_node.findall("./collaboratorEvent"):
        collab_details = list()
        collab_details.append(event.findall("interactionType")[0].text)
        collab_details.append(event.findall("originIp")[0].text)
        collab_details.append(event.findall("time")[0].text)

        if collab_details[0] == "DNS":
            collab_details.append(event.findall("lookupType")[0].text)
            collab_details.append(event.findall("lookupHost")[0].text)
            collab_text += (
                "The Collaborator server received a "
                + collab_details[0]
                + " lookup of type "
                + collab_details[3]
                + " for the domain name "
                + collab_details[4]
                + " at "
                + collab_details[2]
                + " originating from "
                + collab_details[1]
                + ". "
            )

        for request_response in event.findall("./requestresponse"):
            request = get_clean_base64(
                request_response.findall("request")[0].text
            )
            response = get_clean_base64(
                request_response.findall("response")[0].text
            )
            unsaved_req_resp.append({"req": request, "resp": response})
        if collab_details[0] == "HTTP":
            collab_text += (
                "The Collaborator server received an "
                + collab_details[0]
                + " request at "
                + collab_details[2]
                + " originating from "
                + collab_details[1]
                + ". "
            )

    text_maker = html2text.HTML2Text()
    text_maker.body_width = 0

    background = do_clean(item_node.findall("issueBackground"))
    if background:
        background = text_maker.handle(background)

    detail = do_clean(item_node.findall("issueDetail"))
    if detail:
        detail = text_maker.handle(detail)
        if collab_text:
            detail = text_maker.handle(detail + "<p>" + collab_text + "</p>")

    remediation = do_clean(item_node.findall("remediationBackground"))
    if remediation:
        remediation = text_maker.handle(remediation)

    remediation_detail = do_clean(item_node.findall("remediationDetail"))
    if remediation_detail:
        remediation = (
            text_maker.handle(remediation_detail + "\n") + remediation
        )

    references = do_clean(item_node.findall("references"))
    if references:
        references = text_maker.handle(references)

    severity = item_node.findall("severity")[0].text
    if "information" == severity.lower():
        severity = "Info"

    scanner_confidence = item_node.findall("confidence")[0].text
    if scanner_confidence:
        if scanner_confidence == "Certain":
            scanner_confidence = 1
        elif scanner_confidence == "Firm":
            scanner_confidence = 4
        elif scanner_confidence == "Tentative":
            scanner_confidence = 7

    host_node = item_node.findall("host")[0]
    url_host = host_node.text
    path = item_node.findall("path")[0].text

    # Finding and Endpoint objects returned have not been saved to the database
    finding = Finding(
        title=item_node.findall("name")[0].text,
        url=url,
        test=test,
        severity=severity,
        param=parameter,
        scanner_confidence=scanner_confidence,
        description="URL: " + url_host + path + "\n\n" + detail + "\n",
        mitigation=remediation,
        references=references,
        false_p=False,
        duplicate=False,
        out_of_scope=False,
        mitigated=None,
        dynamic_finding=True,
        impact=background,
        unique_id_from_tool=serial_number,
        vuln_id_from_tool=vuln_id_from_tool,
    )
    finding.unsaved_req_resp = unsaved_req_resp
    # manage endpoint
    finding.unsaved_endpoints = [Endpoint.from_uri(url_host)]
    # manage cwes
    cwes = do_clean_cwe(item_node.findall("vulnerabilityClassifications"))
    if len(cwes) > 1:
        # FIXME support more than one CWE
        logger.debug(
            f"more than one CWE for a finding {cwes}. NOT supported by parser API"
        )
    if len(cwes) > 0:
        finding.cwe = cwes[0]
    return finding
