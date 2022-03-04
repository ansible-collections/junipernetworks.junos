#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The arg spec for the junos_security_policies module
"""


class Security_policiesArgs(object):  # pylint: disable=R0903
    """The arg spec for the junos_security_policies module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "options": {
                "from_zones": {
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "to_zones": {
                            "elements": "dict",
                            "options": {
                                "name": {"type": "str"},
                                "policies": {
                                    "elements": "dict",
                                    "options": {
                                        "description": {"type": "str"},
                                        "match": {
                                            "options": {
                                                "application": {
                                                    "options": {
                                                        "any": {"type": "bool"},
                                                        "names": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                    },
                                                    "type": "dict",
                                                },
                                                "destination_address": {
                                                    "options": {
                                                        "addresses": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                        "any": {"type": "bool"},
                                                        "any_ipv4": {"type": "bool"},
                                                        "any_ipv6": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                                "destination_address_excluded": {"type": "bool"},
                                                "dynamic_application": {
                                                    "options": {
                                                        "any": {"type": "bool"},
                                                        "names": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                        "none": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                                "from_zone": {
                                                    "options": {
                                                        "any": {"type": "bool"},
                                                        "junos_host": {"type": "bool"},
                                                        "names": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                    },
                                                    "type": "dict",
                                                },
                                                "source_address": {
                                                    "options": {
                                                        "addresses": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                        "any": {"type": "bool"},
                                                        "any_ipv4": {"type": "bool"},
                                                        "any_ipv6": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                                "source_address_excluded": {"type": "bool"},
                                                "source_end_user_profile": {"type": "str"},
                                                "source_identity": {
                                                    "options": {
                                                        "any": {"type": "bool"},
                                                        "authenticated_user": {"type": "bool"},
                                                        "names": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                        "unauthenticated_user": {"type": "bool"},
                                                        "unknown_user": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                                "to_zone": {
                                                    "options": {
                                                        "any": {"type": "bool"},
                                                        "junos_host": {"type": "bool"},
                                                        "names": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                    },
                                                    "type": "dict",
                                                },
                                                "url_category": {
                                                    "options": {
                                                        "any": {"type": "bool"},
                                                        "names": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                        "none": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                        "name": {"type": "str"},
                                        "scheduler_name": {"type": "str"},
                                        "then": {
                                            "options": {
                                                "count": {"type": "bool"},
                                                "deny": {"type": "bool"},
                                                "log": {
                                                    "choices": [
                                                        "session-close",
                                                        "session-init",
                                                    ],
                                                    "type": "str",
                                                },
                                                "permit": {
                                                    "options": {
                                                        "application_services": {
                                                            "options": {
                                                                "advanced_anti_malware_policy": {"type": "str"},
                                                                "application_firewalls": {
                                                                    "elements": "dict",
                                                                    "options": {"rule_set": {"type": "str"}},
                                                                    "type": "list",
                                                                },
                                                                "application_traffic_control_rule_set": {"type": "str"},
                                                                "gprs_gtp_profile": {"type": "str"},
                                                                "gprs_sctp_profile": {"type": "str"},
                                                                "icap_redirect": {"type": "str"},
                                                                "idp": {"type": "bool"},
                                                                "idp_policy": {"type": "str"},
                                                                "packet_capture": {"type": "bool"},
                                                                "redirect_wx": {"type": "bool"},
                                                                "reverse_redirect_wx": {"type": "bool"},
                                                                "security_intelligence": {
                                                                    "options": {
                                                                        "add_destination_identity_to_feed": {"type": "str"},
                                                                        "add_destination_ip_to_feed": {"type": "str"},
                                                                        "add_source_identity_to_feed": {"type": "str"},
                                                                        "add_source_ip_to_feed": {"type": "str"},
                                                                    },
                                                                    "type": "dict",
                                                                },
                                                                "security_intelligence_policy": {"type": "str"},
                                                                "ssl_proxy": {
                                                                    "options": {
                                                                        "enable": {"type": "bool"},
                                                                        "profile_name": {"type": "str"},
                                                                    },
                                                                    "type": "dict",
                                                                },
                                                                "uac_policy": {
                                                                    "options": {
                                                                        "captive_portal": {"type": "str"},
                                                                        "enable": {"type": "bool"},
                                                                    },
                                                                    "type": "dict",
                                                                },
                                                                "utm_policy": {"type": "str"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                        "destination_address": {
                                                            "choices": [
                                                                "drop-translated",
                                                                "drop-untranslated",
                                                            ],
                                                            "type": "str",
                                                        },
                                                        "firewall_authentication": {
                                                            "options": {
                                                                "pass_through": {
                                                                    "no_log": False,
                                                                    "options": {
                                                                        "access_profile": {"type": "str"},
                                                                        "auth_only_browser": {"type": "bool"},
                                                                        "auth_user_agent": {"type": "str"},
                                                                        "client_match": {"type": "str"},
                                                                        "ssl_termination_profile": {"type": "str"},
                                                                        "web_redirect": {"type": "bool"},
                                                                        "web_redirect_to_https": {"type": "bool"},
                                                                    },
                                                                    "type": "dict",
                                                                },
                                                                "push_to_identity_management": {"type": "bool"},
                                                                "user_firewall": {
                                                                    "options": {
                                                                        "access_profile": {"type": "str"},
                                                                        "auth_only_browser": {"type": "bool"},
                                                                        "auth_user_agent": {"type": "str"},
                                                                        "domain": {"type": "str"},
                                                                        "ssl_termination_profile": {"type": "str"},
                                                                        "web_redirect": {"type": "bool"},
                                                                        "web_redirect_to_https": {"type": "bool"},
                                                                    },
                                                                    "type": "dict",
                                                                },
                                                                "web_authentication": {
                                                                    "elements": "str",
                                                                    "type": "list",
                                                                },
                                                            },
                                                            "type": "dict",
                                                        },
                                                        "tcp_options": {
                                                            "options": {
                                                                "initial_tcp_mss": {"type": "int"},
                                                                "reverse_tcp_mss": {"type": "int"},
                                                                "sequence_check_required": {"type": "bool"},
                                                                "syn_check_required": {"type": "bool"},
                                                                "window_scale": {"type": "bool"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                        "tunnel": {
                                                            "options": {
                                                                "ipsec_vpn": {"type": "str"},
                                                                "pair_policy": {"type": "str"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                    },
                                                    "type": "dict",
                                                },
                                                "reject": {
                                                    "options": {
                                                        "enable": {"type": "bool"},
                                                        "profile": {"type": "str"},
                                                        "ssl_proxy": {
                                                            "options": {
                                                                "enable": {"type": "bool"},
                                                                "profile_name": {"type": "str"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "list",
                                },
                            },
                            "type": "list",
                        },
                    },
                    "type": "list",
                },
                "global": {
                    "options": {
                        "policies": {
                            "elements": "dict",
                            "options": {
                                "description": {"type": "str"},
                                "match": {
                                    "options": {
                                        "application": {
                                            "options": {
                                                "any": {"type": "bool"},
                                                "names": {
                                                    "elements": "str",
                                                    "type": "list",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                        "destination_address": {
                                            "options": {
                                                "addresses": {
                                                    "elements": "str",
                                                    "type": "list",
                                                },
                                                "any": {"type": "bool"},
                                                "any_ipv4": {"type": "bool"},
                                                "any_ipv6": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "destination_address_excluded": {"type": "bool"},
                                        "dynamic_application": {
                                            "options": {
                                                "any": {"type": "bool"},
                                                "names": {
                                                    "elements": "str",
                                                    "type": "list",
                                                },
                                                "none": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "from_zone": {
                                            "options": {
                                                "any": {"type": "bool"},
                                                "junos_host": {"type": "bool"},
                                                "names": {
                                                    "elements": "str",
                                                    "type": "list",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                        "source_address": {
                                            "options": {
                                                "addresses": {
                                                    "elements": "str",
                                                    "type": "list",
                                                },
                                                "any": {"type": "bool"},
                                                "any_ipv4": {"type": "bool"},
                                                "any_ipv6": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "source_address_excluded": {"type": "bool"},
                                        "source_end_user_profile": {"type": "str"},
                                        "source_identity": {
                                            "options": {
                                                "any": {"type": "bool"},
                                                "authenticated_user": {"type": "bool"},
                                                "names": {
                                                    "elements": "str",
                                                    "type": "list",
                                                },
                                                "unauthenticated_user": {"type": "bool"},
                                                "unknown_user": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "to_zone": {
                                            "options": {
                                                "any": {"type": "bool"},
                                                "junos_host": {"type": "bool"},
                                                "names": {
                                                    "elements": "str",
                                                    "type": "list",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                        "url_category": {
                                            "options": {
                                                "any": {"type": "bool"},
                                                "names": {
                                                    "elements": "str",
                                                    "type": "list",
                                                },
                                                "none": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "name": {"type": "str"},
                                "scheduler_name": {"type": "str"},
                                "then": {
                                    "options": {
                                        "count": {"type": "bool"},
                                        "deny": {"type": "bool"},
                                        "log": {
                                            "choices": [
                                                "session-close",
                                                "session-init",
                                            ],
                                            "type": "str",
                                        },
                                        "permit": {
                                            "options": {
                                                "application_services": {
                                                    "options": {
                                                        "advanced_anti_malware_policy": {"type": "str"},
                                                        "application_firewalls": {
                                                            "elements": "dict",
                                                            "options": {"rule_set": {"type": "str"}},
                                                            "type": "list",
                                                        },
                                                        "application_traffic_control_rule_set": {"type": "str"},
                                                        "gprs_gtp_profile": {"type": "str"},
                                                        "gprs_sctp_profile": {"type": "str"},
                                                        "icap_redirect": {"type": "str"},
                                                        "idp": {"type": "bool"},
                                                        "idp_policy": {"type": "str"},
                                                        "packet_capture": {"type": "bool"},
                                                        "redirect_wx": {"type": "bool"},
                                                        "reverse_redirect_wx": {"type": "bool"},
                                                        "security_intelligence": {
                                                            "options": {
                                                                "add_destination_identity_to_feed": {"type": "str"},
                                                                "add_destination_ip_to_feed": {"type": "str"},
                                                                "add_source_identity_to_feed": {"type": "str"},
                                                                "add_source_ip_to_feed": {"type": "str"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                        "security_intelligence_policy": {"type": "str"},
                                                        "ssl_proxy": {
                                                            "options": {
                                                                "enable": {"type": "bool"},
                                                                "profile_name": {"type": "str"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                        "uac_policy": {
                                                            "options": {
                                                                "captive_portal": {"type": "str"},
                                                                "enable": {"type": "bool"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                        "utm_policy": {"type": "str"},
                                                    },
                                                    "type": "dict",
                                                },
                                                "destination_address": {
                                                    "choices": [
                                                        "drop-translated",
                                                        "drop-untranslated",
                                                    ],
                                                    "type": "str",
                                                },
                                                "firewall_authentication": {
                                                    "options": {
                                                        "pass_through": {
                                                            "no_log": False,
                                                            "options": {
                                                                "access_profile": {"type": "str"},
                                                                "auth_only_browser": {"type": "bool"},
                                                                "auth_user_agent": {"type": "str"},
                                                                "client_match": {"type": "str"},
                                                                "ssl_termination_profile": {"type": "str"},
                                                                "web_redirect": {"type": "bool"},
                                                                "web_redirect_to_https": {"type": "bool"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                        "push_to_identity_management": {"type": "bool"},
                                                        "user_firewall": {
                                                            "options": {
                                                                "access_profile": {"type": "str"},
                                                                "auth_only_browser": {"type": "bool"},
                                                                "auth_user_agent": {"type": "str"},
                                                                "domain": {"type": "str"},
                                                                "ssl_termination_profile": {"type": "str"},
                                                                "web_redirect": {"type": "bool"},
                                                                "web_redirect_to_https": {"type": "bool"},
                                                            },
                                                            "type": "dict",
                                                        },
                                                        "web_authentication": {
                                                            "elements": "str",
                                                            "type": "list",
                                                        },
                                                    },
                                                    "type": "dict",
                                                },
                                                "tcp_options": {
                                                    "options": {
                                                        "initial_tcp_mss": {"type": "int"},
                                                        "reverse_tcp_mss": {"type": "int"},
                                                        "sequence_check_required": {"type": "bool"},
                                                        "syn_check_required": {"type": "bool"},
                                                        "window_scale": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                                "tunnel": {
                                                    "options": {
                                                        "ipsec_vpn": {"type": "str"},
                                                        "pair_policy": {"type": "str"},
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                        "reject": {
                                            "options": {
                                                "enable": {"type": "bool"},
                                                "profile": {"type": "str"},
                                                "ssl_proxy": {
                                                    "options": {
                                                        "enable": {"type": "bool"},
                                                        "profile_name": {"type": "str"},
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "list",
                        }
                    },
                    "type": "dict",
                },
            },
            "type": "dict",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "rendered",
                "gathered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
