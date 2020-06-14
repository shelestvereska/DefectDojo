__author__ = 'aaronweaver'

from datetime import datetime
import json
from dojo.models import Finding


class ESLintParser(object):
    def _convert_eslint_severity_to_dojo_severity(self, eslint_severity):
        if eslint_severity == 2:
            return "High"
        elif eslint_severity == 1:
            return "Medium"
        else:
            return None

    def __init__(self, filename, test):
        self.items = []
        tree = filename.read()
        try:
            data = json.loads(str(tree, 'utf-8'))
        except:
            data = json.loads(tree)

        for item in data:
            categories = ''
            language = ''
            mitigation = ''
            impact = ''
            references = ''
            findingdetail = ''
            title = ''
            group = ''
            status = ''

            if (len(item["messages"]) == 0):
                continue

            for message in item["messages"]:
                title = message["message"] + " Test ID: " + message["ruleId"]

                #  ##### Finding details information ######
                findingdetail += "Filename: " + item["filePath"] + "\n"
                findingdetail += "Line number: " + str(message["line"]) + "\n"

                sev = self._convert_eslint_severity_to_dojo_severity(message["severity"])

                find = Finding(title=title,
                            test=test,
                            active=False,
                            verified=False,
                            description=findingdetail,
                            severity=sev.title(),
                            numerical_severity=Finding.get_numerical_severity(sev),
                            file_path=item["filePath"],
                            line=message["line"],
                            url='N/A',
                            static_finding=True)

                self.items.append(find)
