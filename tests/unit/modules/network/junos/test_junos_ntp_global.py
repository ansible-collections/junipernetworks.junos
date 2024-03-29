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

from unittest.mock import patch

from ansible_collections.junipernetworks.junos.plugins.modules import junos_ntp_global
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import set_module_args

from .junos_module import TestJunosModule, load_fixture


class TestJunosNtp_globalModule(TestJunosModule):
    module = junos_ntp_global

    def setUp(self):
        super(TestJunosNtp_globalModule, self).setUp()

        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration",
        )
        self.lock_configuration = self.mock_lock_configuration.start()

        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration",
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()

        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ntp_global.ntp_global.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ntp_global.ntp_global.commit_configuration",
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.ntp_global.ntp_global."
            "Ntp_globalFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestJunosNtp_globalModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(
        self,
        commands=None,
        format="text",
        changed=False,
        filename=None,
    ):
        def load_from_file(*args, **kwargs):
            output = load_fixture("junos_ntp_global_config.cfg")
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_junos_ntp_global_merged_01(self):
        set_module_args(
            dict(
                config=dict(
                    boot_server="78.46.194.186",
                    broadcasts=[
                        dict(
                            address="172.16.255.255",
                            key="50",
                            ttl=200,
                            version=3,
                            routing_instance_name="rt1",
                        ),
                        dict(
                            address="192.16.255.255",
                            key="50",
                            ttl=200,
                            version=3,
                            routing_instance_name="rt1",
                        ),
                    ],
                    broadcast_client=True,
                    interval_range=2,
                    multicast_client="224.0.0.1",
                    peers=[
                        dict(peer="78.44.194.186"),
                        dict(
                            peer="172.44.194.186",
                            key_id="10000",
                            prefer=True,
                            version=3,
                        ),
                    ],
                    servers=[
                        dict(
                            server="48.46.194.186",
                            key_id=34,
                            prefer=True,
                            version=2,
                            routing_instance="rt1",
                        ),
                        dict(
                            server="48.45.194.186",
                            key_id=34,
                            prefer=True,
                            version=2,
                        ),
                    ],
                    source_addresses=[
                        dict(
                            source_address="172.45.194.186",
                            routing_instance="rt1",
                        ),
                        dict(
                            source_address="171.45.194.186",
                            routing_instance="rt2",
                        ),
                    ],
                    threshold=dict(action="accept", value=300),
                    trusted_keys=[dict(key_id=3000), dict(key_id=2000)],
                ),
                state="merged",
            ),
        )
        result = self.execute_module(changed=True)
        self.assertIn(
            "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:broadcast><nc:name>172.16.255.255</nc:name><nc:key>50</nc:key>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:routing-instance-name>rt1</nc:routing-instance-name><nc:ttl>200</nc:ttl>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:version>3</nc:version></nc:broadcast><nc:broadcast>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:name>192.16.255.255</nc:name><nc:key>50</nc:key>",
            str(result["commands"]),
        )

    def test_junos_ntp_global_merged_02(self):
        set_module_args(
            dict(
                config=dict(
                    boot_server="78.46.194.186",
                    authentication_keys=[
                        dict(id="2", algorithm="md5", key="asdfghd"),
                        dict(id="5", algorithm="sha1", key="aasdad"),
                    ],
                ),
                state="merged",
            ),
        )
        result = self.execute_module(changed=True)
        self.assertIn(
            "<nc:ntp><nc:authentication-key><nc:name>2</nc:name><nc:type>md5</nc:type><nc:value>asdfghd</nc:value></nc:authentication-key>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:authentication-key><nc:name>5</nc:name><nc:type>sha1</nc:type><nc:value>aasdad</nc:value>",
            str(result["commands"]),
        )

    def test_junos_ntp_global_parsed_01(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                    <system>
        <ntp>
            <boot-server>78.46.194.186</boot-server>
            <interval-range>
                <value>2</value>
            </interval-range>
            <peer>
                <name>78.44.194.186</name>
            </peer>
            <peer>
                <name>172.44.194.186</name>
                <key>10000</key>
                <version>3</version>
                <prefer/>
            </peer>
            <server>
                <name>48.46.194.186</name>
                <key>34</key>
                <version>2</version>
                <prefer/>
                <routing-instance>rt1</routing-instance>
            </server>
            <server>
                <name>48.45.194.186</name>
                <key>34</key>
                <version>2</version>
                <prefer/>
            </server>
            <broadcast>
                <name>172.16.255.255</name>
                <routing-instance-name>rt1</routing-instance-name>
                <key>50</key>
                <version>3</version>
                <ttl>200</ttl>
            </broadcast>
            <broadcast>
                <name>192.16.255.255</name>
                <routing-instance-name>rt2</routing-instance-name>
                <key>50</key>
                <version>3</version>
                <ttl>200</ttl>
            </broadcast>
            <broadcast-client/>
            <multicast-client>
                <address>224.0.0.1</address>
            </multicast-client>
            <trusted-key>3000</trusted-key>
            <trusted-key>2000</trusted-key>
            <threshold>
                <value>300</value>
                <action>accept</action>
            </threshold>
            <source-address>
                <name>172.45.194.186</name>
                <routing-instance>rt1</routing-instance>
            </source-address>
            <source-address>
                <name>171.45.194.186</name>
                <routing-instance>rt2</routing-instance>
            </source-address>
        </ntp>
    </system>
    <interfaces xmlns="http://yang.juniper.net/junos-es/conf/interfaces">
        <interface>
            <name>fxp0</name>
            <unit>
                <name>0</name>
                <family>
                    <inet>
                        <dhcp>
                        </dhcp>
                    </inet>
                </family>
            </unit>
        </interface>
    </interfaces>
    <routing-instances xmlns="http://yang.juniper.net/junos-es/conf/routing-instances">
        <instance>
            <name>rt1</name>
            <description>rt1</description>
        </instance>
        <instance>
            <name>rt2</name>
            <description>rt2</description>
        </instance>
    </routing-instances>
                </configuration>
            </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_dict = {
            "boot_server": "78.46.194.186",
            "broadcast_client": True,
            "broadcasts": [
                {
                    "address": "172.16.255.255",
                    "key": "50",
                    "routing_instance_name": "rt1",
                    "ttl": 200,
                    "version": 3,
                },
                {
                    "address": "192.16.255.255",
                    "key": "50",
                    "routing_instance_name": "rt2",
                    "ttl": 200,
                    "version": 3,
                },
            ],
            "interval_range": 2,
            "multicast_client": "224.0.0.1",
            "peers": [
                {"peer": "78.44.194.186"},
                {
                    "key_id": 10000,
                    "peer": "172.44.194.186",
                    "prefer": True,
                    "version": 3,
                },
            ],
            "servers": [
                {
                    "key_id": 34,
                    "prefer": True,
                    "routing_instance": "rt1",
                    "server": "48.46.194.186",
                    "version": 2,
                },
                {
                    "key_id": 34,
                    "prefer": True,
                    "server": "48.45.194.186",
                    "version": 2,
                },
            ],
            "source_addresses": [
                {
                    "routing_instance": "rt1",
                    "source_address": "172.45.194.186",
                },
                {
                    "routing_instance": "rt2",
                    "source_address": "171.45.194.186",
                },
            ],
            "threshold": {"action": "accept", "value": 300},
            "trusted_keys": [{"key_id": 2000}, {"key_id": 3000}],
        }
        self.assertEqual(sorted(parsed_dict), sorted(result["parsed"]))

    def test_junos_ntp_global_parsed_02(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                    <system>
                        <ntp>
                            <boot-server>78.46.194.186</boot-server>
                            <interval-range>
                                <value>2</value>
                            </interval-range>
                            <peer>
                                <name>172.44.194.186</name>
                                <key>10000</key>
                                <version>3</version>
                                <prefer/>
                            </peer>
                            <server>
                                <name>48.45.194.186</name>
                                <key>34</key>
                                <version>2</version>
                                <prefer/>
                            </server>
                            <broadcast>
                                <name>192.16.255.255</name>
                                <routing-instance-name>rt2</routing-instance-name>
                                <key>50</key>
                                <version>3</version>
                                <ttl>200</ttl>
                            </broadcast>
                            <broadcast-client/>
                            <multicast-client>
                                <address>224.0.0.1</address>
                            </multicast-client>
                            <trusted-key>2000</trusted-key>
                            <threshold>
                                <value>300</value>
                                <action>accept</action>
                            </threshold>
                            <source-address>
                                <name>171.45.194.186</name>
                                <routing-instance>rt2</routing-instance>
                            </source-address>
                        </ntp>
                    </system>
                    <routing-instances xmlns="http://yang.juniper.net/junos-es/conf/routing-instances">
                        <instance>
                            <name>rt1</name>
                            <description>rt1</description>
                        </instance>
                        <instance>
                            <name>rt2</name>
                            <description>rt2</description>
                        </instance>
                    </routing-instances>
                </configuration>
            </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_dict = {
            "boot_server": "78.46.194.186",
            "broadcast_client": True,
            "broadcasts": [
                {
                    "address": "192.16.255.255",
                    "key": "50",
                    "routing_instance_name": "rt2",
                    "ttl": 200,
                    "version": 3,
                },
            ],
            "interval_range": 2,
            "multicast_client": "224.0.0.1",
            "peers": [
                {
                    "key_id": 10000,
                    "peer": "172.44.194.186",
                    "prefer": True,
                    "version": 3,
                },
            ],
            "servers": [
                {
                    "key_id": 34,
                    "prefer": True,
                    "server": "48.45.194.186",
                    "version": 2,
                },
            ],
            "source_addresses": [
                {"routing_instance": "rt2", "source_address": "171.45.194.186"},
            ],
            "threshold": {"action": "accept", "value": 300},
            "trusted_keys": [{"key_id": 2000}],
        }
        self.assertEqual(sorted(parsed_dict), sorted(result["parsed"]))

    def test_junos_ntp_global_parsed_03(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                    <system>
                        <ntp>
                            <authentication-key>
                                <name>2</name>
                                <type>md5</type>
                                <value>$9$GxDjqfT3CA0UjfzF6u0RhS</value>
                            </authentication-key>
                            <authentication-key>
                                <name>5</name>
                                <type>sha1</type>
                                <value>$9$ZsUDk.mT3/toJGiHqQz</value>
                            </authentication-key>
                        </ntp>
                    </system>
                    <routing-instances xmlns="http://yang.juniper.net/junos-es/conf/routing-instances">
                        <instance>
                            <name>rt1</name>
                            <description>rt1</description>
                        </instance>
                        <instance>
                            <name>rt2</name>
                            <description>rt2</description>
                        </instance>
                    </routing-instances>
                </configuration>
            </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_dict = {
            "authentication_keys": [
                {
                    "algorithm": "md5",
                    "id": 2,
                    "key": "$9$GxDjqfT3CA0UjfzF6u0RhS",
                },
                {
                    "algorithm": "sha1",
                    "id": 5,
                    "key": "$9$ZsUDk.mT3/toJGiHqQz",
                },
            ],
        }
        self.assertEqual(sorted(parsed_dict), sorted(result["parsed"]))

    def test_junos_ntp_global_overridden_01(self):
        set_module_args(
            dict(
                config=dict(
                    boot_server="78.46.194.186",
                    broadcasts=[
                        dict(
                            address="172.16.255.255",
                            key="50",
                            ttl=200,
                            version=3,
                            routing_instance_name="rt1",
                        ),
                        dict(
                            address="192.16.255.255",
                            key="50",
                            ttl=200,
                            version=3,
                            routing_instance_name="rt1",
                        ),
                    ],
                    broadcast_client=True,
                    interval_range=2,
                    multicast_client="224.0.0.1",
                    peers=[
                        dict(peer="78.44.194.186"),
                        dict(
                            peer="172.44.194.186",
                            key_id="10000",
                            prefer=True,
                            version=3,
                        ),
                    ],
                    servers=[
                        dict(
                            server="48.46.194.186",
                            key_id=34,
                            prefer=True,
                            version=2,
                            routing_instance="rt1",
                        ),
                        dict(
                            server="48.45.194.186",
                            key_id=34,
                            prefer=True,
                            version=2,
                        ),
                    ],
                    source_addresses=[
                        dict(
                            source_address="172.45.194.186",
                            routing_instance="rt1",
                        ),
                        dict(
                            source_address="171.45.194.186",
                            routing_instance="rt2",
                        ),
                    ],
                    threshold=dict(action="accept", value=300),
                    trusted_keys=[dict(key_id=3000), dict(key_id=2000)],
                ),
                state="overridden",
            ),
        )
        result = self.execute_module(changed=True)
        self.assertIn(
            "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:broadcast><nc:name>172.16.255.255</nc:name><nc:key>50</nc:key>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:routing-instance-name>rt1</nc:routing-instance-name><nc:ttl>200</nc:ttl>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:version>3</nc:version></nc:broadcast><nc:broadcast>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:name>192.16.255.255</nc:name><nc:key>50</nc:key>",
            str(result["commands"]),
        )

    def test_junos_ntp_global_gathered(self):
        """
        :return:
        """
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gather_list = {
            "authentication_keys": [
                {
                    "algorithm": "md5",
                    "id": 3,
                    "key": "$9$GxDjqfT3CA0UjfzF6u0RhS",
                },
                {
                    "algorithm": "sha1",
                    "id": 4,
                    "key": "$9$ZsUDk.mT3/toJGiHqQz",
                },
            ],
        }
        self.assertEqual(sorted(gather_list), sorted(result["gathered"]))

    def test_junos_ntp_global_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    boot_server="78.46.194.186",
                    authentication_keys=[
                        dict(id="2", algorithm="md5", key="asdfghd"),
                        dict(id="5", algorithm="sha1", key="aasdad"),
                    ],
                ),
                state="rendered",
            ),
        )
        rendered = (
            '<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:ntp><nc:authentication-key><nc:name>2</nc:name><nc:type>md5</nc:type>"
            "<nc:value>asdfghd</nc:value></nc:authentication-key><nc:authentication-key>"
            "<nc:name>5</nc:name><nc:type>sha1</nc:type><nc:value>aasdad</nc:value>"
            "</nc:authentication-key><nc:boot-server>78.46.194.186</nc:boot-server></nc:ntp></nc:system>"
        )
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(rendered))

    def test_junos_ntp_global_replaced_01(self):
        set_module_args(
            dict(
                config=dict(
                    boot_server="78.46.194.186",
                    broadcasts=[
                        dict(
                            address="172.16.255.255",
                            key="50",
                            ttl=200,
                            version=3,
                            routing_instance_name="rt1",
                        ),
                        dict(
                            address="192.16.255.255",
                            key="50",
                            ttl=200,
                            version=3,
                            routing_instance_name="rt1",
                        ),
                    ],
                    broadcast_client=True,
                    interval_range=2,
                    multicast_client="224.0.0.1",
                    peers=[
                        dict(peer="78.44.194.186"),
                        dict(
                            peer="172.44.194.186",
                            key_id="10000",
                            prefer=True,
                            version=3,
                        ),
                    ],
                    servers=[
                        dict(
                            server="48.46.194.186",
                            key_id=34,
                            prefer=True,
                            version=2,
                            routing_instance="rt1",
                        ),
                        dict(
                            server="48.45.194.186",
                            key_id=34,
                            prefer=True,
                            version=2,
                        ),
                    ],
                    source_addresses=[
                        dict(
                            source_address="172.45.194.186",
                            routing_instance="rt1",
                        ),
                        dict(
                            source_address="171.45.194.186",
                            routing_instance="rt2",
                        ),
                    ],
                    threshold=dict(action="accept", value=300),
                    trusted_keys=[dict(key_id=3000), dict(key_id=2000)],
                ),
                state="replaced",
            ),
        )
        result = self.execute_module(changed=True)
        self.assertIn(
            "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:broadcast><nc:name>172.16.255.255</nc:name><nc:key>50</nc:key>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:routing-instance-name>rt1</nc:routing-instance-name><nc:ttl>200</nc:ttl>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:version>3</nc:version></nc:broadcast><nc:broadcast>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:name>192.16.255.255</nc:name><nc:key>50</nc:key>",
            str(result["commands"]),
        )
