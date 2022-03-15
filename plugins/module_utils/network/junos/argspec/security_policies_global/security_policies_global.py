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

"""
The arg spec for the junos_security_policies_global module
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type


class Security_policies_globalArgs(object):  # pylint: disable=R0903
    """The arg spec for the junos_security_policies_global module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "options": {
                "default_policy": {
                    "choices": ["deny-all", "permit-all"],
                    "type": "str",
                },
                "policy_rematch": {
                    "options": {
                        "enable": {"type": "bool"},
                        "extensive": {"type": "bool"},
                    },
                    "type": "dict",
                },
                "policy_stats": {
                    "options": {
                        "enable": {"type": "bool"},
                        "system_wide": {"type": "bool"},
                    },
                    "type": "dict",
                },
                "pre_id_default_policy_action": {
                    "options": {
                        "log": {
                            "options": {
                                "session_close": {"type": "bool"},
                                "session_init": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "session_timeout": {
                            "options": {
                                "icmp": {"type": "int"},
                                "icmp6": {"type": "int"},
                                "ospf": {"type": "int"},
                                "others": {"type": "int"},
                                "tcp": {"type": "int"},
                                "udp": {"type": "int"},
                            },
                            "type": "dict",
                        },
                    },
                    "type": "dict",
                },
                "traceoptions": {
                    "options": {
                        "file": {
                            "options": {
                                "files": {"type": "int"},
                                "match": {"type": "str"},
                                "no_world_readable": {"type": "bool"},
                                "size": {"type": "str"},
                                "world_readable": {"type": "bool"},
                            },
                            "required": True,
                            "type": "dict",
                        },
                        "flag": {
                            "choices": [
                                "all",
                                "configuration",
                                "compilation",
                                "ipc",
                                "lookup",
                                "routing-socket",
                                "rules",
                            ],
                            "type": "str",
                        },
                        "no_remote_trace": {"type": "bool"},
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
