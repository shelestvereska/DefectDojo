from ..dojo_test_case import DojoTestCase
from dojo.models import Test
from dojo.tools.crunch42.parser import Crunch42Parser


class TestCrunch42Parser(DojoTestCase):

    def test_crunch42parser_single_has_many_findings(self):
        testfile = open("unittests/scans/crunch42/crunch42_many_findings.json")
        parser = Crunch42Parser()
        findings = parser.get_findings(testfile, Test())
        testfile.close()
        self.assertEqual(8, len(findings))

    def test_crunch42parser_single_has_many_findings2(self):
        testfile = open("unittests/scans/crunch42/crunch42_many_findings2.json")
        parser = Crunch42Parser()
        findings = parser.get_findings(testfile, Test())
        testfile.close()
        self.assertEqual(5, len(findings))
