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
    junos_snmp_server,
)
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import (
    set_module_args,
)
from .junos_module import TestJunosModule, load_fixture


class TestJunosSnmp_serverModule(TestJunosModule):
    module = junos_snmp_server

    def setUp(self):
        super(TestJunosSnmp_serverModule, self).setUp()

        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration"
        )
        self.lock_configuration = self.mock_lock_configuration.start()

        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration"
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()

        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.snmp_server.snmp_server.load_config"
        )
        self.load_config = self.mock_load_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.snmp_server.snmp_server.commit_configuration"
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.snmp_server.snmp_server."
            "Snmp_serverFacts.get_device_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestJunosSnmp_serverModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(
        self, commands=None, format="text", changed=False, filename=None
    ):
        def load_from_file(*args, **kwargs):
            output = load_fixture("junos_snmp_server_config.cfg")
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_junos_snmp_server_merged_arp_01(self):
        set_module_args(
            dict(
                config=dict(arp=dict(set=True, host_name_resolution=True)),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        self.assertIn(
            '<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">',
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:arp><nc:host-name-resolution/></nc:arp></nc:snmp>",
            str(result["commands"]),
        )

    def test_junos_snmp_server_merged_client_02(self):
        set_module_args(
            dict(
                config=dict(
                    client_lists=[
                        dict(
                            name="cl2",
                            addresses=[dict(address="192.16.4.0/24")],
                        )
                    ]
                ),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        self.assertIn(
            '<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">',
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:client-list><nc:name>cl2</nc:name><nc:client-address-list>",
            str(result["commands"]),
        )
        self.assertIn(
            "<nc:name>192.16.4.0/24</nc:name>", str(result["commands"])
        )
        self.assertIn(
            "</nc:client-address-list></nc:client-list></nc:snmp>",
            str(result["commands"]),
        )

    def test_junos_snmp_server_merged_clients_03(self):
        set_module_args(
            dict(
                config=dict(
                    client_lists=[
                        dict(
                            name="cl3",
                            addresses=[
                                dict(address="172.16.1.0/24"),
                                dict(address="10.11.11.11", restrict=True),
                            ],
                        ),
                        dict(
                            name="cl4",
                            addresses=[dict(address="172.16.4.0/24")],
                        ),
                    ]
                ),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            '<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">',
            "<nc:client-list><nc:name>cl3</nc:name>",
            "<nc:client-address-list><nc:name>172.16.1.0/24</nc:name>",
            "</nc:client-address-list><nc:client-address-list>",
            "<nc:name>10.11.11.11</nc:name><nc:restrict/></nc:client-address-list>",
            "</nc:client-list><nc:client-list><nc:name>cl4</nc:name>",
            "<nc:client-address-list><nc:name>172.16.4.0/24</nc:name>",
            "</nc:client-address-list></nc:client-list></nc:snmp>",
        ]
        for command in commands:
            self.assertIn(command, str(result["commands"]))

    def test_junos_snmp_server_merged_routing_access_04(self):
        set_module_args(
            dict(
                config=dict(
                    routing_instance_access=dict(
                        set=True, access_lists=["clv1"]
                    )
                ),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            '<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">',
            "<nc:routing-instance-access><nc:access-list><nc:name>clv1</nc:name>",
            "</nc:access-list></nc:routing-instance-access></nc:snmp>",
        ]
        for command in commands:
            self.assertIn(command, str(result["commands"]))

    def test_junos_snmp_server_merged_communities_05(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="comm1",
                            clients=[
                                dict(address="24.0.0.0/32", restrict=True)
                            ],
                            routing_instances=[
                                dict(
                                    name="clv1",
                                    clients=[
                                        dict(
                                            address="13.13.13.13/24",
                                            restrict=True,
                                        )
                                    ],
                                )
                            ],
                        )
                    ]
                ),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            '<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:community><nc:name>comm1</nc:name><nc:clients>",
            "<nc:name>24.0.0.0/32</nc:name><nc:restrict/></nc:clients>",
            "<nc:routing-instance><nc:name>clv1</nc:name><nc:clients>",
            "<nc:name>13.13.13.13/24</nc:name><nc:restrict/></nc:clients>",
            "</nc:routing-instance></nc:community></nc:snmp>",
        ]
        for command in commands:
            self.assertIn(command, str(result["commands"]))

    def test_junos_snmp_server_merged_06(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="comm1",
                            clients=[
                                dict(address="24.0.0.0/32", restrict=True),
                                dict(address="30.0.0.0/32", restrict=True),
                            ],
                            routing_instances=[
                                dict(
                                    name="clv1",
                                    clients=[
                                        dict(
                                            address="13.13.13.13/24",
                                            restrict=True,
                                        ),
                                        dict(address="24.0.0.0/32"),
                                        dict(address="30.0.0.0/32"),
                                    ],
                                ),
                                dict(
                                    name="clv2",
                                    clients=[dict(address="15.15.15.15/24")],
                                ),
                            ],
                        ),
                        dict(name="comm2"),
                    ],
                    contact="rohitthakur2590",
                    customization=dict(ether_stats_ifd_only=True),
                    description="Local SNMP Server",
                    engine_id=dict(
                        local="local1",
                        use_default_ip_address=True,
                        use_mac_address=True,
                    ),
                    filter_duplicates=True,
                    filter_interfaces=dict(
                        all_internal_interfaces=True,
                        interfaces=["eth1", "eth2"],
                    ),
                    health_monitor=dict(
                        falling_threshold=50,
                        idp=True,
                        interval=100,
                        rising_threshold=60,
                    ),
                    if_count_with_filter_interfaces=True,
                    interfaces=["eth1", "eth2", "eth3"],
                    location="inter_lab",
                    logical_system_trap_filter=True,
                    name="SNMP_LAB_SERVER",
                    nonvolatile=dict(commit_delay=30),
                    rmon=dict(
                        alarms=[
                            dict(
                                id=4,
                                variable="1.x.y.z",
                                sample_type="absolute-value",
                                rising_threshold=1020,
                            ),
                            dict(
                                id=5,
                                variable="1.x.y.z",
                                sample_type="absolute-value",
                                rising_threshold=1020,
                            ),
                        ],
                        events=[
                            dict(id=100, type="log"),
                            dict(id=200, type="log"),
                        ],
                    ),
                    routing_instance_access=dict(
                        access_lists=["clv1", "clv2"]
                    ),
                    subagent=dict(tcp=dict(routing_instances_default=True)),
                    snmp_v3=dict(
                        notify=[dict(name="not1", type="inform", tag="tag2")],
                        notify_filter=[
                            dict(
                                name="not_fil_01",
                                oids=[dict(include=True, oid="1.a.s.b.d")],
                            ),
                            dict(
                                name="not_fil_02",
                                oids=[
                                    dict(include=True, oid="1.x.b.b.d"),
                                    dict(include=True, oid="1.a.c.b.d"),
                                ],
                            ),
                        ],
                        snmp_community=[
                            dict(
                                community_index="v3_comm1",
                                community_name="mycommu",
                                security_name="sec101",
                                context="cont1",
                                tag="109",
                            ),
                            dict(
                                community_index="v3_comm2",
                                community_name="mycomm",
                                security_name="sec102",
                                context="cont1",
                                tag="109",
                            ),
                        ],
                        target_addresses=[
                            dict(
                                name="tar201",
                                address="162.12.10.2",
                                port=23122,
                                timeout=300,
                                retry_count=200,
                                tag_list="tag101",
                                address_mask="24",
                                routing_instance="clv2",
                                target_parameters="tarparam2",
                            ),
                            dict(
                                name="tar202",
                                address="162.12.10.2",
                                port=23122,
                                timeout=300,
                                retry_count=200,
                                tag_list="tag101",
                                address_mask="24",
                                routing_instance="clv2",
                                target_parameters="tarparam2",
                            ),
                        ],
                        target_parameters=[
                            dict(
                                name="param111",
                                notify_filter="not121",
                                parameters=dict(
                                    message_processing_model="v1",
                                    security_model="v1",
                                    security_level="none",
                                    security_name="secure111",
                                ),
                            )
                        ],
                    ),
                    traceoptions=dict(
                        file=dict(
                            files=20,
                            match="snmp_cfg",
                            no_world_readable=True,
                            size=20000,
                        ),
                        flag=dict(
                            all=True,
                            general=True,
                            interface_stats=True,
                            nonvolatile_sets=True,
                            pdu=True,
                            protocol_timeouts=True,
                            routing_socket=True,
                            subagent=True,
                            timer=True,
                            varbind_error=True,
                        ),
                        memory_trace=dict(size=1350),
                    ),
                    trap_groups=[
                        dict(
                            name="trgrp_01",
                            destination_port=2346,
                            categories=dict(
                                authentication=True,
                                chassis=True,
                                otn_alarms=dict(
                                    oc_lof=True, otu_uas_threshold=True
                                ),
                            ),
                            targets=["11.11.11.11", "12.12.12.12"],
                            routing_instance="clv1",
                        )
                    ],
                ),
                state="merged",
            )
        )
        result = self.execute_module(changed=True)
        commands = [
            '<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">',
            "<nc:routing-instance-access><nc:access-list><nc:name>clv1</nc:name>",
            "</nc:access-list><nc:access-list><nc:name>clv2</nc:name></nc:access-list>",
            "</nc:routing-instance-access><nc:community><nc:name>comm1</nc:name><nc:clients>",
            "<nc:name>24.0.0.0/32</nc:name><nc:restrict/></nc:clients><nc:clients><nc:name>30.0.0.0/32</nc:name>",
            "<nc:restrict/></nc:clients><nc:routing-instance><nc:name>clv1</nc:name><nc:clients>",
            "<nc:name>13.13.13.13/24</nc:name><nc:restrict/></nc:clients><nc:clients><nc:name>24.0.0.0/32</nc:name>",
            "</nc:clients><nc:clients><nc:name>30.0.0.0/32</nc:name></nc:clients></nc:routing-instance>",
            "<nc:routing-instance><nc:name>clv2</nc:name><nc:clients><nc:name>15.15.15.15/24</nc:name>",
            "</nc:clients></nc:routing-instance></nc:community><nc:community><nc:name>comm2</nc:name>",
            "</nc:community><nc:contact>rohitthakur2590</nc:contact><nc:customization><nc:ether-stats-ifd-only/>",
            "</nc:customization><nc:description>Local SNMP Server</nc:description><nc:engine-id>",
            "<nc:local>local1</nc:local><nc:use-default-ip-address/><nc:use-mac-address/></nc:engine-id>",
            "</nc:filter-interfaces><nc:health-monitor><nc:falling-threshold>50</nc:falling-threshold>",
            "<nc:rising-threshold>60</nc:rising-threshold><nc:interval>100</nc:interval><nc:idp/></nc:health-monitor>",
            "<nc:if-count-with-filter-interfaces/><nc:interface>eth1</nc:interface><nc:interface>eth2</nc:interface>",
            "<nc:interface>eth3</nc:interface><nc:location>inter_lab</nc:location><nc:logical-system-trap-filter/>",
            "<nc:system-name>SNMP_LAB_SERVER</nc:system-name><nc:nonvolatile><nc:commit-delay>30</nc:commit-delay>",
            "</nc:nonvolatile><nc:rmon><nc:alarm><nc:name>4</nc:name><nc:variable>1.x.y.z</nc:variable>",
            "<nc:sample-type>absolute-value</nc:sample-type><nc:rising-threshold>1020</nc:rising-threshold>",
            "</nc:alarm><nc:alarm><nc:name>5</nc:name><nc:variable>1.x.y.z</nc:variable>",
            "<nc:sample-type>absolute-value</nc:sample-type><nc:rising-threshold>1020</nc:rising-threshold></nc:alarm>",
            "<nc:event><nc:name>100</nc:name><nc:type>log</nc:type></nc:event><nc:event><nc:name>200</nc:name>",
            "<nc:type>log</nc:type></nc:event></nc:rmon><nc:subagent><nc:tcp><nc:routing-instance><nc:default/>",
            "</nc:routing-instance></nc:tcp></nc:subagent><nc:traceoptions><nc:file><nc:match>snmp_cfg</nc:match>",
            "<nc:files>20</nc:files><nc:no-world-readable/><nc:size>20000</nc:size></nc:file><nc:flag>",
            "<nc:name>all</nc:name></nc:flag><nc:flag><nc:name>general</nc:name></nc:flag><nc:flag>",
            "<nc:name>interface-stats</nc:name></nc:flag><nc:flag><nc:name>nonvolatile-sets</nc:name>",
            "</nc:flag><nc:flag><nc:name>pdu</nc:name></nc:flag><nc:flag><nc:name>protocol-timeouts</nc:name></nc:flag>",
            "<nc:flag><nc:name>routing-socket</nc:name></nc:flag><nc:flag><nc:name>subagent</nc:name>",
            "</nc:flag><nc:flag><nc:name>timer</nc:name></nc:flag><nc:flag><nc:name>varbind-error</nc:name>",
            "</nc:flag><nc:memory-trace><nc:size>1350</nc:size></nc:memory-trace></nc:traceoptions><nc:trap-group>",
            "<nc:name>trgrp_01</nc:name><nc:destination-port>2346</nc:destination-port><nc:categories>",
            "<nc:authentication/><nc:chassis/><nc:otn-alarms><nc:oc-lof/><nc:otu-uas-threshold/></nc:otn-alarms>",
            "</nc:categories><nc:targets><nc:name>11.11.11.11</nc:name></nc:targets><nc:targets>",
            "<nc:name>12.12.12.12</nc:name></nc:targets><nc:routing-instance>clv1</nc:routing-instance>",
            "</nc:trap-group><nc:v3><nc:notify><nc:name>not1</nc:name><nc:type>inform</nc:type><nc:tag>tag2</nc:tag>",
            "</nc:notify><nc:notify-filter><nc:name>not_fil_01</nc:name><nc:oid><nc:name>1.a.s.b.d</nc:name>",
            "<nc:include/></nc:oid></nc:notify-filter><nc:notify-filter><nc:name>not_fil_02</nc:name><nc:oid>",
            "<nc:name>1.x.b.b.d</nc:name><nc:include/></nc:oid><nc:oid><nc:name>1.a.c.b.d</nc:name><nc:include/>",
            "</nc:oid></nc:notify-filter><nc:snmp-community><nc:name>v3_comm1</nc:name>",
            "<nc:community-name>mycommu</nc:community-name><nc:security-name>sec101</nc:security-name>",
            "<nc:context>cont1</nc:context><nc:tag>109</nc:tag></nc:snmp-community><nc:snmp-community>",
            "<nc:name>v3_comm2</nc:name><nc:community-name>mycomm</nc:community-name>",
            "<nc:security-name>sec102</nc:security-name><nc:context>cont1</nc:context><nc:tag>109</nc:tag>",
            "</nc:snmp-community><nc:target-address><nc:name>tar201</nc:name><nc:address>162.12.10.2</nc:address>",
            "<nc:port>23122</nc:port><nc:timeout>300</nc:timeout><nc:retry-count>200</nc:retry-count>",
            "<nc:tag-list>tag101</nc:tag-list><nc:address-mask>24</nc:address-mask>",
            "<nc:routing-instance>clv2</nc:routing-instance><nc:target-parameters>tarparam2</nc:target-parameters>",
            "</nc:target-address><nc:target-address><nc:name>tar202</nc:name><nc:address>162.12.10.2</nc:address>",
            "<nc:port>23122</nc:port><nc:timeout>300</nc:timeout><nc:retry-count>200</nc:retry-count>",
            "<nc:tag-list>tag101</nc:tag-list><nc:address-mask>24</nc:address-mask>",
            "<nc:routing-instance>clv2</nc:routing-instance><nc:target-parameters>tarparam2</nc:target-parameters>",
            "</nc:target-address><nc:target-parameters><nc:name>param111</nc:name>",
            "<nc:notify-filter>not121</nc:notify-filter><nc:parameters>",
            "<nc:message-processing-model>v1</nc:message-processing-model><nc:security-model>v1</nc:security-model>",
            "<nc:security-level>none</nc:security-level><nc:security-name>secure111</nc:security-name></nc:parameters>",
            "</nc:target-parameters></nc:v3></nc:snmp>",
        ]
        for command in commands:
            self.assertIn(command, str(result["commands"]))

    def test_junos_snmp_server_parsed_07(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                    <snmp>
        <system-name>SNMP_LAB_SERVER</system-name>
        <description>Local SNMP Server</description>
        <location>inter_lab</location>
        <contact>rohitthakur2590</contact>
        <interface>eth1.0</interface>
        <interface>eth2.0</interface>
        <interface>eth3.0</interface>
        <filter-interfaces>
            <interfaces>
                <name>eth1</name>
            </interfaces>
            <interfaces>
                <name>eth2</name>
            </interfaces>
            <all-internal-interfaces/>
        </filter-interfaces>
        <if-count-with-filter-interfaces/>
        <filter-duplicates/>
        <nonvolatile>
            <commit-delay>30</commit-delay>
        </nonvolatile>
        <v3>
            <target-address>
                <name>tar201</name>
                <address>162.12.10.2</address>
                <port>23122</port>
                <timeout>300</timeout>
                <retry-count>200</retry-count>
                <tag-list>tag101</tag-list>
                <address-mask>24.0.0.0</address-mask>
                <routing-instance>clv2</routing-instance>
                <target-parameters>tarparam2</target-parameters>
            </target-address>
            <target-address>
                <name>tar202</name>
                <address>162.12.10.2</address>
                <port>23122</port>
                <timeout>300</timeout>
                <retry-count>200</retry-count>
                <tag-list>tag101</tag-list>
                <address-mask>24.0.0.0</address-mask>
                <routing-instance>clv2</routing-instance>
                <target-parameters>tarparam2</target-parameters>
            </target-address>
            <target-parameters>
                <name>param111</name>
                <parameters>
                    <message-processing-model>v1</message-processing-model>
                    <security-model>v1</security-model>
                    <security-level>none</security-level>
                    <security-name>secure111</security-name>
                </parameters>
                <notify-filter>
                    <filter>not121</filter>
                </notify-filter>
            </target-parameters>
            <notify>
                <name>not1</name>
                <type>inform</type>
                <tag>tag2</tag>
            </notify>
            <notify-filter>
                <name>not_fil_01</name>
                <oid>
                    <name>1.a.s.b.d</name>
                    <include/>
                </oid>
            </notify-filter>
            <notify-filter>
                <name>not_fil_02</name>
                <oid>
                    <name>1.x.b.b.d</name>
                    <include/>
                </oid>
                <oid>
                    <name>1.a.c.b.d</name>
                    <include/>
                </oid>
            </notify-filter>
            <snmp-community>
                <name>v3_comm1</name>
                <community-name>$9$gUoGiQF/tpB5QORhr8LjHq</community-name>
                <security-name>sec101</security-name>
                <context>cont1</context>
                <tag>109</tag>
            </snmp-community>
            <snmp-community>
                <name>v3_comm2</name>
                <community-name>$9$9te0A0IKMX-dslKwgoGq.</community-name>
                <security-name>sec102</security-name>
                <context>cont1</context>
                <tag>109</tag>
            </snmp-community>
        </v3>
        <subagent>
            <tcp>
                <routing-instance>
                    <default/>
                </routing-instance>
            </tcp>
        </subagent>
        <engine-id>
            <use-mac-address/>
        </engine-id>
        <community>
            <name>comm1</name>
            <clients>
                <name>24.0.0.0/32</name>
                <restrict/>
            </clients>
            <clients>
                <name>30.0.0.0/32</name>
                <restrict/>
            </clients>
            <routing-instance>
                <name>clv1</name>
                <clients>
                    <name>13.13.13.13/24</name>
                    <restrict/>
                </clients>
                <clients>
                    <name>24.0.0.0/32</name>
                </clients>
                <clients>
                    <name>30.0.0.0/32</name>
                </clients>
            </routing-instance>
            <routing-instance>
                <name>clv2</name>
                <clients>
                    <name>15.15.15.15/24</name>
                </clients>
            </routing-instance>
        </community>
        <community>
            <name>comm2</name>
        </community>
        <trap-group>
            <name>trgrp_01</name>
            <destination-port>2346</destination-port>
            <categories>
                <authentication/>
                <chassis/>
                <otn-alarms>
                    <oc-lof/>
                    <otu-uas-threshold/>
                </otn-alarms>
            </categories>
            <targets>
                <name>11.11.11.11</name>
            </targets>
            <targets>
                <name>12.12.12.12</name>
            </targets>
            <routing-instance>clv1</routing-instance>
        </trap-group>
        <routing-instance-access>
            <access-list>
                <name>clv1</name>
            </access-list>
            <access-list>
                <name>clv2</name>
            </access-list>
        </routing-instance-access>
        <logical-system-trap-filter/>
        <traceoptions>
            <memory-trace>
                <size>1350</size>
            </memory-trace>
            <file>
                <size>20000</size>
                <files>20</files>
                <no-world-readable/>
                <match>snmp_cfg</match>
            </file>
            <flag>
                <name>all</name>
            </flag>
            <flag>
                <name>general</name>
            </flag>
            <flag>
                <name>interface-stats</name>
            </flag>
            <flag>
                <name>nonvolatile-sets</name>
            </flag>
            <flag>
                <name>pdu</name>
            </flag>
            <flag>
                <name>protocol-timeouts</name>
            </flag>
            <flag>
                <name>routing-socket</name>
            </flag>
            <flag>
                <name>subagent</name>
            </flag>
            <flag>
                <name>timer</name>
            </flag>
            <flag>
                <name>varbind-error</name>
            </flag>
        </traceoptions>
        <rmon>
            <alarm>
                <name>4</name>
                <variable>1.x.y.z</variable>
                <sample-type>absolute-value</sample-type>
                <rising-threshold>1020</rising-threshold>
            </alarm>
            <alarm>
                <name>5</name>
                <variable>1.x.y.z</variable>
                <sample-type>absolute-value</sample-type>
                <rising-threshold>1020</rising-threshold>
            </alarm>
            <event>
                <name>100</name>
                <type>log</type>
            </event>
            <event>
                <name>200</name>
                <type>log</type>
            </event>
        </rmon>
        <health-monitor>
            <interval>100</interval>
            <rising-threshold>60</rising-threshold>
            <falling-threshold>50</falling-threshold>
            <idp>
            </idp>
        </health-monitor>
        <customization>
            <ether-stats-ifd-only/>
        </customization>
    </snmp>
                </configuration>
            </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_dict = {
            "communities": [
                {
                    "clients": [
                        {"address": "24.0.0.0/32", "restrict": True},
                        {"address": "30.0.0.0/32", "restrict": True},
                    ],
                    "name": "comm1",
                    "routing_instances": [
                        {
                            "clients": [
                                {
                                    "address": "13.13.13.13/24",
                                    "restrict": True,
                                },
                                {"address": "24.0.0.0/32"},
                                {"address": "30.0.0.0/32"},
                            ],
                            "name": "clv1",
                        },
                        {
                            "clients": [{"address": "15.15.15.15/24"}],
                            "name": "clv2",
                        },
                    ],
                },
                {"name": "comm2"},
            ],
            "contact": "rohitthakur2590",
            "customization": {"ether_stats_ifd_only": True},
            "description": "Local SNMP Server",
            "engine_id": {"use_mac_address": True},
            "filter_duplicates": True,
            "filter_interfaces": {
                "all_internal_interfaces": True,
                "interfaces": ["eth1", "eth2"],
            },
            "health_monitor": {
                "falling_threshold": 50,
                "idp": True,
                "interval": 100,
                "rising_threshold": 60,
            },
            "if_count_with_filter_interfaces": True,
            "location": "inter_lab",
            "logical_system_trap_filter": True,
            "name": "SNMP_LAB_SERVER",
            "nonvolatile": {"commit_delay": 30},
            "rmon": {
                "alarms": [
                    {
                        "id": "4",
                        "rising_threshold": 1020,
                        "sample_type": "absolute-value",
                        "variable": "1.x.y.z",
                    },
                    {
                        "id": "5",
                        "rising_threshold": 1020,
                        "sample_type": "absolute-value",
                        "variable": "1.x.y.z",
                    },
                ],
                "events": [
                    {"id": 100, "type": "log"},
                    {"id": 200, "type": "log"},
                ],
            },
            "routing_instance_access": {"access_lists": ["clv1", "clv2"]},
            "snmp_v3": {
                "notify": [{"name": "not1", "tag": "tag2", "type": "inform"}],
                "notify_filter": [
                    {
                        "name": "not_fil_01",
                        "oids": [{"include": True, "oid": "1.a.s.b.d"}],
                    },
                    {
                        "name": "not_fil_02",
                        "oids": [
                            {"include": True, "oid": "1.x.b.b.d"},
                            {"include": True, "oid": "1.a.c.b.d"},
                        ],
                    },
                ],
                "snmp_community": [
                    {
                        "community_index": "v3_comm1",
                        "community_name": "$9$gUoGiQF/tpB5QORhr8LjHq",
                        "context": "cont1",
                        "security_name": "sec101",
                        "tag": "109",
                    },
                    {
                        "community_index": "v3_comm2",
                        "community_name": "$9$9te0A0IKMX-dslKwgoGq.",
                        "context": "cont1",
                        "security_name": "sec102",
                        "tag": "109",
                    },
                ],
                "target_addresses": [
                    {
                        "address": "162.12.10.2",
                        "address_mask": "24.0.0.0",
                        "name": "tar201",
                        "port": 23122,
                        "retry_count": 200,
                        "routing_instance": "clv2",
                        "tag_list": "tag101",
                        "target_parameters": "tarparam2",
                        "timeout": 300,
                    },
                    {
                        "address": "162.12.10.2",
                        "address_mask": "24.0.0.0",
                        "name": "tar202",
                        "port": 23122,
                        "retry_count": 200,
                        "routing_instance": "clv2",
                        "tag_list": "tag101",
                        "target_parameters": "tarparam2",
                        "timeout": 300,
                    },
                ],
                "target_parameters": [
                    {
                        "name": "param111",
                        "notify_filter": "{'filter': 'not121'}",
                        "parameters": {
                            "message_processing_model": "v1",
                            "security_level": "none",
                            "security_model": "v1",
                            "security_name": "secure111",
                        },
                    }
                ],
            },
            "subagent": {"tcp": {"routing_instances_default": True}},
            "traceoptions": {
                "file": {
                    "files": 20,
                    "match": "snmp_cfg",
                    "no_world_readable": True,
                    "size": 20000,
                },
                "flag": {
                    "all": True,
                    "general": True,
                    "interface_stats": True,
                    "nonvolatile_sets": True,
                    "pdu": True,
                    "protocol_timeouts": True,
                    "routing_socket": True,
                    "subagent": True,
                    "timer": True,
                    "varbind_error": True,
                },
                "memory_trace": {"size": 1350},
            },
            "trap_groups": [
                {
                    "categories": {
                        "authentication": True,
                        "chassis": True,
                        "otn_alarms": {
                            "oc_lof": True,
                            "otu_uas_threshold": True,
                        },
                    },
                    "destination_port": 2346,
                    "name": "trgrp_01",
                    "routing_instance": "clv1",
                    "targets": ["11.11.11.11", "12.12.12.12"],
                }
            ],
        }
        self.assertEqual(sorted(parsed_dict), sorted(result["parsed"]))

    def test_junos_ntp_global_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    client_lists=[
                        dict(
                            name="cl2",
                            addresses=[dict(address="192.16.4.0/24")],
                        )
                    ]
                ),
                state="rendered",
            )
        )
        rendered = (
            '<nc:snmp xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:client-list><nc:name>cl2</nc:name>'
            "<nc:client-address-list><nc:name>192.16.4.0/24</nc:name></nc:client-address-list>"
            "</nc:client-list></nc:snmp>"
        )
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(rendered))
