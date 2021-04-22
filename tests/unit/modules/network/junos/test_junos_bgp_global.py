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

import q
from ansible_collections.junipernetworks.junos.tests.unit.compat.mock import (
    patch,
    MagicMock,
)
from ansible_collections.junipernetworks.junos.plugins.modules import (
    junos_bgp_global,
)
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import (
    set_module_args,
)
from .junos_module import TestJunosModule, load_fixture


class TestJunosBgp_globalModule(TestJunosModule):
    module = junos_bgp_global

    def setUp(self):
        super(TestJunosBgp_globalModule, self).setUp()

        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration"
        )
        self.lock_configuration = self.mock_lock_configuration.start()

        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration"
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()

        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.bgp_global.bgp_global.load_config"
        )
        self.load_config = self.mock_load_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.bgp_global.bgp_global.commit_configuration"
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.bgp_global.bgp_global."
            "Bgp_globalFacts.get_device_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestJunosBgp_globalModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, format="text", changed=False):
        def load_from_file(*args, **kwargs):
            output = load_fixture("junos_bgp_global_config.cfg")
            q(output)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_junos_bgp_global_merged(self):
        set_module_args(
            dict(
                config=dict(
                    damping=True,
                    description="This is configured with Junos_bgp resource module",
                    preference="2",
                    bfd_liveness_detection=dict(
                        minimum_receive_interval=4,
                        multiplier=10,
                        no_adaptation=True,
                        version="automatic",
                    ),
                ),
                state="merged",
            )
        )
        commands = [
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:bgp><nc:damping/><nc:description>This is configured with Junos_bgp resource module</nc:description>"
            "<nc:preference>2</nc:preference><nc:bfd-liveness-detection>"
            "<nc:minimum-receive-interval>4</nc:minimum-receive-interval>"
            "<nc:multiplier>10</nc:multiplier>"
            "<nc:no-adaptation/><nc:version>automatic</nc:version></nc:bfd-liveness-detection></nc:bgp></nc:protocols>",
            '<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"/>',
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_bgp_global_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    accept_remote_nexthop=True,
                    advertise_from_main_vpn_tables=True,
                    advertise_inactive=True,
                    as_number="65432",
                    authentication_algorithm="md5",
                    bgp_error_tolerance=dict(
                        malformed_route_limit=30000000
                    ),
                    damping=True,
                    description="This is configured with Junos_bgp resource module",
                    hold_time=5,
                    holddown_all_stale_labels=True,
                    log_updown=True,
                    no_advertise_peer_as=True,
                    no_aggregator_id=True,
                    out_delay=10,
                    preference="2",
                ),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_bgp_global_replaced(self):
        """

        :return:
        """
        set_module_args(
            dict(
                config=dict(
                    accept_remote_nexthop=True,
                    advertise_from_main_vpn_tables=True,
                    advertise_inactive=True,
                    as_number="65432",
                    authentication_algorithm="md5",
                    bgp_error_tolerance=dict(
                        malformed_route_limit=20000000
                    ),
                    damping=True,
                    description="This is configured with Junos_bgp resource module",
                    groups=[
                        dict(name="internal",
                             out_delay=22
                             ),
                        dict(name="external",
                             out_delay=20)
                    ],
                    hold_time=4,
                    holddown_all_stale_labels=True,
                    log_updown=True,
                    keep="all",
                    mtu_discovery=True,
                    no_precision_timers=True,
                    no_advertise_peer_as=True,
                    no_aggregator_id=True,
                    out_delay=10,
                    preference="2",
                ),
                state="replaced",
            )
        )

        commands = [
            '<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">'
            '<nc:bgp><nc:accept-remote-nexthop delete=\"delete\"/>'
            '<nc:add-path-display-ipv4-address delete=\"delete\"/>'
            '<nc:advertise-bgp-static delete=\"delete\"/>'
            '<nc:advertise-external delete=\"delete\"/>'
            '<nc:advertise-from-main-vpn-tables delete=\"delete\"/>'
            '<nc:advertise-inactive delete=\"delete\"/>'
            '<nc:advertise-peer-as delete=\"delete\"/>'
            '<nc:authentication-algorithm delete=\"delete\"/>'
            '<nc:authentication-key delete=\"delete\"/>'
            '<nc:authentication-key-chain delete=\"delete\"/>'
            '<nc:bfd-liveness-detection delete=\"delete\"/>'
            '<nc:bgp-error-tolerance delete=\"delete\"/><nc:bmp delete=\"delete\"/>'
            '<nc:group delete=\"delete\"/><nc:cluster delete=\"delete\"/>'
            '<nc:damping delete=\"delete\"/><nc:description delete=\"delete\"/>'
            '<nc:disable delete=\"delete\"/><nc:egress-te-sid-stats delete=\"delete\"/>'
            '<nc:enforce-first-as delete=\"delete\"/><nc:export delete=\"delete\"/>'
            '<nc:forwarding-context delete=\"delete\"/><nc:hold-time delete=\"delete\"/>'
            '<nc:holddown-all-stale-labels delete=\"delete\"/><nc:import delete=\"delete\"/>'
            '<nc:include-mp-next-hop delete=\"delete\"/><nc:ipsec-sa delete=\"delete\"/>'
            '<nc:keep delete=\"delete\"/><nc:local-address delete=\"delete\"/>'
            '<nc:local-interface delete=\"delete\"/><nc:local-preference delete=\"delete\"/>'
            '<nc:log-updown delete=\"delete\"/><nc:mtu-discovery delete=\"delete\"/>'
            '<nc:no-advertise-peer-as delete=\"delete\"/><nc:no-aggregator-id delete=\"delete\"/>'
            '<nc:no-client-reflect delete=\"delete\"/><nc:no-precision-timers delete=\"delete\"/>'
            '<nc:passive delete=\"delete\"/><nc:peer-as delete=\"delete\"/>'
            '<nc:precision-timers delete=\"delete\"/><nc:preference delete=\"delete\"/>'
            '<nc:out-delay delete=\"delete\"/><nc:rfc6514-compliant-safi129 delete=\"delete\"/>'
            '<nc:route-server-client delete=\"delete\"/><nc:send-addpath-optimization delete=\"delete\"/>'
            '<nc:sr-preference-override delete=\"delete\"/>'
            '<nc:stale-labels-holddown-period delete=\"delete\"/><nc:tcp-aggressive-transmission delete=\"delete\"/>'
            '<nc:tcp-mss delete=\"delete\"/><nc:ttl delete=\"delete\"/>'
            '<nc:unconfigured-peer-graceful-restart delete=\"delete\"/>'
            '<nc:vpn-apply-export delete=\"delete\"/></nc:bgp><nc:bgp>'
            '<nc:accept-remote-nexthop/><nc:advertise-from-main-vpn-tables/>'
            '<nc:advertise-inactive/><nc:damping/><nc:holddown-all-stale-labels/>'
            '<nc:log-updown/><nc:mtu-discovery/><nc:no-advertise-peer-as/>'
            '<nc:no-aggregator-id/><nc:no-precision-timers/>'
            '<nc:authentication-algorithm>md5</nc:authentication-algorithm>'
            '<nc:description>This is configured with Junos_bgp resource module</nc:description>'
            '<nc:hold-time>4</nc:hold-time><nc:keep>all</nc:keep><nc:preference>2</nc:preference>'
            '<nc:out-delay>10</nc:out-delay><nc:bgp-error-tolerance>'
            '<nc:malformed-route-limit>20000000</nc:malformed-route-limit>'
            '</nc:bgp-error-tolerance><nc:group><nc:name>internal</nc:name>'
            '<nc:out-delay>22</nc:out-delay></nc:group><nc:group><nc:name>external</nc:name>'
            '<nc:out-delay>20</nc:out-delay></nc:group></nc:bgp></nc:protocols>',
            '<nc:routing-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">'
            '<nc:autonomous-system delete=\"delete\"/>'
            '<nc:autonomous-system>65432</nc:autonomous-system></nc:routing-options>'
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_bgp_global_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    accept_remote_nexthop=True,
                    advertise_from_main_vpn_tables=True,
                    advertise_inactive=True,
                    as_number="65432",
                    authentication_algorithm="md5",
                    bgp_error_tolerance=dict(
                        malformed_route_limit=30000000
                    ),
                    damping=True,
                    description="This is configured with Junos_bgp resource module",
                    hold_time=5,
                    holddown_all_stale_labels=True,
                    log_updown=True,
                    no_advertise_peer_as=True,
                    no_aggregator_id=True,
                    out_delay=10,
                    preference="2",
                ),
                state="replaced",
            )
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_bgp_global_rendered(self):
        """

        :return:
        """
        set_module_args(
            dict(
                config=dict(
                    description="This is configured with Junos_bgp resource module",
                    groups=[
                        dict(name="internal",
                             out_delay=22
                             ),
                    ],
                    hold_time=4,
                    holddown_all_stale_labels=True,
                    include_mp_next_hop=True,
                    log_updown=True,
                    loops=5,
                    keep="all",
                    mtu_discovery=True,
                    out_delay=10,
                    preference="2",
                ),
                state="rendered",
            )
        )

        rendered = "<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"><nc:bgp>" \
                   "<nc:holddown-all-stale-labels/><nc:include-mp-next-hop/><nc:log-updown/>" \
                   "<nc:mtu-discovery/>" \
                   "<nc:description>This is configured with Junos_bgp resource module</nc:description>" \
                   "<nc:hold-time>4</nc:hold-time><nc:keep>all</nc:keep><nc:preference>2</nc:preference>" \
                   "<nc:out-delay>10</nc:out-delay><nc:group>" \
                   "<nc:name>internal</nc:name><nc:out-delay>22</nc:out-delay>" \
                   "</nc:group></nc:bgp></nc:protocols>"
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(rendered))

    def test_junos_bgp_global_gathered(self):
        """

        :return:
        """
        set_module_args(
            dict(
                state="gathered",
            )
        )
        result = self.execute_module(changed=False)
        gather_dict = {
            "accept_remote_nexthop": True,
            "advertise_from_main_vpn_tables": True,
            "advertise_inactive": True,
            "as_number": "65432",
            "authentication_algorithm": "md5",
            "bgp_error_tolerance": {
                "malformed_route_limit": "30000000",
            },
            "damping": True,
            "description": "This is configured with Junos_bgp resource module",
            "hold_time": "5",
            "holddown_all_stale_labels": True,
            "log_updown": True,
            "no_advertise_peer_as": True,
            "no_aggregator_id": True,
            "out_delay": "10",
            "preference": "2"
        }
        self.assertEqual(sorted(gather_dict), sorted(result["gathered"]))

    def test_junos_bgp_global_parsed(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                    <protocols>
                        <bgp>
                            <advertise-from-main-vpn-tables />
                            <holddown-all-stale-labels />
                            <description>This is configured with Junos_bgp resource module</description>
                            <accept-remote-nexthop />
                            <preference>2</preference>
                            <hold-time>5</hold-time>
                            <advertise-inactive />
                            <no-advertise-peer-as />
                            <no-aggregator-id />
                            <out-delay>10</out-delay>
                            <log-updown />
                            <damping />
                            <bgp-error-tolerance>
                            <malformed-route-limit>30000000</malformed-route-limit>
                            </bgp-error-tolerance>
                            <authentication-algorithm>md5</authentication-algorithm>
                        </bgp>
                    </protocols>
                    <routing-options>
                        <static>
                            <route>
                            <name>172.16.17.0/24</name>
                            <discard />
                            </route>
                        </static>
                        <router-id>10.200.16.75</router-id>
                        <autonomous-system>
                            <as-number>65432</as-number>
                        </autonomous-system>
                    </routing-options>
                </configuration>
            </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_dict = {
            "accept_remote_nexthop": "True",
            "advertise_from_main_vpn_tables": "True",
            "advertise_inactive": "True",
            "as_number": "65534",
            "authentication_algorithm": "md5",
            "bgp_error_tolerance": {
                "malformed_route_limit": "30000000",
            },
            "damping": "True",
            "description": "This is configured with Junos_bgp resource module",
            "hold_time": "5",
            "holddown_all_stale_labels": "True",
            "log_updown": "true",
            "no_advertise_peer_as": "true",
            "no_aggregator_id": "true",
            "out_delay": "10",
            "preference": "2"
        }
        self.assertEqual(sorted(parsed_dict), sorted(result["parsed"]))

    def test_junos_bgp_global_delete_all(self):
        set_module_args(dict(config=dict(), state="deleted"))

        commands = [
            '<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">'
            '<nc:bgp><nc:accept-remote-nexthop delete=\"delete\"/><nc:add-path-display-ipv4-address delete=\"delete\"/>'
            '<nc:advertise-bgp-static delete=\"delete\"/><nc:advertise-external delete=\"delete\"/>'
            '<nc:advertise-from-main-vpn-tables delete=\"delete\"/><nc:advertise-inactive delete=\"delete\"/>'
            '<nc:advertise-peer-as delete=\"delete\"/><nc:authentication-algorithm delete=\"delete\"/>'
            '<nc:authentication-key delete=\"delete\"/><nc:authentication-key-chain delete=\"delete\"/>'
            '<nc:bfd-liveness-detection delete=\"delete\"/><nc:bgp-error-tolerance delete=\"delete\"/>'
            '<nc:bmp delete=\"delete\"/><nc:group delete=\"delete\"/><nc:cluster delete=\"delete\"/>'
            '<nc:damping delete=\"delete\"/><nc:description delete=\"delete\"/><nc:disable delete=\"delete\"/>'
            '<nc:egress-te-sid-stats delete=\"delete\"/><nc:enforce-first-as delete=\"delete\"/>'
            '<nc:export delete=\"delete\"/><nc:forwarding-context delete=\"delete\"/>'
            '<nc:hold-time delete=\"delete\"/><nc:holddown-all-stale-labels delete=\"delete\"/>'
            '<nc:import delete=\"delete\"/><nc:include-mp-next-hop delete=\"delete\"/>'
            '<nc:ipsec-sa delete=\"delete\"/><nc:keep delete=\"delete\"/><nc:local-address delete=\"delete\"/>'
            '<nc:local-interface delete=\"delete\"/>'
            '<nc:local-preference delete=\"delete\"/><nc:log-updown delete=\"delete\"/>'
            '<nc:mtu-discovery delete=\"delete\"/><nc:no-advertise-peer-as delete=\"delete\"/>'
            '<nc:no-aggregator-id delete=\"delete\"/><nc:no-client-reflect delete=\"delete\"/>'
            '<nc:no-precision-timers delete=\"delete\"/><nc:passive delete=\"delete\"/>'
            '<nc:peer-as delete=\"delete\"/><nc:precision-timers delete=\"delete\"/>'
            '<nc:preference delete=\"delete\"/><nc:out-delay delete=\"delete\"/>'
            '<nc:rfc6514-compliant-safi129 delete=\"delete\"/><nc:route-server-client delete=\"delete\"/>'
            '<nc:send-addpath-optimization delete=\"delete\"/><nc:sr-preference-override delete=\"delete\"/>'
            '<nc:stale-labels-holddown-period delete=\"delete\"/><nc:tcp-aggressive-transmission delete=\"delete\"/>'
            '<nc:tcp-mss delete=\"delete\"/><nc:ttl delete=\"delete\"/>'
            '<nc:unconfigured-peer-graceful-restart delete=\"delete\"/>'
            "<nc:vpn-apply-export delete=\"delete\"/></nc:bgp></nc:protocols>",
            '"<nc:routing-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">'
            '<nc:autonomous-system delete=\"delete\"/></nc:routing-options>'
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
    '''

    def test_junos_bgp_global_delete_idempotent(self):
        set_module_args(dict(state="deleted"))
        self.execute_module(changed=False, commands=[])

    def test_junos_bgp_global_purged(self):
        self.get_connection.return_value = load_fixture(
            "junos_bgp_global_config.cfg"
        )
        src = load_fixture("junos_bgp_global.cfg", content="str")
        set_module_args(dict(src=src))
        set_module_args(dict(config=dict(), state="purged"))

        commands = [
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:bgp delete="delete"/></nc:protocols>',
            '<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"/>',
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), commands)

    def test_junos_bgp_global_purged_idempotent(self):
        set_module_args(dict(state="purged"))
        self.execute_module(changed=False, commands=[])

    def test_junos_bgp_global_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    damping=True,
                    description="This is configured with Junos_bgp resource module",
                    preference="2",
                    bfd_liveness_detection=dict(
                        minimum_receive_interval=4,
                        multiplier=10,
                        no_adaptation=True,
                        version="automatic",
                    ),
                ),
                state="merged",
            )
        )
        commands = [
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:bgp>'
            "<nc:damping/><nc:description>This is configured with Junos_bgp resource module</nc:description>"
            "<nc:preference>2</nc:preference><nc:bfd-liveness-detection>"
            "<nc:minimum-receive-interval>4</nc:minimum-receive-interval>"
            "<nc:multiplier>10</nc:multiplier><nc:no-adaptation/><nc:version>automatic</nc:version>"
            "</nc:bfd-liveness-detection>"
            "</nc:bgp></nc:protocols>"
        ]
        self.execute_module(changed=False, commands=commands)
'''
