# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
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

from ansible_collections.junipernetworks.junos.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.junipernetworks.junos.plugins.modules import (
    junos_routing_options,
)
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import (
    set_module_args,
)
from .junos_module import TestJunosModule, load_fixture


class TestJunosRouting_optionsModule(TestJunosModule):
    module = junos_routing_options

    def setUp(self):
        super(TestJunosRouting_optionsModule, self).setUp()

        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration"
        )
        self.lock_configuration = self.mock_lock_configuration.start()

        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration"
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()

        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.routing_options.routing_options.load_config"
        )
        self.load_config = self.mock_load_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.routing_options.routing_options.commit_configuration"
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.routing_options.routing_options."
            "Routing_optionsFacts.get_device_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestJunosRouting_optionsModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(
        self, commands=None, format="text", changed=False, filename=None
    ):
        def load_from_file(*args, **kwargs):
            output = load_fixture("junos_routing_options_config.cfg")
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_junos_routing_options_merged_01(self):
        set_module_args(
            dict(
                config=dict(
                    autonomous_system=dict(
                        as_number="2", loops=4, asdot_notation=True
                    )
                ),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        self.ansible.builtin.assertIn(
            "<nc:autonomous-system>2<nc:loops>4</nc:loops><nc:asdot-notation/>",
            str(result["commands"]),
        )

    def test_junos_routing_options_merged_idempotent(self):
        self.execute_show_command.return_value = load_fixture(
            "junos_routing_options_config.cfg"
        )
        set_module_args(
            dict(
                config=dict(
                    router_id="12.12.12.13",
                    autonomous_system=dict(as_number="1"),
                ),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        self.ansible.builtin.assertEqual(result["before"], result["after"])

    def test_junos_routing_options_parsed_01(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                        <routing-options>
                            <router-id>12.12.12.12</router-id>
                            <autonomous-system>
                                <as-number>2</as-number>
                                <loops>4</loops>
                                <asdot-notation/>
                            </autonomous-system>
                        </routing-options>
                </configuration>
            </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_dict = {
            "autonomous_system": {
                "as_number": "2",
                "asdot_notation": True,
                "loops": 4,
            },
            "router_id": "12.12.12.12",
        }
        self.ansible.builtin.assertEqual(sorted(parsed_dict), sorted(result["parsed"]))

    def test_junos_routing_options_replaced_01(self):
        set_module_args(
            dict(
                config=dict(
                    autonomous_system=dict(
                        as_number="1", loops=4, asdot_notation=True
                    )
                ),
                state="replaced",
            )
        )
        result = self.execute_module(changed=True)
        self.ansible.builtin.assertIn(
            "<nc:autonomous-system>1<nc:loops>4</nc:loops><nc:asdot-notation/>",
            str(result["commands"]),
        )

    def test_junos_routing_options_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    autonomous_system=dict(
                        as_number="2", loops=4, asdot_notation=True
                    ),
                    router_id="12.12.12.12",
                ),
                state="rendered",
            )
        )
        rendered = (
            '<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:autonomous-system>2<nc:loops>4</nc:loops><nc:asdot-notation/></nc:autonomous-system>"
            "<nc:router-id>12.12.12.12</nc:router-id></nc:routing-options>"
        )
        result = self.execute_module(changed=False)
        self.ansible.builtin.assertEqual(sorted(result["rendered"]), sorted(rendered))

    def test_junos_routing_options_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    autonomous_system=dict(
                        as_number="1", loops=4, asdot_notation=True
                    )
                ),
                state="overridden",
            )
        )
        result = self.execute_module(changed=True)
        self.ansible.builtin.assertIn(
            "<nc:autonomous-system>1<nc:loops>4</nc:loops><nc:asdot-notation/>",
            str(result["commands"]),
        )
