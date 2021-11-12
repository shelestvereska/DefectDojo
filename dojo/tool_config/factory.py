from dojo.tools.sonarqube_api.api_client import SonarQubeAPI
from dojo.tools.cobalt_api.api_client import CobaltAPI

SCAN_APIS = {'SonarQube': SonarQubeAPI,
             'Cobalt.io': CobaltAPI}


def create_API(tool_configuration):
    if tool_configuration.tool_type.name in SCAN_APIS:
        api_class = SCAN_APIS.get(tool_configuration.tool_type.name)
        return api_class(tool_configuration)
    else:
        return None
