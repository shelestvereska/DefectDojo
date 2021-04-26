from django.test import TestCase
from dojo.tools.nikto.parser import NiktoParser
from dojo.models import Test, Engagement, Product


class TestNiktoParser(TestCase):

    def test_parse_file_with_old_format(self):
        test = Test()
        engagement = Engagement()
        engagement.product = Product()
        test.engagement = engagement
        testfile = open("dojo/unittests/scans/nikto/nikto-report-old-format.xml")
        parser = NiktoParser()
        findings = parser.get_findings(testfile, test)
        self.assertEqual(1, len(findings))

    def test_parse_file_with_no_vuln_has_no_findings(self):
        testfile = open("dojo/unittests/scans/nikto/nikto-report-zero-vuln.xml")
        parser = NiktoParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(0, len(findings))

    def test_parse_file_with_one_vuln_has_one_finding(self):
        test = Test()
        engagement = Engagement()
        engagement.product = Product()
        test.engagement = engagement
        testfile = open("dojo/unittests/scans/nikto/nikto-report-one-vuln.xml")
        parser = NiktoParser()
        findings = parser.get_findings(testfile, test)
        self.assertEqual(1, len(findings))

    def test_parse_file_with_multiple_vuln_has_multiple_findings(self):
        test = Test()
        engagement = Engagement()
        engagement.product = Product()
        test.engagement = engagement
        testfile = open("dojo/unittests/scans/nikto/nikto-report-many-vuln.xml")
        parser = NiktoParser()
        findings = parser.get_findings(testfile, test)
        self.assertTrue(len(findings) == 10)

    def test_parse_file_json_with_multiple_vuln_has_multiple_findings(self):
        testfile = open("dojo/unittests/scans/nikto/juice-shop.json")
        parser = NiktoParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(11, len(findings))
        for finding in findings:
            if "OSVDB-3092" == finding.unique_id_from_tool:
                self.assertEqual("001811", finding.vuln_id_from_tool)
                self.assertEqual(1, finding.nb_occurences)
                self.assertEqual("Medium", finding.severity)
                self.assertEqual(1, len(finding.unsaved_endpoints))
                endpoint = finding.unsaved_endpoints[0]
                self.assertEqual(443, endpoint.port)
                self.assertEqual("juice-shop.herokuapp.com", endpoint.host)
                self.assertEqual("/public/", endpoint.path)
            if ("Retrieved via header: 1.1 vegur" == finding.title and
                    "Info" == finding.severity):
                self.assertEqual(1, len(finding.unsaved_endpoints))
            if ("Potentially Interesting Backup/Cert File Found. " == finding.title and
                    "Info" == finding.severity):
                self.assertEqual(140, len(finding.unsaved_endpoints))

    def test_parse_file_json_with_uri_errors(self):
        testfile = open("dojo/unittests/scans/nikto/nikto-output.xml")
        parser = NiktoParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(13, len(findings))
        for finding in findings:
            if "favicon.ico file identifies this server as: Apache Tomcat" == finding.title:
                self.assertEqual("500008", finding.vuln_id_from_tool)
                self.assertEqual(1, finding.nb_occurences)
                self.assertEqual("Medium", finding.severity)
                # this one as error in URL
                # self.assertEqual(1, len(finding.unsaved_endpoints))
                # endpoint = finding.unsaved_endpoints[0]
                # self.assertEqual(443, endpoint.port)
                # self.assertEqual("juice-shop.herokuapp.com", endpoint.host)
                # self.assertEqual("/public/", endpoint.path)
            elif "/examples/servlets/index.html: Apache Tomcat default JSP pages present." == finding.title:
                self.assertEqual("000366", finding.vuln_id_from_tool)
                self.assertEqual(1, finding.nb_occurences)
                self.assertEqual("Info", finding.severity)
                self.assertEqual(1, len(finding.unsaved_endpoints))
                endpoint = finding.unsaved_endpoints[0]
                self.assertEqual(8070, endpoint.port)
                self.assertEqual("127.0.0.1", endpoint.host)
                self.assertEqual("examples/servlets/index.html", endpoint.path)

    def test_parse_file_json_another(self):
        testfile = open("dojo/unittests/scans/nikto/tdh.json")
        parser = NiktoParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(8, len(findings))
        with self.subTest(i=0):
            finding = findings[0]
            self.assertEqual("Uncommon header 'x-cacheable' found, with contents: YES", finding.title)
            self.assertEqual("999100", finding.vuln_id_from_tool)
            self.assertEqual(1, finding.nb_occurences)
            self.assertEqual("Info", finding.severity)
            self.assertEqual(1, len(finding.unsaved_endpoints))
            endpoint = finding.unsaved_endpoints[0]
            self.assertEqual(443, endpoint.port)
            self.assertEqual("www.tdh.com", endpoint.host)
            self.assertEqual("/", endpoint.path)
        with self.subTest(i=1):
            finding = findings[1]
            self.assertEqual("Uncommon header 'x-cache' found, with contents: HIT", finding.title)
            self.assertEqual("999100", finding.vuln_id_from_tool)
            self.assertEqual(1, finding.nb_occurences)
            self.assertEqual("Info", finding.severity)
            self.assertEqual(1, len(finding.unsaved_endpoints))
            endpoint = finding.unsaved_endpoints[0]
            self.assertEqual(443, endpoint.port)
            self.assertEqual("www.tdh.com", endpoint.host)
            self.assertEqual("/", endpoint.path)

    def test_parse_file_xml_another(self):
        testfile = open("dojo/unittests/scans/nikto/tdh.xml")
        parser = NiktoParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(8, len(findings))
        with self.subTest(i=0):
            finding = findings[0]
            self.assertEqual("Uncommon header 'x-cacheable' found, with contents: YES", finding.title)
            self.assertEqual("999100", finding.vuln_id_from_tool)
            self.assertEqual(1, finding.nb_occurences)
            self.assertEqual("Info", finding.severity)
            self.assertEqual(1, len(finding.unsaved_endpoints))
            endpoint = finding.unsaved_endpoints[0]
            self.assertEqual(443, endpoint.port)
            self.assertEqual("www.tdh.com", endpoint.host)
            self.assertEqual("/", endpoint.path)
        with self.subTest(i=1):
            finding = findings[1]
            self.assertEqual("Uncommon header 'x-cache' found, with contents: HIT", finding.title)
            self.assertEqual("999100", finding.vuln_id_from_tool)
            self.assertEqual(1, finding.nb_occurences)
            self.assertEqual("Info", finding.severity)
            self.assertEqual(1, len(finding.unsaved_endpoints))
            endpoint = finding.unsaved_endpoints[0]
            self.assertEqual(443, endpoint.port)
            self.assertEqual("www.tdh.com", endpoint.host)
            self.assertEqual("/", endpoint.path)
