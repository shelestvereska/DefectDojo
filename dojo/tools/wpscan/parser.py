
import hashlib
import json
from datetime import datetime
import hyperlink

from dojo.models import Endpoint, Finding


class WpscanParser(object):
    """WPScan – WordPress Security Scanner"""

    def get_scan_types(self):
        return ["Wpscan"]

    def get_label_for_scan_types(self, scan_type):
        return "Wpscan"

    def get_description_for_scan_types(self, scan_type):
        return "Import JSON report"

    def get_findings(self, file, test):
        tree = json.load(file)

        report_date = None
        if 'start_time' in tree:
            report_date = datetime.utcfromtimestamp(tree.get('start_time'))

        dupes = dict()
        for plugin in tree.get('plugins', []):
            node = tree['plugins'][plugin]
            for vul in node.get('vulnerabilities'):

                description = "\n".join([
                    '**Title:** `' + vul['title'] + "`\n",
                    '**Location:** `' + node['location'] + "`\n",
                    '**Plugin:** `' + plugin + "`\n",
                ])

                finding = Finding(
                    title=vul['title'],
                    description=description,
                    severity='Medium',
                    cwe=1035,
                    references=self.generate_references(vul['references']),
                    dynamic_finding=True,
                    static_finding=False,
                    unique_id_from_tool=vul['references']['wpvulndb'][0],
                    nb_occurences=1,
                )
                # manage version
                finding.component_name = plugin
                if 'version' in node and node['version'] is not None:
                    finding.component_version = node['version'].get('number')
                # manage date of finding with report date
                if report_date:
                    finding.date = report_date
                # if there is a fixed version fill mitigation
                if 'fixed_in' in vul:
                    finding.mitigation = 'fixed in : ' + vul['fixed_in']
                # manage CVE
                if 'cve' in vul['references']:
                    finding.cve = "CVE-" + vul['references']['cve'][0]

                # internal de-duplication
                dupe_key = hashlib.sha256(str(finding.unique_id_from_tool).encode('utf-8')).hexdigest()
                if dupe_key in dupes:
                    find = dupes[dupe_key]
                    if finding.references:
                        dupes[dupe_key].references += finding.references
                    find.nb_occurences += finding.nb_occurences
                else:
                    dupes[dupe_key] = finding

        # manage interesting interesting_findings
        for interesting_finding in tree.get('interesting_findings', []):
            references = self.generate_references(interesting_finding['references'])
            description = "\n".join([
                '**Type:** `' + interesting_finding.get('type') + "`\n",
                '**Url:** `' + interesting_finding['url'] + "`\n",
            ])
            finding = Finding(
                title=f"Interesting finding: {interesting_finding.get('to_s')}",
                description=description,
                severity='Info',
                dynamic_finding=True,
                static_finding=False,
            )
            # manage endpoint
            url = hyperlink.parse(interesting_finding['url'])
            endpoint = Endpoint(
                path="/".join(url.path),
                host=url.host,
                port=url.port,
                protocol=url.scheme,
            )
            finding.unsaved_endpoints = [endpoint]
            # manage date of finding with report date
            if report_date:
                finding.date = report_date

            # internal de-duplication
            dupe_key = hashlib.sha256(str("interesting_findings" + finding.title + interesting_finding['url']).encode('utf-8')).hexdigest()
            if dupe_key in dupes:
                find = dupes[dupe_key]
                if finding.references:
                    dupes[dupe_key].references += finding.references
                find.nb_occurences += finding.nb_occurences
            else:
                dupes[dupe_key] = finding

        return list(dupes.values())

    def generate_references(self, node):
        references = ""
        for ref in node:
            for item in node.get(ref, []):
                if ref == 'url':
                    references += f"* [{item}]({item})\n"
                elif ref == 'wpvulndb':
                    references += f"* [WPScan WPVDB](https://wpscan.com/vulnerability/{item})\n"
                else:
                    references += f"* {item} - {ref}\n"
        return references
