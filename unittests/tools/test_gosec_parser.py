from dojo.models import Test
from dojo.tools.gosec.parser import GosecParser
from unittests.dojo_test_case import DojoTestCase


class TestGosecParser(DojoTestCase):

    def test_parse_file_with_one_finding(self):
        with open("unittests/scans/gosec/many_vulns.json") as testfile:
            parser = GosecParser()
            findings = parser.get_findings(testfile, Test())
            self.assertEqual(28, len(findings))
            finding = findings[0]
            self.assertEqual("Low", finding.severity)
            self.assertEqual("/vagrant/go/src/govwa/app.go", finding.file_path)
            self.assertEqual(79, finding.line)
