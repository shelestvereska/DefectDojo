import datetime
from dojo.importers import utils as importer_utils
from dojo.models import Test, Finding, \
    Test_Type, \
    BurpRawRequestResponse, \
    Endpoint_Status, \
    Test_Import
from dojo.endpoint.utils import endpoint_get_or_create

from dojo.utils import get_current_user, max_safe

from django.core.exceptions import MultipleObjectsReturned
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
import dojo.notifications.helper as notifications_helper
import dojo.finding.helper as finding_helper
import dojo.jira_link.helper as jira_helper
import base64
import logging

from dojo.tools.factory import get_parser

logger = logging.getLogger(__name__)
deduplicationLogger = logging.getLogger("dojo.specific-loggers.deduplication")


class DojoDefaultImporter(object):

    def create_test(self, scan_type, test_type_name, engagement, lead, environment, tags=None,
                    scan_date=None, version=None, branch_tag=None, build_id=None, commit_hash=None, now=timezone.now(),
                    api_scan_configuration=None):

        test_type, created = Test_Type.objects.get_or_create(
            name=test_type_name)

        if created:
            logger.info('Created new Test_Type with name %s because a report is being imported', test_type.name)

        test = Test(
            engagement=engagement,
            lead=lead,
            test_type=test_type,
            scan_type=scan_type,
            target_start=scan_date if scan_date else now.date(),
            target_end=scan_date if scan_date else now.date(),
            environment=environment,
            percent_complete=100,
            version=version,
            branch_tag=branch_tag,
            build_id=build_id,
            commit_hash=commit_hash,
            api_scan_configuration=api_scan_configuration,
            tags=tags)
        try:
            # TODO What is going on here?
            test.full_clean()
        except ValidationError:
            pass

        test.save()
        return test

    def process_parsed_findings(self, test, parsed_findings, scan_type, user, active, verified, minimum_severity=None,
                                endpoints_to_add=None, push_to_jira=None, group_by=None, now=timezone.now(), service=None):
        logger.debug('endpoints_to_add: %s', endpoints_to_add)
        new_findings = []
        items = parsed_findings
        logger.debug('starting import of %i items.', len(items) if items else 0)
        i = 0
        for item in items:
            # FIXME hack to remove when all parsers have unit tests for this attribute
            if item.severity.lower().startswith('info') and item.severity != 'Info':
                item.severity = 'Info'

            item.numerical_severity = Finding.get_numerical_severity(item.severity)

            if minimum_severity and (Finding.SEVERITIES[item.severity] >
                    Finding.SEVERITIES[minimum_severity]):
                # finding's severity is below the configured threshold : ignoring the finding
                continue

            item.test = test
            item.reporter = user if user else get_current_user
            item.last_reviewed = now
            item.last_reviewed_by = user if user else get_current_user

            # Only set active/verified flags if they were NOT set by default value(True)
            if item.active:
                item.active = active
            if item.verified:
                item.verified = verified

            item.created = now
            item.updated = now

            item.service = service

            item.save(dedupe_option=False)

            if settings.FEATURE_FINDING_GROUPS and group_by:
                finding_helper.add_finding_to_auto_group(item, group_by)

            if (hasattr(item, 'unsaved_req_resp') and
                    len(item.unsaved_req_resp) > 0):
                for req_resp in item.unsaved_req_resp:
                    burp_rr = BurpRawRequestResponse(
                        finding=item,
                        burpRequestBase64=base64.b64encode(req_resp["req"].encode("utf-8")),
                        burpResponseBase64=base64.b64encode(req_resp["resp"].encode("utf-8")))
                    burp_rr.clean()
                    burp_rr.save()

            if (item.unsaved_request is not None and
                    item.unsaved_response is not None):
                burp_rr = BurpRawRequestResponse(
                    finding=item,
                    burpRequestBase64=base64.b64encode(item.unsaved_request.encode()),
                    burpResponseBase64=base64.b64encode(item.unsaved_response.encode()))
                burp_rr.clean()
                burp_rr.save()

            for endpoint in item.unsaved_endpoints:
                try:
                    endpoint.clean()
                except ValidationError as e:
                    logger.warning("DefectDojo is storing broken endpoint because cleaning wasn't successful: "
                                   "{}".format(e))

                try:
                    ep, created = endpoint_get_or_create(
                        protocol=endpoint.protocol,
                        userinfo=endpoint.userinfo,
                        host=endpoint.host,
                        port=endpoint.port,
                        path=endpoint.path,
                        query=endpoint.query,
                        fragment=endpoint.fragment,
                        product=test.engagement.product)
                except (MultipleObjectsReturned):
                    pass

                try:
                    eps, created = Endpoint_Status.objects.get_or_create(
                        finding=item,
                        endpoint=ep)
                except (MultipleObjectsReturned):
                    pass

                ep.endpoint_status.add(eps)
                item.endpoint_status.add(eps)
                item.endpoints.add(ep)

            if endpoints_to_add:
                for endpoint in endpoints_to_add:
                    logger.debug('adding endpoint %s', endpoint)
                    # TODO Not sure what happens here, we get an endpoint model and try to create it again?
                    try:
                        endpoint.clean()
                    except ValidationError as e:
                        logger.warning("DefectDojo is storing broken endpoint because cleaning wasn't successful: "
                                       "{}".format(e))

                    try:
                        ep, created = endpoint_get_or_create(
                            protocol=endpoint.protocol,
                            userinfo=endpoint.userinfo,
                            host=endpoint.host,
                            port=endpoint.port,
                            path=endpoint.path,
                            query=endpoint.query,
                            fragment=endpoint.fragment,
                            product=test.engagement.product)
                    except (MultipleObjectsReturned):
                        pass
                    try:
                        eps, created = Endpoint_Status.objects.get_or_create(
                            finding=item,
                            endpoint=ep)
                    except (MultipleObjectsReturned):
                        pass

                    ep.endpoint_status.add(eps)
                    item.endpoints.add(ep)
                    item.endpoint_status.add(eps)

            if item.unsaved_tags:
                item.tags = item.unsaved_tags

            new_findings.append(item)
            # to avoid pushing a finding group multiple times, we push those outside of the loop
            if settings.FEATURE_FINDING_GROUPS and item.finding_group:
                item.save()
            else:
                item.save(push_to_jira=push_to_jira)

        if settings.FEATURE_FINDING_GROUPS and push_to_jira:
            for finding_group in set([finding.finding_group for finding in new_findings if finding.finding_group is not None]):
                jira_helper.push_to_jira(finding_group)

        return new_findings

    def close_old_findings(self, test, scan_date_time, user, push_to_jira=None):
        old_findings = []
        # Close old active findings that are not reported by this scan.
        new_hash_codes = test.finding_set.values('hash_code')

        # TODO I don't think these criteria are 100% correct, why are findings with the same hash_code excluded?
        # Would it make more sense to exclude duplicates? But the deduplication process can be unfinished because it's
        # run in a celery async task...
        if test.engagement.deduplication_on_engagement:
            old_findings = Finding.objects.exclude(test=test) \
                                            .exclude(hash_code__in=new_hash_codes) \
                                            .filter(test__engagement=test.engagement,
                                                test__test_type=test.test_type,
                                                active=True)
        else:
            # TODO BUG? this will violate the deduplication_on_engagement setting for other engagements
            old_findings = Finding.objects.exclude(test=test) \
                                            .exclude(hash_code__in=new_hash_codes) \
                                            .filter(test__engagement__product=test.engagement.product,
                                                test__test_type=test.test_type,
                                                active=True)

        for old_finding in old_findings:
            old_finding.active = False
            old_finding.is_mitigated = True
            old_finding.mitigated = scan_date_time
            old_finding.notes.create(author=user,
                                        entry="This finding has been automatically closed"
                                        " as it is not present anymore in recent scans.")
            endpoint_status = old_finding.endpoint_status.all()
            for status in endpoint_status:
                status.mitigated_by = user
                status.mitigated_time = timezone.now()
                status.mitigated = True
                status.last_modified = timezone.now()
                status.save()

            old_finding.tags.add('stale')

            # to avoid pushing a finding group multiple times, we push those outside of the loop
            if settings.FEATURE_FINDING_GROUPS and old_finding.finding_group:
                # don't try to dedupe findings that we are closing
                old_finding.save(dedupe_option=False)
            else:
                old_finding.save(dedupe_option=False, push_to_jira=push_to_jira)

        if settings.FEATURE_FINDING_GROUPS and push_to_jira:
            for finding_group in set([finding.finding_group for finding in old_findings if finding.finding_group is not None]):
                jira_helper.push_to_jira(finding_group)

        return old_findings

    def update_timestamps(self, test, scan_date, version, branch_tag, build_id, commit_hash, now, scan_date_time):
        test.engagement.updated = now
        if test.engagement.engagement_type == 'CI/CD':
            test.engagement.target_end = max_safe([scan_date, test.engagement.target_end])

        test.updated = now
        test.target_end = max_safe([scan_date_time, test.target_end])

        if version:
            test.version = version

        if branch_tag:
            test.branch_tag = branch_tag
            test.engagement.version = version

        if build_id:
            test.build_id = build_id

        if branch_tag:
            test.commit_hash = commit_hash

        test.save()
        test.engagement.save()

    def import_scan(self, scan, scan_type, engagement, lead, environment, active, verified, tags=None, minimum_severity=None,
                    user=None, endpoints_to_add=None, scan_date=None, version=None, branch_tag=None, build_id=None,
                    commit_hash=None, push_to_jira=None, close_old_findings=False, group_by=None, api_scan_configuration=None,
                    service=None):

        logger.debug(f'IMPORT_SCAN: parameters: {locals()}')

        user = user or get_current_user()

        now = timezone.now()
        # retain weird existing logic to use current time for provided scan date
        scan_date_time = datetime.datetime.combine(scan_date, timezone.now().time())
        if settings.USE_TZ:
            scan_date_time = timezone.make_aware(scan_date_time, timezone.get_default_timezone())

        if api_scan_configuration and api_scan_configuration.product != engagement.product:
            raise ValidationError('API Scan Configuration has to be from same product as  the Engagement')

        # check if the parser that handle the scan_type manage tests
        # if yes, we parse the data first
        # after that we customize the Test_Type to reflect the data
        # This allow us to support some meta-formats like SARIF or the generic format
        parser = get_parser(scan_type)
        if hasattr(parser, 'get_tests'):
            logger.debug('IMPORT_SCAN parser v2: Create Test and parse findings')
            tests = parser.get_tests(scan_type, scan)
            # for now we only consider the first test in the list and artificially aggregate all findings of all tests
            # this is the same as the old behavior as current import/reimporter implementation doesn't handle the case
            # when there is more than 1 test
            #
            # we also aggregate the label of the Test_type to show the user the original scan_type
            # only if they are different. This is to support meta format like SARIF
            # so a report that have the label 'CodeScanner' will be changed to 'CodeScanner Scan (SARIF)'
            test_type_name = scan_type
            if len(tests) > 0:
                if tests[0].type:
                    test_type_name = tests[0].type + " Scan"
                    if test_type_name != scan_type:
                        test_type_name = f"{test_type_name} ({scan_type})"

                test = self.create_test(scan_type, test_type_name, engagement, lead, environment, scan_date=scan_date, tags=tags,
                                    version=version, branch_tag=branch_tag, build_id=build_id, commit_hash=commit_hash, now=now,
                                    api_scan_configuration=api_scan_configuration)
                # This part change the name of the Test
                # we get it from the data of the parser
                test_raw = tests[0]
                if test_raw.name:
                    test.name = test_raw.name
                if test_raw.description:
                    test.description = test_raw.description
                test.save()

                logger.debug('IMPORT_SCAN parser v2: Parse findings (aggregate)')
                # currently we only support import one Test
                # so for parser that support multiple tests (like SARIF)
                # we aggregate all the findings into one uniq test
                parsed_findings = []
                for test_raw in tests:
                    parsed_findings.extend(test_raw.findings)
            else:
                logger.info(f'No tests found in import for {scan_type}')
        else:
            logger.debug('IMPORT_SCAN: Create Test')
            # by default test_type == scan_type
            test = self.create_test(scan_type, scan_type, engagement, lead, environment, scan_date=scan_date, tags=tags,
                                version=version, branch_tag=branch_tag, build_id=build_id, commit_hash=commit_hash, now=now,
                                api_scan_configuration=api_scan_configuration)

            logger.debug('IMPORT_SCAN: Parse findings')
            parser = get_parser(scan_type)
            parsed_findings = parser.get_findings(scan, test)

        logger.debug('IMPORT_SCAN: Processing findings')
        new_findings = self.process_parsed_findings(test, parsed_findings, scan_type, user, active,
                                                    verified, minimum_severity=minimum_severity,
                                                    endpoints_to_add=endpoints_to_add, push_to_jira=push_to_jira,
                                                    group_by=group_by, now=now, service=service)

        closed_findings = []
        if close_old_findings:
            logger.debug('IMPORT_SCAN: Closing findings no longer present in scan report')
            closed_findings = self.close_old_findings(test, scan_date_time, user=user, push_to_jira=push_to_jira)

        logger.debug('IMPORT_SCAN: Updating test/engagement timestamps')
        importer_utils.update_timestamps(test, scan_date, version, branch_tag, build_id, commit_hash, now, scan_date_time)

        if settings.TRACK_IMPORT_HISTORY:
            logger.debug('IMPORT_SCAN: Updating Import History')
            importer_utils.update_import_history(Test_Import.IMPORT_TYPE, active, verified, tags, minimum_severity,
                                                    endpoints_to_add, version, branch_tag, build_id, commit_hash,
                                                    push_to_jira, close_old_findings, test, new_findings, closed_findings)

        logger.debug('IMPORT_SCAN: Generating notifications')
        notifications_helper.notify_test_created(test)
        updated_count = len(new_findings) + len(closed_findings)
        if updated_count > 0:
            notifications_helper.notify_scan_added(test, updated_count, new_findings=new_findings, findings_mitigated=closed_findings)

        logger.debug('IMPORT_SCAN: Done')

        return test, len(new_findings), len(closed_findings)
