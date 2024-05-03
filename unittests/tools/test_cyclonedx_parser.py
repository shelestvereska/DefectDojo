import datetime

from dojo.models import Finding, Test
from dojo.tools.cyclonedx.parser import CycloneDXParser

from ..dojo_test_case import DojoTestCase


class TestCyclonedxParser(DojoTestCase):
    def test_grype_report(self):
        with open("unittests/scans/cyclonedx/grype_dd_1_14_1.xml") as file:
            parser = CycloneDXParser()
            findings = list(parser.get_findings(file, Test()))
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
            self.assertEqual(312, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                self.assertEqual("Low", finding.severity)
                self.assertEqual("Django", finding.component_name)
                self.assertEqual("2.2.18", finding.component_version)
                self.assertEqual(datetime.date(2021, 4, 13), datetime.datetime.date(finding.date))
            with self.subTest(i=200):
                finding = findings[200]
                self.assertEqual("Low", finding.severity)
                self.assertEqual("libopenjp2-7", finding.component_name)
                self.assertEqual("2.3.0-2+deb10u2", finding.component_version)
                vulnerability_ids = finding.unsaved_vulnerability_ids
                self.assertEqual(1, len(vulnerability_ids))
                self.assertEqual('CVE-2019-6988', vulnerability_ids[0])
                self.assertEqual(datetime.date(2021, 4, 13), datetime.datetime.date(finding.date))

    def test_spec1_report(self):
        """Test a report from the spec itself"""
        with open("unittests/scans/cyclonedx/spec1.xml") as file:
            parser = CycloneDXParser()
            findings = list(parser.get_findings(file, Test()))
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
            self.assertEqual(1, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                vulnerability_ids = finding.unsaved_vulnerability_ids
                self.assertEqual(1, len(vulnerability_ids))
                self.assertEqual('CVE-2018-7489', vulnerability_ids[0])
                self.assertEqual("Critical", finding.severity)
                self.assertIn(finding.cwe, [184, 502])  # there is 2 CWE in the report
                self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", finding.cvssv3)
                self.assertEqual("jackson-databind", finding.component_name)
                self.assertEqual("2.9.9", finding.component_version)
                self.assertEqual("CVE-2018-7489", finding.vuln_id_from_tool)
                self.assertEqual("Upgrade\n", finding.mitigation)
                self.assertEqual(finding.component_name + ":" + finding.component_version + " | " + vulnerability_ids[0],
                                 finding.title)

    def test_spec1_report_low_first(self):
        """Test a report from the spec itself"""
        with open("unittests/scans/cyclonedx/spec1_lowfirst.xml") as file:
            parser = CycloneDXParser()
            findings = list(parser.get_findings(file, Test()))
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
            self.assertEqual(1, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                vulnerability_ids = finding.unsaved_vulnerability_ids
                self.assertEqual(1, len(vulnerability_ids))
                self.assertEqual('CVE-2018-7489', vulnerability_ids[0])
                self.assertEqual("Critical", finding.severity)
                self.assertIn(finding.cwe, [184, 502])  # there is 2 CWE in the report
                self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", finding.cvssv3)
                self.assertEqual("jackson-databind", finding.component_name)
                self.assertEqual("2.9.9", finding.component_version)
                self.assertEqual("CVE-2018-7489", finding.vuln_id_from_tool)
                self.assertEqual("Upgrade\n", finding.mitigation)

    def test_cyclonedx_bom_report(self):
        with open("unittests/scans/cyclonedx/cyclonedx_bom.xml") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
            self.assertEqual(0, len(findings))

    def test_cyclonedx_jake_report(self):
        """Test a report generated by Jake"""
        with open("unittests/scans/cyclonedx/jake.xml") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
            self.assertEqual(0, len(findings))

    def test_cyclonedx_retirejs_report(self):
        """Test a report generated by RetireJS"""
        with open("unittests/scans/cyclonedx/retirejs.latest.xml") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
            self.assertEqual(0, len(findings))

    def test_cyclonedx_grype_11_report(self):
        """Test a report generated by Grype 0.11"""
        with open("unittests/scans/cyclonedx/dd_1_15_0.xml") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
            self.assertEqual(381, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                self.assertEqual("Low", finding.severity)
                self.assertEqual("apt", finding.component_name)
                self.assertEqual("1.8.2.1", finding.component_version)
                self.assertFalse(finding.is_mitigated)
                self.assertTrue(finding.active)
            with self.subTest(i=5):
                finding = findings[5]
                self.assertEqual("Info", finding.severity)
                self.assertEqual("bind9-host", finding.component_name)
                self.assertEqual("1:9.11.5.P4+dfsg-5.1+deb10u3", finding.component_version)
            with self.subTest(i=379):
                finding = findings[379]
                self.assertEqual("Low", finding.severity)
                self.assertEqual("tar", finding.component_name)
                self.assertEqual("1.30+dfsg-6", finding.component_version)
                vulnerability_ids = finding.unsaved_vulnerability_ids
                self.assertEqual(1, len(vulnerability_ids))
                self.assertEqual('CVE-2019-9923', vulnerability_ids[0])
                self.assertIn("urn:uuid:be0e9032-5b6b-4ce4-9be4-e5956a0309c1", finding.description)
                self.assertEqual("CVE-2019-9923", finding.vuln_id_from_tool)
            with self.subTest(i=380):
                finding = findings[380]
                self.assertEqual("Low", finding.severity)
                self.assertEqual("tar", finding.component_name)
                self.assertEqual("1.30+dfsg-6", finding.component_version)
                vulnerability_ids = finding.unsaved_vulnerability_ids
                self.assertEqual(1, len(vulnerability_ids))
                self.assertEqual('CVE-2021-20193', vulnerability_ids[0])
                self.assertIn("urn:uuid:17a8ccee-f13b-4d9d-abfc-f3964597df9a", finding.description)
                self.assertEqual("CVE-2021-20193", finding.vuln_id_from_tool)

    def test_cyclonedx_1_4_xml(self):
        """CycloneDX version 1.4 XML format"""
        with open("unittests/scans/cyclonedx/valid-vulnerability-1.4.xml") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
                finding.clean()
            self.assertEqual(1, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                self.assertEqual("jackson-databind:2.9.4 | SNYK-JAVA-COMFASTERXMLJACKSONCORE-32111", finding.title)
                self.assertEqual("Critical", finding.severity)
                self.assertEqual("jackson-databind", finding.component_name)
                self.assertEqual("2.9.4", finding.component_version)
                self.assertIn(finding.cwe, [184, 502])  # there is 2 CWE in the report
                self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", finding.cvssv3)
                self.assertIn(
                    "FasterXML jackson-databind before 2.7.9.3, 2.8.x before 2.8.11.1 and 2.9.x before 2.9.5 allows unauthenticated remote code execution",
                    finding.description,
                )
                self.assertIn(
                    "Upgrade com.fasterxml.jackson.core:jackson-databind to version 2.6.7.5, 2.8.11.1, 2.9.5 or higher.",
                    finding.mitigation,
                )
                self.assertIn(
                    "An optional explanation of why the application is not affected by the vulnerable component.",
                    finding.mitigation,
                )
                self.assertIn(
                    "GitHub Commit",
                    finding.references,
                )
                self.assertIn(
                    "https://github.com/FasterXML/jackson-databind/commit/6799f8f10cc78e9af6d443ed6982d00a13f2e7d2",
                    finding.references,
                )
                self.assertEqual("SNYK-JAVA-COMFASTERXMLJACKSONCORE-32111", finding.vuln_id_from_tool)
                vulnerability_ids = finding.unsaved_vulnerability_ids
                self.assertEqual(3, len(vulnerability_ids))
                self.assertEqual('SNYK-JAVA-COMFASTERXMLJACKSONCORE-32111', vulnerability_ids[0])
                self.assertEqual('CVE-2018-7489', vulnerability_ids[1])
                self.assertEqual('CVE-2018-7489', vulnerability_ids[2])
                self.assertTrue(finding.is_mitigated)
                self.assertFalse(finding.active)

    def test_cyclonedx_1_4_json(self):
        """CycloneDX version 1.4 JSON format"""
        with open("unittests/scans/cyclonedx/valid-vulnerability-1.4.json") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
                finding.clean()
            self.assertEqual(1, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                self.assertEqual("jackson-databind:2.9.4 | SNYK-JAVA-COMFASTERXMLJACKSONCORE-32111", finding.title)
                self.assertEqual("Critical", finding.severity)
                self.assertEqual("jackson-databind", finding.component_name)
                self.assertEqual("2.9.4", finding.component_version)
                self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", finding.cvssv3)
                self.assertIn(
                    "FasterXML jackson-databind before 2.7.9.3, 2.8.x before 2.8.11.1 and 2.9.x before 2.9.5 allows unauthenticated remote code execution",
                    finding.description,
                )
                self.assertIn(
                    "Upgrade com.fasterxml.jackson.core:jackson-databind to version 2.6.7.5, 2.8.11.1, 2.9.5 or higher.",
                    finding.mitigation,
                )
                self.assertIn(
                    "An optional explanation of why the application is not affected by the vulnerable component.",
                    finding.mitigation,
                )
                self.assertIn(
                    "GitHub Commit",
                    finding.references,
                )
                self.assertIn(
                    "https://github.com/FasterXML/jackson-databind/commit/6799f8f10cc78e9af6d443ed6982d00a13f2e7d2",
                    finding.references,
                )
                self.assertEqual("SNYK-JAVA-COMFASTERXMLJACKSONCORE-32111", finding.vuln_id_from_tool)
                vulnerability_ids = finding.unsaved_vulnerability_ids
                self.assertEqual(2, len(vulnerability_ids))
                self.assertEqual('SNYK-JAVA-COMFASTERXMLJACKSONCORE-32111', vulnerability_ids[0])
                self.assertEqual('CVE-2018-7489', vulnerability_ids[1])
                self.assertTrue(finding.is_mitigated)
                self.assertFalse(finding.active)

    def test_cyclonedx_1_4_jake_json(self):
        """CycloneDX version 1.4 JSON format produced by jake 1.4.1"""
        with open("unittests/scans/cyclonedx/jake2.json") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            self.assertEqual(7, len(findings))
            for finding in findings:
                finding.clean()
                if finding.vuln_id_from_tool == "c7129ff8-08bc-4afe-82ec-7d97b9491741":
                    with self.subTest(i="CVE-2021-33203"):
                        self.assertIn(finding.severity, Finding.SEVERITIES)
                        self.assertEqual("Django:2.0 | c7129ff8-08bc-4afe-82ec-7d97b9491741", finding.title)
                        self.assertEqual("High", finding.severity)
                        self.assertEqual("Django", finding.component_name)
                        self.assertEqual("2.0", finding.component_version)
                        vulnerability_ids = finding.unsaved_vulnerability_ids
                        self.assertEqual(2, len(vulnerability_ids))
                        self.assertEqual('CVE-2021-33203', vulnerability_ids[1])
                        self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N", finding.cvssv3)
                        self.assertIn(
                            "Django before 2.2.24, 3.x before 3.1.12, and 3.2.x before 3.2.4 has a potential directory traversal",
                            finding.description,
                        )
                        self.assertEqual(datetime.date(2022, 1, 28), datetime.datetime.date(finding.date))
                elif finding.vuln_id_from_tool == "c9b6a6a5-01a4-4d4c-b480-b9d6825dc4d0":
                    with self.subTest(i="CVE-2018-7536"):
                        self.assertEqual("Django:2.0 | c9b6a6a5-01a4-4d4c-b480-b9d6825dc4d0", finding.title)
                        self.assertEqual("Medium", finding.severity)
                        self.assertEqual("Django", finding.component_name)
                        self.assertEqual("2.0", finding.component_version)
                        vulnerability_ids = finding.unsaved_vulnerability_ids
                        self.assertEqual(2, len(vulnerability_ids))
                        self.assertEqual('CVE-2018-7536', vulnerability_ids[1])
                        self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L", finding.cvssv3)
                        self.assertIn(
                            "An issue was discovered in Django 2.0 before 2.0.3, 1.11 before 1.11.11, and 1.8 before 1.8.19.",
                            finding.description,
                        )
                        self.assertEqual(datetime.date(2022, 1, 28), datetime.datetime.date(finding.date))
                elif finding.vuln_id_from_tool == "90cfba6a-ddc9-4708-b131-5d875e8c558d":
                    with self.subTest(i="CVE-2018-6188"):
                        self.assertEqual("High", finding.severity)
                        self.assertEqual("Django", finding.component_name)
                        self.assertEqual("2.0", finding.component_version)
                        vulnerability_ids = finding.unsaved_vulnerability_ids
                        self.assertEqual(2, len(vulnerability_ids))
                        self.assertEqual('CVE-2018-6188', vulnerability_ids[1])
                        self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N", finding.cvssv3)
                        self.assertIn(
                            "django.contrib.auth.forms.AuthenticationForm in Django 2.0 before 2.0.2, and 1.11.8 and 1.11.9, allows remote attackers to obtain potentially sensitive information",
                            finding.description,
                        )
                        self.assertEqual(datetime.date(2022, 1, 28), datetime.datetime.date(finding.date))

    def test_cyclonedx_1_4_xml_cvssv31(self):
        """CycloneDX version 1.4 XML format"""
        with open("unittests/scans/cyclonedx/log4j.xml") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
                finding.clean()
            self.assertEqual(8, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                self.assertEqual("log4j-core:2.13.2 | CVE-2021-44228", finding.title)
                self.assertEqual("Critical", finding.severity)
                self.assertEqual("log4j-core", finding.component_name)
                self.assertEqual("2.13.2", finding.component_version)
                self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", finding.cvssv3)

    def test_cyclonedx_1_4_json_cvssv31(self):
        """CycloneDX version 1.4 JSON format"""
        with open("unittests/scans/cyclonedx/log4j.json") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
                finding.clean()
            self.assertEqual(8, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                self.assertEqual("log4j-core:2.13.2 | CVE-2021-44228", finding.title)
                self.assertEqual("Critical", finding.severity)
                self.assertEqual("log4j-core", finding.component_name)
                self.assertEqual("2.13.2", finding.component_version)
                self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", finding.cvssv3)

    def test_cyclonedx_1_4_json_nested_cvssv31(self):
        """CycloneDX version 1.4 JSON format"""
        with open("unittests/scans/cyclonedx/nested-component-log4j.json") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
                finding.clean()
            self.assertEqual(8, len(findings))
            with self.subTest(i=0):
                finding = findings[0]
                self.assertEqual("log4j-core:2.13.2 | CVE-2021-44228", finding.title)
                self.assertEqual("Critical", finding.severity)
                self.assertEqual("log4j-core", finding.component_name)
                self.assertEqual("2.13.2", finding.component_version)
                self.assertEqual("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", finding.cvssv3)

    def test_cyclonedx_issue_9277(self):
        """CycloneDX version 1.5 JSON format"""
        with open("unittests/scans/cyclonedx/issue_9277.json") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
                finding.clean()
            self.assertEqual(14, len(findings))
            with self.subTest(i=0):
                finding = findings[1]
                self.assertEqual("Description was not provided.", finding.description)

    def test_cyclonedx_issue_8022(self):
        """CycloneDX version 1.4 JSON format"""
        with open("unittests/scans/cyclonedx/issue_8022.json") as file:
            parser = CycloneDXParser()
            findings = parser.get_findings(file, Test())
            for finding in findings:
                self.assertIn(finding.severity, Finding.SEVERITIES)
                finding.clean()
            self.assertEqual(1, len(findings))
