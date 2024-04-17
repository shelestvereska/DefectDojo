scoutsuite_results =
{
  "account_id": "gcp-project-id",
  "all_projects": false,
  "environment": "default",
  "folder_id": null,
  "last_run": {
    "ruleset_about": "This ruleset consists of numerous rules that are considered standard by NCC Group. The rules enabled range from violations of well-known security best practices to gaps resulting from less-known security implications of provider-specific mechanisms. Additional rules exist, some of them requiring extra-parameters to be configured, and some of them being applicable to a limited number of users.",
    "ruleset_name": "default",
    "run_parameters": {
      "excluded_regions": null,
      "regions": null,
      "services": [],
      "skipped_services": []
    },
    "summary": {
      "cloudsql": {
        "checked_items": 0,
        "flagged_items": 0,
        "max_level": "warning",
        "resources_count": 0,
        "rules_count": 6
      },
      "cloudstorage": {
        "checked_items": 8,
        "flagged_items": 4,
        "max_level": "warning",
        "resources_count": 2,
        "rules_count": 4
      },
      "computeengine": {
        "checked_items": 0,
        "flagged_items": 0,
        "max_level": "warning",
        "resources_count": 0,
        "rules_count": 11
      },
      "iam": {
        "checked_items": 0,
        "flagged_items": 0,
        "max_level": "warning",
        "resources_count": 0,
        "rules_count": 9
      },
      "kms": {
        "checked_items": 0,
        "flagged_items": 0,
        "max_level": "warning",
        "resources_count": 0,
        "rules_count": 0
      },
      "kubernetesengine": {
        "checked_items": 0,
        "flagged_items": 0,
        "max_level": "warning",
        "resources_count": 0,
        "rules_count": 19
      },
      "stackdriverlogging": {
        "checked_items": 1,
        "flagged_items": 0,
        "max_level": "warning",
        "resources_count": 2,
        "rules_count": 1
      },
      "stackdrivermonitoring": {
        "checked_items": 0,
        "flagged_items": 0,
        "max_level": "warning",
        "resources_count": 0,
        "rules_count": 0
      }
    },
    "time": "2021-01-08 17:28:00+0100",
    "version": "5.10.2"
  },
  "metadata": {
    "compute": {
      "computeengine": {
        "resources": {
          "firewalls": {
            "cols": 2,
            "count": 0,
            "full_path": "services.computeengine.projects.id.firewalls",
            "path": "services.computeengine.projects.id.firewalls",
            "script": "services.computeengine.projects.firewalls"
          },
          "instances": {
            "cols": 2,
            "count": 0,
            "full_path": "services.computeengine.projects.id.zones.id.instances",
            "path": "services.computeengine.projects.id.zones.id.instances",
            "script": "services.computeengine.projects.zones.instances"
          },
          "networks": {
            "cols": 2,
            "count": 0,
            "full_path": "services.computeengine.projects.id.networks",
            "path": "services.computeengine.projects.id.networks",
            "script": "services.computeengine.projects.networks"
          },
          "snapshots": {
            "cols": 2,
            "count": 0,
            "full_path": "services.computeengine.projects.id.snapshots",
            "path": "services.computeengine.projects.id.snapshots",
            "script": "services.computeengine.projects.snapshots"
          },
          "subnetworks": {
            "cols": 2,
            "count": 0,
            "full_path": "services.computeengine.projects.id.regions.id.subnetworks",
            "path": "services.computeengine.projects.id.regions.id.subnetworks",
            "script": "services.computeengine.projects.regions.subnetworks"
          }
        }
      },
      "kubernetesengine": {
        "resources": {
          "clusters": {
            "cols": 2,
            "count": 0,
            "full_path": "services.kubernetesengine.projects.id.zones.id.clusters",
            "path": "services.kubernetesengine.projects.id.zones.id.clusters",
            "script": "services.kubernetesengine.projects.zones.clusters"
          }
        }
      }
    },
    "database": {
      "cloudsql": {
        "resources": {
          "instances": {
            "cols": 2,
            "count": 0,
            "full_path": "services.cloudsql.projects.id.instances",
            "path": "services.cloudsql.projects.id.instances",
            "script": "services.cloudsql.projects.instances"
          }
        }
      }
    },
    "management": {
      "stackdriverlogging": {
        "resources": {
          "metrics": {
            "cols": 2,
            "count": 0,
            "full_path": "services.stackdriverlogging.projects.id.metrics",
            "path": "services.stackdriverlogging.projects.id.metrics",
            "script": "services.stackdriverlogging.projects.metrics"
          },
          "sinks": {
            "cols": 2,
            "count": 2,
            "full_path": "services.stackdriverlogging.projects.id.sinks",
            "path": "services.stackdriverlogging.projects.id.sinks",
            "script": "services.stackdriverlogging.projects.sinks"
          }
        }
      },
      "stackdrivermonitoring": {
        "resources": {
          "alert_policies": {
            "cols": 2,
            "count": 0,
            "full_path": "services.stackdrivermonitoring.projects.id.alert_policies",
            "path": "services.stackdrivermonitoring.projects.id.alert_policies",
            "script": "services.stackdrivermonitoring.projects.alert_policies"
          },
          "uptime_checks": {
            "cols": 2,
            "count": 0,
            "full_path": "services.stackdrivermonitoring.projects.id.uptime_checks",
            "path": "services.stackdrivermonitoring.projects.id.uptime_checks",
            "script": "services.stackdrivermonitoring.projects.uptime_checks"
          }
        }
      }
    },
    "security": {
      "iam": {
        "resources": {
          "bindings": {
            "cols": 2,
            "count": 0,
            "full_path": "services.iam.projects.id.bindings",
            "path": "services.iam.projects.id.bindings",
            "script": "services.iam.projects.bindings"
          },
          "groups": {
            "cols": 2,
            "count": 0,
            "full_path": "services.iam.projects.id.groups",
            "path": "services.iam.projects.id.groups",
            "script": "services.iam.projects.groups"
          },
          "service_accounts": {
            "cols": 2,
            "count": 0,
            "full_path": "services.iam.projects.id.service_accounts",
            "path": "services.iam.projects.id.service_accounts",
            "script": "services.iam.projects.service_accounts"
          },
          "users": {
            "cols": 2,
            "count": 0,
            "full_path": "services.iam.projects.id.users",
            "path": "services.iam.projects.id.users",
            "script": "services.iam.projects.users"
          }
        }
      },
      "kms": {
        "resources": {
          "keyrings": {
            "cols": 2,
            "count": 0,
            "full_path": "services.kms.projects.id.keyrings",
            "path": "services.kms.projects.id.keyrings",
            "script": "services.kms.projects.keyrings"
          }
        }
      }
    },
    "storage": {
      "cloudstorage": {
        "resources": {
          "buckets": {
            "cols": 2,
            "count": 2,
            "full_path": "services.cloudstorage.projects.id.buckets",
            "path": "services.cloudstorage.projects.id.buckets",
            "script": "services.cloudstorage.projects.buckets"
          }
        }
      }
    }
  },
  "organization_id": null,
  "project_id": "gcp-project-id",
  "provider_code": "gcp",
  "provider_name": "Google Cloud Platform",
  "result_format": "json",
  "service_list": [
    "cloudsql",
    "cloudstorage",
    "computeengine",
    "iam",
    "kms",
    "stackdriverlogging",
    "stackdrivermonitoring",
    "kubernetesengine"
  ],
  "services": {
    "cloudsql": {
      "filters": {},
      "findings": {
        "cloudsql-allows-root-login-from-any-host": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "6.4",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Instances",
          "description": "Instance Allows Root Login from Any Host",
          "flagged_items": 0,
          "id_suffix": "root_access_from_any_host",
          "items": [],
          "level": "warning",
          "path": "cloudsql.projects.id.instances.id",
          "rationale": "Root access to MySQL Database Instances should be allowed only through trusted IPs.",
          "references": [
            "https://forsetisecurity.org/docs/latest/concepts/best-practices.html#cloud-sql",
            "https://cloud.google.com/blog/products/gcp/best-practices-for-securing-your-google-cloud-databases"
          ],
          "remediation": null,
          "service": "Cloud SQL"
        },
        "cloudsql-instance-backups-disabled": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Instances",
          "description": "Instance with Automatic Backups Disabled",
          "flagged_items": 0,
          "id_suffix": "automatic_backup_enabled",
          "items": [],
          "level": "warning",
          "path": "cloudsql.projects.id.instances.id",
          "rationale": "Automatic backups should be configured for Cloud SQL instances in order to ensure backups are created regularly.",
          "references": [
            "https://cloud.google.com/sql/docs/mysql/backup-recovery/backups"
          ],
          "remediation": null,
          "service": "Cloud SQL"
        },
        "cloudsql-instance-is-open-to-the-world": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "6.2",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Instances",
          "description": "Instance Allowing All Incoming Connections",
          "display_path": "cloudsql.projects.id.instances.id",
          "flagged_items": 0,
          "id_suffix": "open_to_the_world",
          "items": [],
          "level": "danger",
          "path": "cloudsql.projects.id.instances.id.authorized_networks.id",
          "rationale": "Database instances should accept connections from trusted IPs and networks only.",
          "references": null,
          "remediation": null,
          "service": "Cloud SQL"
        },
        "cloudsql-instance-no-binary-logging": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Instances",
          "description": "Instance with Binary Logging Disabled",
          "flagged_items": 0,
          "id_suffix": "log_enabled",
          "items": [],
          "level": "warning",
          "path": "cloudsql.projects.id.instances.id",
          "rationale": "The benefits of enabling binary logs (replication, scalability, auditability, point-in-time data recovery, etc.) can improve the security posture of the Cloud SQL instance.",
          "references": [
            "https://cloud.google.com/sql/docs/mysql/instance-settings",
            "https://cloud.google.com/sql/docs/mysql/replication/tips"
          ],
          "remediation": null,
          "service": "Cloud SQL"
        },
        "cloudsql-instance-ssl-not-required": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "6.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Instances",
          "description": "Instance Not Requiring SSL for Incoming Connections",
          "flagged_items": 0,
          "id_suffix": "ssl_required",
          "items": [],
          "level": "warning",
          "path": "cloudsql.projects.id.instances.id",
          "rationale": "All incoming connections to databases should require the use of SSL.",
          "references": [
            "https://cloud.google.com/sql/docs/mysql/authorize-ssl"
          ],
          "remediation": null,
          "service": "Cloud SQL"
        },
        "cloudsql-instance-with-no-backups": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Instances",
          "description": "Instance with No Backups",
          "flagged_items": 0,
          "id_suffix": "last_backup_timestamp",
          "items": [],
          "level": "warning",
          "path": "cloudsql.projects.id.instances.id",
          "rationale": "Weekly or monthly backups should be created of all databases holding sensitive information.",
          "references": [
            "https://cloud.google.com/sql/docs/mysql/backup-recovery/backups"
          ],
          "remediation": null,
          "service": "Cloud SQL"
        }
      },
      "instances_count": 0,
      "projects": {
        "gcp-project-id": {
          "instances": {},
          "instances_count": 0
        }
      }
    },
    "cloudstorage": {
      "buckets_count": 2,
      "filters": {},
      "findings": {
        "cloudstorage-bucket-allAuthenticatedUsers": {
          "checked_items": 2,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "5.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Buckets",
          "description": "Bucket Accessible by \"allAuthenticatedUsers\"",
          "display_path": "cloudstorage.projects.id.buckets.id",
          "flagged_items": 0,
          "id_suffix": "allAuthenticatedUsers",
          "items": [],
          "level": "danger",
          "path": "cloudstorage.projects.id.buckets.id",
          "rationale": "Allowing anonymous and/or public access grants permissions to anyone to access bucket content. Such access might not be desired if you are storing any sensitive data. Hence, ensure that anonymous and/or public access to a bucket is not allowed.",
          "references": [
            "https://cloud.google.com/storage/docs/access-control/iam-reference",
            "https://cloud.google.com/storage/docs/access-control/making-data-public"
          ],
          "remediation": "No role should contain \"allUsers\" and/or \"allAuthenticatedUsers\" as a member.",
          "service": "Cloud Storage"
        },
        "cloudstorage-bucket-allUsers": {
          "checked_items": 2,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "5.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Buckets",
          "description": "Bucket Accessible by \"allUsers\"",
          "display_path": "cloudstorage.projects.id.buckets.id",
          "flagged_items": 0,
          "id_suffix": "allUsers",
          "items": [],
          "level": "danger",
          "path": "cloudstorage.projects.id.buckets.id",
          "rationale": "Allowing anonymous and/or public access grants permissions to anyone to access bucket content. Such access might not be desired if you are storing any sensitive data. Hence, ensure that anonymous and/or public access to a bucket is not allowed.",
          "references": [
            "https://cloud.google.com/storage/docs/access-control/iam-reference",
            "https://cloud.google.com/storage/docs/access-control/making-data-public"
          ],
          "remediation": "No role should contain \"allUsers\" and/or \"allAuthenticatedUsers\" as a member.",
          "service": "Cloud Storage"
        },
        "cloudstorage-bucket-no-logging": {
          "checked_items": 2,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "5.3",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Buckets",
          "description": "Bucket with Logging Disabled",
          "flagged_items": 2,
          "id_suffix": "logging_enabled",
          "items": [
            "cloudstorage.projects.gcp-project-id.buckets.52fc025e81845686d3c9fe5a5dc4f5e7ae740064.logging_enabled",
            "cloudstorage.projects.gcp-project-id.buckets.be0c682b7f6d9568fed2ec924eea5ebcfe083f3b.logging_enabled"
          ],
          "level": "warning",
          "path": "cloudstorage.projects.id.buckets.id",
          "rationale": "Enable access and storage logs, in order to capture all events which may affect objects within target buckets.",
          "references": [
            "https://cloud.google.com/storage/docs/access-logs"
          ],
          "remediation": null,
          "service": "Cloud Storage"
        },
        "cloudstorage-bucket-no-versioning": {
          "checked_items": 2,
          "compliance": null,
          "dashboard_name": "Buckets",
          "description": "Bucket with Versioning Disabled",
          "flagged_items": 2,
          "id_suffix": "versioning_enabled",
          "items": [
            "cloudstorage.projects.gcp-project-id.buckets.52fc025e81845686d3c9fe5a5dc4f5e7ae740064.versioning_enabled",
            "cloudstorage.projects.gcp-project-id.buckets.be0c682b7f6d9568fed2ec924eea5ebcfe083f3b.versioning_enabled"
          ],
          "level": "warning",
          "path": "cloudstorage.projects.id.buckets.id",
          "rationale": "Enable Object Versioning to protect Cloud Storage data from being overwritten or accidentally deleted.",
          "references": [
            "https://cloud.google.com/storage/docs/using-object-versioning"
          ],
          "remediation": null,
          "service": "Cloud Storage"
        }
      },
      "projects": {
        "gcp-project-id": {
          "buckets": {
            "52fc025e81845686d3c9fe5a5dc4f5e7ae740064": {
              "acls": [
                {
                  "entity": "project-owners-1111111111",
                  "role": "OWNER"
                },
                {
                  "entity": "project-editors-1111111111",
                  "role": "OWNER"
                },
                {
                  "entity": "project-viewers-1111111111",
                  "role": "READER"
                }
              ],
              "creation_date": "2019-01-24 09:35:13.157000+00:00",
              "default_object_acl": [
                {
                  "entity": "project-owners-1111111111",
                  "role": "OWNER"
                },
                {
                  "entity": "project-editors-1111111111",
                  "role": "OWNER"
                },
                {
                  "entity": "project-viewers-1111111111",
                  "role": "READER"
                }
              ],
              "id": "52fc025e81845686d3c9fe5a5dc4f5e7ae740064",
              "location": "EU",
              "logging_enabled": false,
              "member_bindings": {},
              "name": "gcp-project-id.appspot.com",
              "project_id": "gcp-project-id",
              "project_number": 1111111111,
              "storage_class": "standard",
              "uniform_bucket_level_access": false,
              "versioning_enabled": false
            },
            "be0c682b7f6d9568fed2ec924eea5ebcfe083f3b": {
              "acls": [
                {
                  "entity": "project-owners-1111111111",
                  "role": "OWNER"
                },
                {
                  "entity": "project-editors-1111111111",
                  "role": "OWNER"
                },
                {
                  "entity": "project-viewers-1111111111",
                  "role": "READER"
                }
              ],
              "creation_date": "2019-01-24 09:35:13.151000+00:00",
              "default_object_acl": [
                {
                  "entity": "project-owners-1111111111",
                  "role": "OWNER"
                },
                {
                  "entity": "project-editors-1111111111",
                  "role": "OWNER"
                },
                {
                  "entity": "project-viewers-1111111111",
                  "role": "READER"
                }
              ],
              "id": "be0c682b7f6d9568fed2ec924eea5ebcfe083f3b",
              "location": "EU",
              "logging_enabled": false,
              "member_bindings": {},
              "name": "staging.gcp-project-id.appspot.com",
              "project_id": "gcp-project-id",
              "project_number": 1111111111,
              "storage_class": "standard",
              "uniform_bucket_level_access": false,
              "versioning_enabled": false
            }
          },
          "buckets_count": 2
        }
      }
    },
    "computeengine": {
      "filters": {},
      "findings": {
        "computeengine-firewall-default-rule-in-use": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Firewall Rule",
          "description": "Default Firewall Rule in Use",
          "flagged_items": 0,
          "id_suffix": "name",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.firewalls.id",
          "rationale": "Some default firewall rules were in use. This could potentially expose sensitive services or protocols to other networks.",
          "references": null,
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-firewall-rule-allows-all-ports": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Firewall Rule Elements",
          "description": "Firewall Rule Opens All Ports (0-65535)",
          "display_path": "computeengine.projects.id.firewalls.id",
          "flagged_items": 0,
          "id_suffix": "permissive_ports",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.firewalls.id.allowed_traffic.id.ports.id",
          "rationale": "The firewall rule allows access to all ports. This widens the attack surface of the infrastructure and makes it easier for an attacker to reach potentially sensitive services over the network.",
          "references": null,
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-firewall-rule-allows-internal-traffic": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Firewall Rule Elements",
          "description": "Firewall Rule Allows Internal Traffic",
          "display_path": "computeengine.projects.id.firewalls.id",
          "flagged_items": 0,
          "id_suffix": "permissive_ports",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.firewalls.id.allowed_traffic.id.ports.id",
          "rationale": "Firewall rule allows ingress connections for all protocols and ports among instances in the network.",
          "references": null,
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-firewall-rule-allows-port-range": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Firewall Rule Elements",
          "description": "Firewall Rule Allows Port Range(s)",
          "display_path": "computeengine.projects.id.firewalls.id",
          "flagged_items": 0,
          "id_suffix": "permissive_ports",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.firewalls.id.allowed_traffic.id.ports.id",
          "rationale": "It was found that the firewall rule was using port ranges. Sometimes, ranges could include unintended ports that should not be exposed. As a result, when possible, explicit port lists should be used instead.",
          "references": null,
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-firewall-rule-allows-public-access": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Firewall Rules",
          "description": "Firewall Rule Allows Public Access (0.0.0.0/0)",
          "flagged_items": 0,
          "id_suffix": "source_ranges",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.firewalls.id",
          "rationale": "The firewall rule was found to be exposing potentially open ports to all source addresses. Ports are commonly probed by automated scanning tools, and could be an indicator of sensitive services exposed to Internet. If such services need to be exposed, a restriction on the source address could help to reduce the attack surface of the infrastructure.",
          "references": null,
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-firewall-rule-opens-all-ports-to-all": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Firewall Rule Elements",
          "description": "Firewall Rule Allows Public Access (0.0.0.0/0) to All Ports (0-65535)",
          "display_path": "computeengine.projects.id.firewalls.id",
          "flagged_items": 0,
          "id_suffix": "permissive_ports",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.firewalls.id.allowed_traffic.id.ports.id",
          "rationale": "The firewall rule was found to be exposing all ports to all source addresses. Ports are commonly probed by automated scanning tools, and could be an indicator of sensitive services exposed to Internet. If such services need to be exposed, a restriction on the source address could help to reduce the attack surface of the infrastructure.",
          "references": null,
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-firewall-rule-opens-sensitive-port-to-all": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Firewall Rule Elements",
          "description": "Firewall INGRESS Rule Allows Public Access (0.0.0.0/0) to a Sensitive Port",
          "display_path": "computeengine.projects.id.firewalls.id",
          "flagged_items": 0,
          "id_suffix": "permissive_ports",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.firewalls.id.allowed_traffic.id.ports.id",
          "rationale": "The firewall rule was found to be exposing a well-known port to all source addresses. Well-known ports are commonly probed by automated scanning tools, and could be an indicator of sensitive services exposed to Internet. If such services need to be exposed, a restriction on the source address could help to reduce the attack surface of the infrastructure.",
          "references": null,
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-instance-disk-with-no-snapshot": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Instances",
          "description": "Instance Disk without Snapshots",
          "display_path": "computeengine.projects.id.zones.id.instances.id",
          "flagged_items": 0,
          "id_suffix": "latest_snapshot",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.zones.id.instances.id.disks.id",
          "rationale": "You should have snapshots of your in-use or available disks taken on a regular basis to enable disaster recovery efforts.",
          "references": [
            "https://cloud.google.com/compute/docs/disks/create-snapshots",
            "https://cloud.google.com/compute/docs/disks/scheduled-snapshots",
            "https://cloud.google.com/compute/docs/disks/snapshot-best-practices"
          ],
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-instance-with-deletion-protection-disabled": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Instances",
          "description": "Instance without Deletion Protection",
          "flagged_items": 0,
          "id_suffix": "deletion_protection_enabled",
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.zones.id.instances.id",
          "rationale": "It is good practice to enable this feature on production instances, to ensure that they may not be deleted by accident.",
          "references": [
            "https://cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion"
          ],
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-network-with-no-instances": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Networks",
          "description": "Network without Instances",
          "flagged_items": 0,
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.networks.id",
          "rationale": "Maintaining unused resources increases risks of misconfigurations and increases the difficulty of audits.",
          "references": null,
          "remediation": null,
          "service": "Compute Engine"
        },
        "computeengine-old-disk-snapshot": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Snapshots",
          "description": "Old Instance Disk Snapshot",
          "flagged_items": 0,
          "items": [],
          "level": "warning",
          "path": "computeengine.projects.id.snapshots.id",
          "rationale": "Disk snapshots that are over 90 days are likely to be outdated.",
          "references": [
            "https://cloud.google.com/compute/docs/disks/create-snapshots",
            "https://cloud.google.com/compute/docs/disks/scheduled-snapshots",
            "https://cloud.google.com/compute/docs/disks/snapshot-best-practices"
          ],
          "remediation": null,
          "service": "Compute Engine"
        }
      },
      "firewalls_count": 0,
      "instances_count": 0,
      "networks_count": 0,
      "projects": {},
      "snapshots_count": 0,
      "subnetworks_count": 0
    },
    "iam": {
      "bindings_count": 0,
      "filters": {},
      "findings": {
        "iam-gmail-accounts-used": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "1.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Users",
          "description": "Gmail Account in Use",
          "flagged_items": 0,
          "id_suffix": "name",
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.users.id",
          "rationale": "Gmail accounts are personally created and controllable accounts. Organizations seldom have any control over them. Thus, it is recommended that you use fully managed corporate Google accounts for increased visibility, auditing, and control over access to Cloud Platform resources.",
          "references": null,
          "remediation": null,
          "service": "IAM"
        },
        "iam-lack-of-service-account-key-rotation": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "1.6",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Service Accounts",
          "description": "Lack of Service Account Key Rotation",
          "display_path": "iam.projects.id.service_accounts.id",
          "flagged_items": 0,
          "id_suffix": "valid_after",
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.service_accounts.id.keys.id",
          "rationale": "Rotating Service Account keys will reduce the window of opportunity for an access key that is associated with a compromised or terminated account to be used. Service Account keys should be rotated to ensure that data cannot be accessed with an old key which might have been lost, cracked, or stolen. It should be ensured that keys are rotated every 90 days.",
          "references": [
            "https://cloud.google.com/iam/docs/creating-managing-service-account-keys"
          ],
          "remediation": null,
          "service": "IAM"
        },
        "iam-primitive-role-in-use": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "1.4",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Bindings",
          "description": "Primitive Role in Use",
          "flagged_items": 0,
          "id_suffix": "name",
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.bindings.id",
          "rationale": "Primitive roles grant significant privileges. In most cases, usage of these roles is not recommended and does not follow security best practice.<br><br><b>Note: </b>This rule may flag Google-Managed Service Accounts. Google services rely on these Service Accounts having access to the project, and recommends not removing or changing the Service Account's role (see https://cloud.google.com/iam/docs/service-accounts#google-managed).",
          "references": [
            "https://cloud.google.com/iam/docs/understanding-roles",
            "https://cloud.google.com/iam/docs/using-iam-securely"
          ],
          "remediation": null,
          "service": "IAM"
        },
        "iam-role-assigned-to-user": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Bindings",
          "description": "IAM Role Assigned to User",
          "flagged_items": 0,
          "id_suffix": "users",
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.bindings.id",
          "rationale": "Best practices recommends granting roles to a Google Suite group instead of to individual users when possible. It is easier to add members to and remove members from a group instead of updating a Cloud IAM policy to add or remove users.",
          "references": [
            "https://cloud.google.com/iam/docs/understanding-roles",
            "https://cloud.google.com/iam/docs/using-iam-securely"
          ],
          "remediation": null,
          "service": "IAM"
        },
        "iam-sa-has-admin-privileges": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "1.4",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Bindings",
          "description": "Service Account with Admin Privileges",
          "flagged_items": 0,
          "id_suffix": "service_accounts",
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.bindings.id",
          "rationale": "Service accounts represent service-level security of the Resources (application or a VM) which can be determined by the roles assigned to it. Enrolling Service Accounts with administrative privileges grants full access to assigned application or a VM, Service Account Access holder can user.<br><br><b>Note: </b>This rule may flag Google-Managed Service Accounts. Google services rely on these Service Accounts having access to the project, and recommends not removing or changing the Service Account's role",
          "references": [
            "https://cloud.google.com/iam/docs/service-accounts#google-managed",
            "https://cloud.google.com/iam/docs/understanding-roles",
            "https://cloud.google.com/iam/docs/using-iam-securely"
          ],
          "remediation": null,
          "service": "IAM"
        },
        "iam-service-account-user-allAuthenticatedUsers": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Service Accounts",
          "description": "Service Account with 'allAuthenticatedUsers' Service Account User",
          "display_path": "iam.projects.id.service_accounts.id",
          "flagged_items": 0,
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.service_accounts.id.bindings.id",
          "rationale": "Access to the Service Account User role (roles/iam.serviceAccountUser) should be restricted, as members granted this role on a service account can use it to indirectly access all the resources to which the service account has access. ",
          "references": [
            "https://cloud.google.com/iam/docs/service-accounts#user-role"
          ],
          "remediation": null,
          "service": "IAM"
        },
        "iam-service-account-user-allUsers": {
          "checked_items": 0,
          "compliance": null,
          "dashboard_name": "Service Accounts",
          "description": "Service Account with 'allUsers' Service Account User",
          "display_path": "iam.projects.id.service_accounts.id",
          "flagged_items": 0,
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.service_accounts.id.bindings.id",
          "rationale": "Access to the Service Account User role (roles/iam.serviceAccountUser) should be restricted, as members granted this role on a service account can use it to indirectly access all the resources to which the service account has access. ",
          "references": [
            "https://cloud.google.com/iam/docs/service-accounts#user-role"
          ],
          "remediation": null,
          "service": "IAM"
        },
        "iam-service-account-with-user-managed-keys": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "1.3",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Service Accounts",
          "description": "User-Managed Service Account Keys",
          "display_path": "iam.projects.id.service_accounts.id",
          "flagged_items": 0,
          "id_suffix": "key_type",
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.service_accounts.id.keys.id",
          "rationale": "It is recommended to prevent use of user-managed service account keys, as anyone who has access to the keys will be able to access resources through the service account. Best practice recommends using GCP-managed keys, which are used by Cloud Platform services such as App Engine and Compute Engine. These keys cannot be downloaded. Google will keep the keys and automatically rotate them on an approximately weekly basis.",
          "references": [
            "https://cloud.google.com/iam/docs/understanding-service-accounts#managing_service_account_keys"
          ],
          "remediation": null,
          "service": "IAM"
        },
        "iam-user-has-sa-user-role": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "1.5",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Bindings",
          "description": "User with \"Service Account User\" Role at the Project Level",
          "flagged_items": 0,
          "id_suffix": "user_has_sa_user_role",
          "items": [],
          "level": "warning",
          "path": "iam.projects.id.bindings.id",
          "rationale": "Granting the iam.serviceAccountUser role to a user for a project gives the user access to all service accounts in the project, including service accounts that may be created in the future. This can result into elevation of privileges by using service accounts and corresponding Compute Engine instances.",
          "references": [
            "https://cloud.google.com/iam/docs/service-accounts#google-managed",
            "https://cloud.google.com/iam/docs/understanding-roles",
            "https://cloud.google.com/iam/docs/using-iam-securely"
          ],
          "remediation": null,
          "service": "IAM"
        }
      },
      "groups_count": 0,
      "projects": {},
      "service_accounts_count": 0,
      "users_count": 0
    },
    "kms": {
      "filters": {},
      "findings": {},
      "keyrings_count": 0,
      "projects": {}
    },
    "kubernetesengine": {
      "clusters_count": 0,
      "filters": {},
      "findings": {
        "kubernetesengine-basic-authentication-enabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.10",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.8.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Basic Authentication Enabled",
          "flagged_items": 0,
          "id_suffix": "basic_authentication_enabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "Basic authentication allows a user to authenticate to the cluster with a username and password and it is stored in plain text without any encryption. Disabling Basic authentication will prevent attacks like brute force. Its recommended to use either client certificate or IAM for authentication.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_authn_methods",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#evaluation_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-certificate-authentication-enabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.8.2",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Certificate Authentication Enabled",
          "flagged_items": 0,
          "id_suffix": "client_certificate_enabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "Unless applications use the client certificate authentication method, it should be disabled.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_authn_methods",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#evaluation_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-cluster-alias-ip-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.13",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.6.2",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Alias IP Disabled",
          "flagged_items": 0,
          "id_suffix": "alias_ip_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "With Alias IPs ranges enabled, Kubernetes Engine clusters can allocate IP addresses from a CIDR block known to Google Cloud Platform. This makes your cluster more scalable and allows your cluster to better interact with other GCP products and entities.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_network_access_to_the_control_plane_and_nodes",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-cluster-has-no-labels": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.5",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Clusters Lacking Labels",
          "flagged_items": 0,
          "id_suffix": "has_no_labels",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "Labels enable users to map their own organizational structures onto system objects in a loosely coupled fashion, without requiring clients to store these mappings. Labels can also be used to apply specific security settings and auto configure objects at creation.",
          "references": [
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_namespaces_and_rbac_to_restrict_access_to_cluster_resources"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-cluster-logging-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.1",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.7.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Cluster Logging Disabled",
          "flagged_items": 0,
          "id_suffix": "logging_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "You should enable cluster logging and use a logging service so your cluster can export logs about its activities.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://kubernetes.io/docs/tasks/debug-application-cluster/audit/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#stackdriver_logging",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-cluster-master-authorized-networks-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.4",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.6.3",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Master Authorized Networks Disabled",
          "flagged_items": 0,
          "id_suffix": "master_authorized_networks_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "Master authorized networks blocks untrusted IP addresses from outside Google Cloud Platform. Addresses from inside GCP can still reach your master through HTTPS provided that they have the necessary Kubernetes credentials.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_network_access_to_the_control_plane_and_nodes",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-cluster-monitoring-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.2",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.7.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Cluster Monitoring Disabled",
          "flagged_items": 0,
          "id_suffix": "monitoring_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "You should enable cluster monitoring and use a monitoring service so your cluster can export metrics about its activities.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#stackdriver_logging",
            "https://cloud.google.com/monitoring/kubernetes-engine#about-skm",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-cluster-network-policy-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.11",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.6.7",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Network Policy Disabled",
          "flagged_items": 0,
          "id_suffix": "network_policy_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "By default, pods are non-isolated; they accept traffic from any source. Pods become isolated by having a NetworkPolicy that selects them. Once there is any NetworkPolicy in a namespace selecting a particular pod, that pod will reject any connections that are not allowed by any NetworkPolicy.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_with_network_policy",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/security-overview#network_security",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-cluster-pod-security-policy-config-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.14",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.10.3",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Pod Security Policy Disabled",
          "flagged_items": 0,
          "id_suffix": "pod_security_policy_enabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "A Pod Security Policy is a cluster-level resource that controls security sensitive aspects of the pod specification. The PodSecurityPolicy objects define a set of conditions that a pod must run with in order to be accepted into the system, as well as defaults for the related fields.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies",
            "https://kubernetes.io/docs/concepts/policy/pod-security-policy",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": "Enable the Pod Security Policy. By default, Pod Security Policy is disabled when you create a new cluster.",
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-cluster-private-google-access-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.16",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Private Google Access Disabled",
          "flagged_items": 0,
          "id_suffix": "private_ip_google_access_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "Enabling Private Google Access allows VMs on a subnetwork to use a private IP address to reach Google APIs rather than an external IP address.",
          "references": [
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_network_access_to_the_control_plane_and_nodes"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-dashboard-enabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.6",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.10.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "The GKE Dashboard Enabled",
          "flagged_items": 0,
          "id_suffix": "dashboard_status",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "You should disable the Kubernetes Web UI (Dashboard) when running on Kubernetes Engine. The Kubernetes Web UI (Dashboard) is backed by a highly privileged Kubernetes Service Account.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#disable_kubernetes_dashboard",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-default-service-account-used": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.17",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.2.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Default Service Account in Use",
          "flagged_items": 0,
          "id_suffix": "default_service_account_used",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "You should create and use a minimally privileged service account to run your Kubernetes Engine cluster instead of using the Compute Engine default service account.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-legacy-abac-enabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.3",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.8.4",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Legacy Authorization (ABAC) Enabled",
          "flagged_items": 0,
          "id_suffix": "legacy_abac_enabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "The legacy authorizer in Kubernetes Engine grants broad, statically defined permissions. To ensure that RBAC limits permissions correctly, you must disable the legacy authorizer. RBAC has significant security advantages, can help you ensure that users only have access to cluster resources within their own namespace and is now stable in Kubernetes.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#leave_abac_disabled_default_for_110",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-legacy-metadata-endpoints-enabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.4.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Legacy Metadata Endpoints Enabled",
          "display_path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "flagged_items": 0,
          "id_suffix": "legacy_metadata_endpoints_enabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id.node_pools.id",
          "rationale": "Unless your app uses the legacy metadata endpoints, you should disable them.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#protect_node_metadata_default_for_112",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-node-auto-repair-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.7",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.5.2",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Nodes Auto-Repair Disabled",
          "display_path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "flagged_items": 0,
          "id_suffix": "auto_repair_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id.node_pools.id",
          "rationale": "Auto-repair helps you keep the nodes in your cluster in a healthy, running state.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-node-auto-upgrade-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.8",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.5.3",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Nodes Auto-Upgrade Disabled",
          "display_path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "flagged_items": 0,
          "id_suffix": "auto_upgrade_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id.node_pools.id",
          "rationale": "Auto-upgrades automatically ensures that security updates are applied and kept up to date.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-node-container-optimized-os-not-used": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.9",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.5.1",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Lack of Container-Optimized OS Node Images",
          "flagged_items": 0,
          "id_suffix": "container_optimized_os_not_used",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "The Container-Optimized OS image provides better support, security, and stability than previous images.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-private-cluster-disabled": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.15",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.6.4",
              "version": "1.0.0"
            },
            {
              "name": "CIS GKE Benchmark",
              "reference": "6.6.5",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Private Cluster Disabled",
          "flagged_items": 0,
          "id_suffix": "private_cluster_disabled",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "A private cluster is a cluster that makes your master inaccessible from the public internet. In a private cluster, nodes do not have public IP addresses, so your workloads run in an environment that is isolated from the internet. Nodes have addressed only in the private RFC 1918 address space. Nodes and masters communicate with each other privately using VPC peering.",
          "references": [
            "https://www.cisecurity.org/benchmark/kubernetes/",
            "https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_network_access_to_the_control_plane_and_nodes",
            "https://cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#default_values_on"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        },
        "kubernetesengine-scopes-not-limited": {
          "checked_items": 0,
          "compliance": [
            {
              "name": "CIS Google Cloud Platform Foundations",
              "reference": "7.18",
              "version": "1.0.0"
            }
          ],
          "dashboard_name": "Clusters",
          "description": "Lack of Access Scope Limitation",
          "flagged_items": 0,
          "id_suffix": "scopes_not_limited",
          "items": [],
          "level": "warning",
          "path": "kubernetesengine.projects.id.zones.id.clusters.id",
          "rationale": "If you are not creating a separate service account for your nodes, you should limit the scopes of the node service account to reduce the possibility of a privilege escalation in an attack. This ensures that your default service account does not have permissions beyond those necessary to run your cluster. While the default scopes are limited, they may include scopes beyond the minimally required scopes needed to run your cluster. If you are accessing private images in Google Container Registry, the minimally required scopes are only logging.write, monitoring, and devstorage.read_only.",
          "references": [
            "https://cloud.google.com/kubernetes-engine/docs/how-to/access-scopes"
          ],
          "remediation": null,
          "service": "Kubernetes Engine"
        }
      },
      "projects": {}
    },
    "stackdriverlogging": {
      "filters": {},
      "findings": {
        "stackdriverlogging-no-export-sinks": {
          "checked_items": 1,
          "compliance": null,
          "dashboard_name": "Logging Configurations",
          "description": "Lack of Export Sinks",
          "display_path": "stackdriverlogging.projects.id.sinks",
          "flagged_items": 0,
          "items": [],
          "level": "warning",
          "path": "stackdriverlogging.projects.id",
          "rationale": "Export sinks for Stackdriver logging were not found. As a result, logs would be deleted after the configured retention period, and would not be backed up.",
          "references": [
            "https://cloud.google.com/logging",
            "https://cloud.google.com/logging/docs/export"
          ],
          "remediation": null,
          "service": "Stackdriver Logging"
        }
      },
      "metrics_count": 0,
      "projects": {
        "gcp-project-id": {
          "metrics": {},
          "metrics_count": 0,
          "sinks": {
            "_Default": {
              "destination": "logging.googleapis.com/projects/gcp-project-id/locations/global/buckets/_Default",
              "filter": "NOT LOG_ID(\"cloudaudit.googleapis.com/activity\") AND NOT LOG_ID(\"externalaudit.googleapis.com/activity\") AND NOT LOG_ID(\"cloudaudit.googleapis.com/system_event\") AND NOT LOG_ID(\"externalaudit.googleapis.com/system_event\") AND NOT LOG_ID(\"cloudaudit.googleapis.com/access_transparency\") AND NOT LOG_ID(\"externalaudit.googleapis.com/access_transparency\")",
              "name": "_Default"
            },
            "_Required": {
              "destination": "logging.googleapis.com/projects/gcp-project-id/locations/global/buckets/_Required",
              "filter": "LOG_ID(\"cloudaudit.googleapis.com/activity\") OR LOG_ID(\"externalaudit.googleapis.com/activity\") OR LOG_ID(\"cloudaudit.googleapis.com/system_event\") OR LOG_ID(\"externalaudit.googleapis.com/system_event\") OR LOG_ID(\"cloudaudit.googleapis.com/access_transparency\") OR LOG_ID(\"externalaudit.googleapis.com/access_transparency\")",
              "name": "_Required"
            }
          },
          "sinks_count": 2
        }
      },
      "sinks_count": 2
    },
    "stackdrivermonitoring": {
      "alert_policies_count": 0,
      "filters": {},
      "findings": {},
      "projects": {
        "gcp-project-id": {
          "alert_policies": {},
          "alert_policies_count": 0,
          "uptime_checks": {},
          "uptime_checks_count": 0
        }
      },
      "uptime_checks_count": 0
    }
  }
}