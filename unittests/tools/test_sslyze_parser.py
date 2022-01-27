from os import path

from ..dojo_test_case import DojoTestCase
from dojo.tools.sslyze.parser import SslyzeParser
from dojo.models import Test


class TestSslyzeJSONParser(DojoTestCase):
    def test_parse_json_file_with_one_target_has_zero_vuln_old(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/one_target_zero_vuln_old.json"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(0, len(findings))

    def test_parse_json_file_with_one_target_has_one_vuln_old(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/one_target_one_vuln_old.json"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())

        self.assertEqual(1, len(findings))
        finding = findings[0]
        self.assertEqual('Problems in certificate deployments (www.example.com:443)', finding.title)
        description = '''www.example.com:443 has problems in certificate deployments:
 - certificate has expired for trust store Android, version 9.0.0_r9
 - certificate has expired for trust store Apple, version iOS 13, iPadOS 13, macOS 10.15, watchOS 6, and tvOS 13
 - certificate has expired for trust store Java, version jdk-13.0.2
 - certificate has expired for trust store Mozilla, version 2019-11-28
 - certificate has expired for trust store Windows, version 2020-05-04'''
        self.assertEqual(description, finding.description)
        self.assertEqual('Medium', finding.severity)

        self.assertEqual(1, len(finding.unsaved_endpoints))
        endpoint = finding.unsaved_endpoints[0]
        self.assertEqual('www.example.com', endpoint.host)
        self.assertEqual(443, endpoint.port)

    def test_parse_json_file_with_one_target_has_four_vuln_old(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/one_target_many_vuln_old.json"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())

        self.assertEqual(4, len(findings))

    def test_parse_json_file_with_two_target_has_many_vuln_old(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/two_targets_two_vuln_old.json"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())

        self.assertEqual(2, len(findings))

    def test_parse_json_file_with_one_target_has_zero_vuln_new(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/one_target_zero_vuln_new.json"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(0, len(findings))

    def test_parse_json_file_with_one_target_has_one_vuln_new(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/one_target_one_vuln_new.json"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())

        self.assertEqual(1, len(findings))
        finding = findings[0]
        self.assertEqual('Unrecommended cipher suites for TLS 1.2 (example.com:443)', finding.title)
        description = '''example.com:443 accepts unrecommended cipher suites for TLS 1.2:
 - TLS_RSA_WITH_AES_256_GCM_SHA384
 - TLS_RSA_WITH_AES_256_CCM_8
 - TLS_RSA_WITH_AES_256_CCM
 - TLS_RSA_WITH_AES_256_CBC_SHA256
 - TLS_RSA_WITH_AES_256_CBC_SHA
 - TLS_RSA_WITH_AES_128_GCM_SHA256
 - TLS_RSA_WITH_AES_128_CCM_8
 - TLS_RSA_WITH_AES_128_CCM
 - TLS_RSA_WITH_AES_128_CBC_SHA256
 - TLS_RSA_WITH_AES_128_CBC_SHA
 - TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
 - TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
 - TLS_DHE_RSA_WITH_AES_256_CCM_8
 - TLS_DHE_RSA_WITH_AES_256_CBC_SHA
 - TLS_DHE_RSA_WITH_AES_128_CCM_8
 - TLS_DHE_RSA_WITH_AES_128_CBC_SHA'''
        self.assertEqual(description, finding.description)
        self.assertEqual('Medium', finding.severity)

        self.assertEqual(1, len(finding.unsaved_endpoints))
        endpoint = finding.unsaved_endpoints[0]
        self.assertEqual('example.com', endpoint.host)
        self.assertEqual(443, endpoint.port)

    def test_parse_json_file_with_one_target_has_four_vuln_new(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/one_target_many_vuln_new.json"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(4, len(findings))

    def test_parse_json_file_with_two_target_has_many_vuln_new(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/two_targets_two_vuln_new.json"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())
        self.assertEqual(5, len(findings))


class TestSSLyzeXMLParser(DojoTestCase):
    def test_parse_file_with_one_target_has_three_vuln(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/report_one_target_three_vuln.xml"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())
        for finding in findings:
            for endpoint in finding.unsaved_endpoints:
                endpoint.clean()
        self.assertEqual(3, len(findings))

    def test_parse_xml_file_with_one_target_has_one_vuln(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/report_one_target_one_vuln.xml"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())
        for finding in findings:
            for endpoint in finding.unsaved_endpoints:
                endpoint.clean()
        self.assertEqual(1, len(findings))

    def test_parse_xml_file_with_one_target_has_three_vuln(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/report_one_target_three_vuln.xml"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())
        for finding in findings:
            for endpoint in finding.unsaved_endpoints:
                endpoint.clean()
        self.assertEqual(3, len(findings))

    def test_parse_xml_file_with_two_target_has_many_vuln(self):
        testfile = open(path.join(path.dirname(__file__), "../scans/sslyze/report_two_target_many_vuln.xml"))
        parser = SslyzeParser()
        findings = parser.get_findings(testfile, Test())
        for finding in findings:
            for endpoint in finding.unsaved_endpoints:
                endpoint.clean()
        self.assertEqual(7, len(findings))
