from django.urls import reverse
from django.test import TestCase
from dojo.models import System_Settings, JIRA_Issue
import json
# from unittest import skip
import logging

logger = logging.getLogger(__name__)


class JIRAWebhookTest(TestCase):
    fixtures = ['dojo_testdata.json']

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.correct_secret = '12345'
        self.incorrect_secret = '1234567890'

    # def setUp(self):
        # self.url = reverse(self.viewname + '-list')

    def system_settings(self, enable_jira=False, enable_jira_web_hook=False, disable_jira_webhook_secret=False, jira_webhook_secret=None):
        ss = System_Settings.objects.get()
        ss.enable_jira = enable_jira
        ss.enable_jira_web_hook = enable_jira_web_hook
        ss.disable_jira_webhook_secret = disable_jira_webhook_secret
        ss.jira_webhook_secret = jira_webhook_secret
        ss.save()

    def test_webhook_get(self):
        response = self.client.get(reverse('jira_web_hook'))
        self.assertEqual(405, response.status_code)

    def test_webhook_jira_disabled(self):
        self.system_settings(enable_jira=False)
        response = self.client.post(reverse('jira_web_hook'))
        self.assertEqual(404, response.status_code)

    def test_webhook_disabled(self):
        self.system_settings(enable_jira=False, enable_jira_web_hook=False)
        response = self.client.post(reverse('jira_web_hook'))
        self.assertEqual(404, response.status_code)

    def test_webhook_invalid_content_type(self):
        self.system_settings(enable_jira=True, enable_jira_web_hook=True, disable_jira_webhook_secret=True)
        response = self.client.post(reverse('jira_web_hook'))
        # 400 due to incorrect content_type
        self.assertEqual(400, response.status_code)

    def test_webhook_secret_disabled_no_secret(self):
        self.system_settings(enable_jira=True, enable_jira_web_hook=True, disable_jira_webhook_secret=True)
        response = self.client.post(reverse('jira_web_hook'))
        # 400 due to incorrect content_type
        self.assertEqual(400, response.status_code)

    def test_webhook_secret_disabled_secret(self):
        self.system_settings(enable_jira=True, enable_jira_web_hook=True, disable_jira_webhook_secret=True)
        response = self.client.post(reverse('jira_web_hook_secret', args=(self.incorrect_secret, )))
        # 400 due to incorrect content_type
        self.assertEqual(400, response.status_code)

    def test_webhook_secret_enabled_no_secret(self):
        self.system_settings(enable_jira=True, enable_jira_web_hook=True, disable_jira_webhook_secret=False, jira_webhook_secret=self.correct_secret)
        response = self.client.post(reverse('jira_web_hook'))
        self.assertEqual(403, response.status_code)

    def test_webhook_secret_enabled_incorrect_secret(self):
        self.system_settings(enable_jira=True, enable_jira_web_hook=True, disable_jira_webhook_secret=False, jira_webhook_secret=self.correct_secret)
        response = self.client.post(reverse('jira_web_hook_secret', args=(self.incorrect_secret, )))
        self.assertEqual(403, response.status_code)

    def test_webhook_secret_enabled_correct_secret(self):
        self.system_settings(enable_jira=True, enable_jira_web_hook=True, disable_jira_webhook_secret=False, jira_webhook_secret=self.correct_secret)
        response = self.client.post(reverse('jira_web_hook_secret', args=(self.correct_secret, )))
        # 400 due to incorrect content_type
        self.assertEqual(400, response.status_code)

    def test_webhook_comment_on_finding(self):
        self.system_settings(enable_jira=True, enable_jira_web_hook=True, disable_jira_webhook_secret=False, jira_webhook_secret=self.correct_secret)

        body = {
            "timestamp": 1605117321425,
            "webhookEvent": "comment_created",
            "comment": {
                        "self": "https://jira.isaac.nl/rest/api/2/issue/2/comment/456843",
                        "id": "456843",
                        "author": {
                            "self": "https://jira.isaac.nl/rest/api/2/user?username=valentijn",
                            "name": "valentijn",
                            "key": "valentijn",
                            "avatarUrls": {
                                "48x48": "https://jira.isaac.nl/secure/useravatar?ownerId=valentijn&avatarId=11101",
                                "24x24": "https://jira.isaac.nl/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
                                "16x16": "https://jira.isaac.nl/secure/useravatar?size=x small&ownerId=valentijn&avatarId=11101",
                                "32x32": "https://jira.isaac.nl/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
                            },
                            "displayName": "Valentijn Scholten",
                            "active": "true",
                            "timeZone": "Europe/Amsterdam"
                        },
                        "body": "test2",
                        "updateAuthor": {
                            "self": "https://jira.isaac.nl/rest/api/2/user?username=valentijn",
                            "name": "valentijn",
                            "key": "valentijn",
                            "avatarUrls": {
                                "48x48": "https://jira.isaac.nl/secure/useravatar?ownerId=valentijn&avatarId=11101",
                                "24x24": "https://jira.isaac.nl/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
                                "16x16": "https://jira.isaac.nl/secure/useravatar?size=xsmall&ownerId=valentijn&avatarId=11101",
                                "32x32": "https://jira.isaac.nl/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
                            },
                            "displayName": "Valentijn Scholten",
                            "active": "true",
                            "timeZone": "Europe/Amsterdam"
                        },
                        "created": "2020-11-11T18:55:21.425+0100",
                        "updated": "2020-11-11T18:55:21.425+0100"
            }
        }

        # finding 5 has a JIRA issue in the initial fixture for unit tests

        jira_issue = JIRA_Issue.objects.get(jira_id=2)
        finding = jira_issue.finding
        notes_count_before = finding.notes.count()

        response = self.client.post(reverse('jira_web_hook_secret', args=(self.correct_secret, )),
                                    body,
                                    content_type="application/json")

        jira_issue = JIRA_Issue.objects.get(jira_id=2)
        finding = jira_issue.finding
        notes_count_after = finding.notes.count()

        self.assertEqual(200, response.status_code)
        self.assertEqual(notes_count_after, notes_count_before + 1)

    def test_webhook_update_finding(self):
        self.system_settings(enable_jira=True, enable_jira_web_hook=True, disable_jira_webhook_secret=False, jira_webhook_secret=self.correct_secret)

        body = json.dumps(json.loads("""
{
   "timestamp":1605117321475,
   "webhookEvent":"jira:issue_updated",
   "issue_event_type_name":"issue_commented",
   "user":{
      "self":"https://jira.onpremise.org/rest/api/2/user?username=valentijn",
      "name":"valentijn",
      "key":"valentijn",
      "emailAddress ":"valentijn.scholten@isaac.nl",
      "avatarUrls":{
         "48x48":"https://jira.onpremise.org/secure/useravatar?ownerId=valentijn&avatarId=11101",
         "24x24":"http s://jira.onpremise.org/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
         "16x16":"https://jira.onpremise.org/secure/useravatar?size=xsmall& ownerId=valentijn&avatarId=11101",
         "32x32":"https://jira.onpremise.org/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
      },
      "displayName ":"Valentijn Scholten",
      "active":"true",
      "timeZone":"Europe/Amsterdam"
   },
   "issue":{
      "id":"2",
      "self":"https://jira.onpremise.org/rest/api/2/issue/2 ",
      "key":"ISEC-277",
      "fields":{
         "issuetype":{
            "self":"https://jira.onpremise.org/rest/api/2/issuetype/3",
            "id":"3",
            "description":"A task is some piece o f work that can be assigned to a user. This does not always result in a quotation/estimate, as it is often some task that needs to be performe d in the context of an existing contract. ",
            "iconUrl":"https://jira.onpremise.org/secure/viewavatar?size=xsmall&avatarId=16681&avatarType=issuetype",
            "name":"Task",
            "subtask":false,
            "avatarId":16681
         },
         "project":{
            "self":"https://jira.onpremise.org/rest/api/2/project/13532",
            "id":"13532",
            "key":"ISEC",
            "name":"ISAAC security",
            "projectTypeKey":"software",
            "avatarUrls":{
               "48x48":"https://jira.onpremise.org/secure/projectavatar?avatarId=14803",
               "24x24":"https://jira.onpremise.org/secure/projectavatar?size=small&avatarId=14803",
               "16x16":"https://jira.onpremise.org/secure/projectavatar?size=xsmall&avatarId=14803",
               "32x32":"https://jira.onpremise.org/secure/projectavatar?size=medium&avatarId=14803"
            },
            "projectCategory":{
               "self":"https://jira.onpremise.org/rest/api/2/projectCategory/10032",
               "id":"10032",
               "description":"All internal isaac projects.",
               "name":"isaac internal"
            }
         },
         "fixVersions":[
         ],
         "customfield_11440":"0|y02wb8: ",
                        "resolution":{
                            "self":"https://jira.isaac.nl/rest/api/2/resolution/11",
                            "id":"11",
                            "description":"Cancelled by the customer.",
                            "name":"Cancelled"
                        },
         "resolutiondate":null,
         "workratio":"-1",
         "lastViewed":"2020-11-11T18:54:32.489+0100",
         "watches":{
            "self":"https://jira.onpremise.org/rest/api/2/issue/ISEC-277/watchers",
            "watchCount":1,
            "isWatching":"true"
         },
         "customfield_10060":[
            "defect.dojo(defect.dojo)",
            "valentijn(valentijn)"
         ],
         "customfield_10182":null,
         "created":"2019-04-04T15:38:21.248+0200",
         "customfield_12043":null,
         "customfield_10340":null,
         "customfield_10341":null,
         "customfield_12045":null,
         "customfield_10100":null,
         "priority":{
            "self":"https://jira.onpremise.org/rest/api/2/priority/5",
            "iconUrl":"https://jira.onpremise.org/images/icons/priorities/trivial.svg",
            "name":"Trivial (Sev5)",
            "id":"5"
         },
         "customfield_10740":null,
         "labels":[
            "NPM_Test",
            "defect-dojo",
            "security"
         ],
         "timeestimate":null,
         "aggregatetimeoriginalestimate":null,
         "issuelinks":[
         ],
         "assignee":{
            "self":"https://jira.onpremise.org/rest/api/2/user?username=valentijn",
            "name":"valentijn",
            "key":"valentijn",
            "emailAddress":"valentijn.scholten@isaac.nl",
            "avatarUrls":{
               "48x48":"https://jira.onpremise.org/secure/useravatar?ownerId=valentijn&avatarId=11101",
               "24x24":"https://jira.onpremise.org/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
               "16x16":"https://jira.onpremise.org/secure/useravatar?size=xsmall&ownerId=valentijn&avatarId=11101",
               "32x32":"https://jira.onpremise.org/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
            },
            "displayName":"Valentijn Scholten",
            "active":"true",
            "timeZone":"Europe/Amsterdam"
         },
         "updated":"2020-11-11T18:54:32.155+0100",
         "status":{
            "self":"https://jira.onpremise.org/rest/api/2/status/10022",
            "description":"Incoming/New issues.",
            "iconUrl":"https://jira.onpremise.org/isaac_content/icons/isaac_status_new.gif",
            "name":"Closed",
            "id":"10022",
            "statusCategory":{
               "self":"https://jira.onpremise.org/rest/api/2/statuscategory/2",
               "id":2,
               "key":"new",
               "colorName":"blue-gray",
               "name":"To Do"
            }
         },
         "components":[
         ],
         "customfield_10051":"2020-11-11T18:54:32.155+0100",
         "timeoriginalestimate":null,
         "customfield_10052":null,
         "description":"description",
         "customfield_10010":null,
         "timetracking":{
         },
         "attachment":[
         ],
         "aggregatetimeestimate":null,
         "summary":"Regular Expression Denial of Service - (braces, <2.3.1)",
         "creator":{
            "self":"https://jira.onpremise.org/rest/api/2/user?username=defect.dojo",
            "name":"defect.dojo",
            "key":"defect.dojo",
            "emailAddress":"defectdojo@isaac.nl",
            "avatarUrls":{
               "48x48":"https://www.gravatar.com/avatar/9637bfb970eff6176357df615f548f1c?d=mm&s=48",
               "24x24":"https://www.gravatar.com/avatar/9637bfb970eff6176357df615f548f1c?d=mm&s=24",
               "16x16":"https://www.gravatar.com/avatar/9637bfb970eff6176357df615f548f1c?d=mm&s=16",
               "32x32":"https://www.gravatar.com/avatar/9637bfb970eff6176357df615f548f1c?d=mm&s=32"
            },
            "displayName":"Defect Dojo",
            "active":"true",
            "timeZone":"Europe/Amsterdam"
         },
         "subtasks":[
         ],
         "customfield_10240":"9223372036854775807",
         "reporter":{
            "self":"https://jira.onpremise.org/rest/api/2/user?username=defect.dojo",
            "name":"defect.dojo",
            "key":"defect.dojo",
            "emailAddress":"defectdojo@isaac.nl",
            "avatarUrls":{
               "48x48":"https://www.gravatar.com/avatar/9637bfb970eff6176357df615f548f1c?d=mm&s=48",
               "24x24":"https://www.gravatar.com/avatar/9637bfb970eff6176357df615f548f1c?d=mm&s=24",
               "16x16":"https://www.gravatar.com/avatar/9637bfb970eff6176357df615f548f1c?d=mm&s=16",
               "32x32":"https://www.gravatar.com/avatar/9637bfb970eff6176357df615f548f1c?d=mm&s=32"
            },
            "displayName":"Defect Dojo",
            "active":"true",
            "timeZone":"Europe/Amsterdam"
         },
         "aggregateprogress":{
            "progress":0,
            "total":0
         },
         "customfield_10640":"9223372036854775807",
         "customfield_10641":null,
         "environment":null,
         "duedate":null,
         "progress":{
            "progress":0,
            "total":0
         },
         "comment":{
            "comments":[
               {
                  "self":"https://jira.onpremise.org/rest/api/2/issue/2/comment/456841",
                  "id":"456841",
                  "author":{
                     "self":"https://jira.onpremise.org/rest/api/2/user?username=valentijn",
                     "name":"valentijn",
                     "key":"valentijn",
                     "emailAddress":"valentijn.scholten@isaac.nl",
                     "avatarUrls":{
                        "48x48":"https://jira.onpremise.org/secure/useravatar?ownerId=valentijn&avatarId=11101",
                        "24x24":"https://jira.onpremise.org/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
                        "16x16":"https://jira.onpremise.org/secure/useravatar?size=xsmall&ownerId=valentijn&avatarId=11101",
                        "32x32":"https://jira.onpremise.org/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
                     },
                     "displayName":"Valentijn Scholten",
                     "active":"true",
                     "timeZone":"Europe/Amsterdam"
                  },
                  "body":"test comment valentijn",
                  "updateAuthor":{
                     "self":"https://jira.onpremise.org/rest/api/2/user?username=valentijn",
                     "name":"valentijn",
                     "key":"valentijn",
                     "emailAddress":"valentijn.scholten@isaac.nl",
                     "avatarUrls":{
                        "48x48":"https://jira.onpremise.org/secure/useravatar?ownerId=valentijn&avatarId=11101",
                        "24x24":"https://jira.onpremise.org/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
                        "16x16":"https://jira.onpremise.org/secure/useravatar?size=xsmall&ownerId=valentijn&avatarId=11101",
                        "32x32":"https://jira.onpremise.org/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
                     },
                     "displayName":"Valentijn Scholten",
                     "active":"true",
                     "timeZone":"Europe/Amsterdam"
                  },
                  "created":"2020-11-11T18:54:32.155+0100",
                  "updated":"2020-11-11T18:54:32.155+0100"
               },
               {
                  "self":"https://jira.onpremise.org/rest/api/2/issue/2/comment/456843",
                  "id":"456843",
                  "author":{
                     "self":"https://jira.onpremise.org/rest/api/2/user?username=valentijn",
                     "name":"valentijn",
                     "key":"valentijn",
                     "emailAddress":"valentijn.scholten@isaac.nl",
                     "avatarUrls":{
                        "48x48":"https://jira.onpremise.org/secure/useravatar?ownerId=valentijn&avatarId=11101",
                        "24x24":"https://jira.onpremise.org/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
                        "16x16":"https://jira.onpremise.org/secure/useravatar?size=xsmall&ownerId=valentijn&avatarId=11101",
                        "32x32":"https://jira.onpremise.org/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
                     },
                     "displayName":"Valentijn Scholten",
                     "active":"true",
                     "timeZone":"Europe/Amsterdam"
                  },
                  "body":"test2",
                  "updateAuthor":{
                     "self":"https://jira.onpremise.org/rest/api/2/user?username=valentijn",
                     "name":"valentijn",
                     "key":"valentijn",
                     "emailAddress":"valentijn.scholten@isaac.nl",
                     "avatarUrls":{
                        "48x48":"https://jira.onpremise.org/secure/useravatar?ownerId=valentijn&avatarId=11101",
                        "24x24":"https://jira.onpremise.org/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
                        "16x16":"https://jira.onpremise.org/secure/useravatar?size=xsmall&ownerId=valentijn&avatarId=11101",
                        "32x32":"https://jira.onpremise.org/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
                     },
                     "displayName":"Valentijn Scholten",
                     "active":"true",
                     "timeZone":"Europe/Amsterdam"
                  },
                  "created":"2020-11-11T18:55:21.425+0100",
                  "updated":"2020-11-11T18:55:21.425+0100"
               }
            ],
            "maxResults":2,
            "total":2,
            "startAt":0
         },
         "worklog":{
            "startAt":0,
            "maxResults":20,
            "total":0,
            "worklogs":[
            ]
         }
      }
   },
   "comment":{
      "self":"https://jira.onpremise.org/rest/api/2/issue/2/comment/456843",
      "id":"456843",
      "author":{
         "self":"https://jira.onpremise.org/rest/api/2/user?username=valentijn",
         "name":"valentijn",
         "key":"valentijn",
         "emailAddress":"valentijn.scholten@isaac.nl",
         "avatarUrls":{
            "48x48":"https://jira.onpremise.org/secure/useravatar?ownerId=valentijn&avatarId=11101",
            "24x24":"https://jira.onpremise.org/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
            "16x16":"https://jira.onpremise.org/secure/useravatar?size=xsmall&ownerId=valentijn&avatarId=11101",
            "32x32":"https://jira.onpremise.org/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
         },
         "displayName":"Valentijn Scholten",
         "active":"true",
         "timeZone":"Europe/Amsterdam"
      },
      "body":"test2",
      "updateAuthor":{
         "self":"https://jira.onpremise.org/rest/api/2/user?username=valentijn",
         "name":"valentijn",
         "key":"valentijn",
         "emailAddress":"valentijn.scholten@isaac.nl",
         "avatarUrls":{
            "48x48":"https://jira.onpremise.org/secure/useravatar?ownerId=valentijn&avatarId=11101",
            "24x24":"https://jira.onpremise.org/secure/useravatar?size=small&ownerId=valentijn&avatarId=11101",
            "16x16":"https://jira.onpremise.org/secure/useravatar?size=xsmall&ownerId=valentijn&avatarId=11101",
            "32x32":"https://jira.onpremise.org/secure/useravatar?size=medium&ownerId=valentijn&avatarId=11101"
         },
         "displayName":"Valentijn Scholten",
         "active":"true",
         "timeZone":"Europe/Amsterdam"
      },
      "created":"2020-11-11T18:55:21.425+0100",
      "updated":"2020-11-11T18:55:21.425+0100"
   }
}
"""))
        # finding 5 has a JIRA issue in the initial fixture for unit tests
        jira_issue = JIRA_Issue.objects.get(jira_id=2)
        finding = jira_issue.finding
        notes_count_before = finding.notes.count()

        response = self.client.post(reverse('jira_web_hook_secret', args=(self.correct_secret, )),
                                    body,
                                    content_type="application/json")

        jira_issue = JIRA_Issue.objects.get(jira_id=2)
        finding = jira_issue.finding
        notes_count_after = finding.notes.count()

        self.assertEqual(200, response.status_code)
        self.assertEqual(notes_count_after, notes_count_before)
        self.assertTrue(finding.is_Mitigated)
        self.assertFalse(finding.active)
        self.assertIsNotNone(finding.mitigated)
