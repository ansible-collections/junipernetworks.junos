#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos bgp_global fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from copy import deepcopy
from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.bgp_global.bgp_global import (
    Bgp_globalArgs,
)
from ansible.module_utils.six import string_types

try:
    from lxml import etree

    HAS_LXML = True
except ImportError:
    HAS_LXML = False

try:
    import xmltodict

    HAS_XMLTODICT = True
except ImportError:
    HAS_XMLTODICT = False


class Bgp_globalFacts(object):
    """ The junos bgp_global fact class
    """

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Bgp_globalArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_connection(self, connection, config_filter):
        """

        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filter)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for bgp_global
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")

        if not data:
            config_filter = """
                <configuration>
                    <protocols>
                        <bgp>
                        </bgp>
                    </protocols>
                    <routing-options>
                        <autonomous-system/>
                    </routing-options>
                </configuration>
                """
            data = self.get_connection(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace")
            )
        objs = {}
        resources = data.xpath("configuration/protocols/bgp")
        autonomous_system_path = data.xpath(
            "configuration/routing-options/autonomous-system"
        )
        if autonomous_system_path:
            self.autonomous_system = self._get_xml_dict(
                autonomous_system_path.pop()
            )
        else:
            self.autonomous_system = ""
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)
        if not objs:
            if self.autonomous_system and self.autonomous_system.get(
                "autonomous-system"
            ):
                objs["as_number"] = self.autonomous_system[
                    "autonomous-system"
                ].get("as-number")
                if self.autonomous_system["autonomous-system"].get("loops"):
                    objs["loops"] = self.autonomous_system[
                        "autonomous-system"
                    ].get("loops")
                if (
                    "asdot-notation"
                    in self.autonomous_system["autonomous-system"]
                ):
                    objs["asdot_notation"] = True
        facts = {}
        if objs:
            facts["bgp_global"] = {}
            params = utils.validate_config(
                self.argument_spec, {"config": objs}
            )
            facts["bgp_global"] = utils.remove_empties(params["config"])
        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(
            etree.tostring(xml_root), dict_constructor=dict
        )
        return xml_dict

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        bgp_global = {}
        bgp = conf.get("bgp")
        # Set ASN value into facts
        if self.autonomous_system and self.autonomous_system.get(
            "autonomous-system"
        ):
            bgp_global["as_number"] = self.autonomous_system[
                "autonomous-system"
            ].get("as-number")
            if self.autonomous_system["autonomous-system"].get("loops"):
                bgp_global["loops"] = self.autonomous_system[
                    "autonomous-system"
                ].get("loops")
            if "asdot-notation" in self.autonomous_system["autonomous-system"]:
                bgp_global["asdot_notation"] = True

        self.parse_attrib(bgp_global, bgp)

        # Read group
        if "group" in bgp.keys():
            bgp_groups = []
            bgp_group = {}
            groups = bgp.get("group")
            if isinstance(groups, dict):
                self.parse_attrib(bgp_group, groups)
                # parse neighbors
                if "neighbor" in groups.keys():
                    neighbors_lst = []
                    neighbors_dict = {}
                    neighbors = groups.get("neighbor")
                    if isinstance(neighbors, dict):
                        self.parse_attrib(
                            neighbors_dict, neighbors, "neighbor"
                        )
                        if neighbors_dict:
                            neighbors_lst.append(neighbors_dict)
                    else:
                        for neighbor in neighbors:
                            self.parse_attrib(
                                neighbors_dict, neighbor, "neighbor"
                            )
                            if neighbors_dict:
                                neighbors_lst.append(neighbors_dict)
                    if neighbors_lst:
                        bgp_group["neighbors"] = neighbors_lst

                if bgp_group:
                    bgp_groups.append(bgp_group)
            else:
                for group in groups:
                    bgp_group = {}
                    self.parse_attrib(bgp_group, group)
                    # Parse neighbors in the group list
                    if "neighbor" in group.keys():
                        neighbors_lst = []
                        neighbors_dict = {}
                        neighbors = group.get("neighbor")
                        if isinstance(neighbors, dict):
                            self.parse_attrib(
                                neighbors_dict, neighbors, "neighbor"
                            )
                            if neighbors_dict:
                                neighbors_lst.append(neighbors_dict)
                        else:
                            for neighbor in neighbors:
                                self.parse_attrib(
                                    neighbors_dict, neighbor, "neighbor"
                                )
                                if neighbors_dict:
                                    neighbors_lst.append(neighbors_dict)
                                    neighbors_dict = {}

                        if neighbors_lst:
                            bgp_group["neighbors"] = neighbors_lst

                    if bgp_group:
                        bgp_groups.append(bgp_group)
            bgp_global["groups"] = bgp_groups
        utils.remove_empties(bgp_global)
        return bgp_global

    def parse_attrib(self, cfg_dict, conf, type=None):
        # Read accept-remote-nexthop value
        if "accept-remote-nexthop" in conf.keys():
            cfg_dict["accept_remote_nexthop"] = True

        # Read add-path-display-ipv4-address value
        if "add-path-display-ipv4-address" in conf.keys():
            cfg_dict["add_path_display_ipv4_address"] = True

        # Parse advertise-bgp-static dictionary
        if "advertise-bgp-static" in conf.keys():
            cfg = {}
            if (
                conf.get("advertise-bgp-static")
                and "advertise-bgp-static" in conf.keys()
            ):
                if "policy" in conf["advertise-bgp-static"]:
                    cfg["policy"] = conf["advertise-bgp-static"].get("policy")
            else:
                cfg["set"] = True
            cfg_dict["advertise_bgp_static"] = cfg

        # Parse advertise-external dictionary
        if "advertise-external" in conf.keys():
            cfg = {}
            if "conditional" in conf["advertise-bgp-static"].keys():
                cfg["conditional"] = True
            else:
                cfg["set"] = True
            cfg_dict["advertise_external"] = cfg

        # Read advertise-from-main-vpn-tables value
        if "advertise-from-main-vpn-tables" in conf.keys():
            cfg_dict["advertise_from_main_vpn_tables"] = True

        # Read advertise-inactive value
        if "advertise-inactive" in conf.keys():
            cfg_dict["advertise_inactive"] = True

        # Read advertise-peer-as value
        if "advertise-peer-as" in conf.keys():
            cfg_dict["advertise_peer_as"] = True

        # Read authentication-algorithm value
        if "authentication-algorithm" in conf.keys():
            cfg_dict["authentication_algorithm"] = conf[
                "authentication-algorithm"
            ]

        # Read authentication-key value
        if "authentication-key" in conf.keys():
            cfg_dict["authentication_key"] = conf["authentication-key"]

        # Read authentication-key-chain value
        if "authentication-key-chain" in conf.keys():
            cfg_dict["authentication_key_chain"] = conf[
                "authentication-key-chain"
            ]

        # Parse bfd-liveness-detection dictionary
        if "bfd-liveness-detection" in conf.keys():
            cfg = {}
            bld = conf["bfd-liveness-detection"]
            # Parse authentication dictionary
            if "authentication" in bld.keys():
                a_dict = {}
                authentication = bld["authentication"]
                if "algorithm" in authentication.keys():
                    a_dict["algorithm"] = authentication["algorithm"]
                if "key-chain" in authentication.keys():
                    a_dict["key_chain"] = authentication["key-chain"]
                if "loose-check" in authentication.keys():
                    a_dict["loose_check"] = True
                cfg["authentication"] = a_dict

            # Parse detection-time dictionary
            if "detection-time" in bld.keys():
                dt_dict = {}
                d_time = bld["detection-time"]
                if "threshold" in d_time.keys():
                    dt_dict["threshold"] = d_time["threshold"]
                cfg["detection_time"] = dt_dict
            # Parse transmit-interval dictionary
            if "transmit-interval" in bld.keys():
                t_dict = {}
                t_int = bld["transmit-interval"]
                if "minimum-interval" in t_int.keys():
                    t_dict["minimum_interval"] = t_int["minimum-interval"]
                cfg["transmit_interval"] = t_dict

            # Read holddown-interval value
            if "holddown-interval" in bld.keys():
                cfg["holddown_interval"] = bld["holddown-interval"]

            # Read minimum-receive-interval value
            if "minimum-receive-interval" in bld.keys():
                cfg["minimum_receive_interval"] = bld[
                    "minimum-receive-interval"
                ]

            # Read minimum-interval value
            if "minimum-interval" in bld.keys():
                cfg["minimum_interval"] = bld["minimum-interval"]

            # Read multiplier value
            if "multiplier" in bld.keys():
                cfg["multiplier"] = bld["multiplier"]

            # Read no-adaptation value
            if "no-adaptation" in bld.keys():
                cfg["no_adaptation"] = True

            # Read session-mode value
            if "session-mode" in bld.keys():
                cfg["session_mode"] = bld["session-mode"]

            # Read version value
            if "version" in bld.keys():
                cfg["version"] = bld["version"]

            # write the  bfd_liveness_detection to bgp global config dictionary
            cfg_dict["bfd_liveness_detection"] = cfg

        # Parse bgp-error-tolerance dictionary
        if "bgp-error-tolerance" in conf.keys():
            cfg = {}
            bet = conf["bgp-error-tolerance"]
            # Parse authentication dictionary
            if "malformed-route-limit" in bet.keys():
                cfg["malformed_route_limit"] = bet["malformed-route-limit"]
            if "malformed-update-log-interval" in bet.keys():
                cfg["malformed_update_log_interval"] = bet[
                    "malformed-update-log-interval"
                ]
            if "no-malformed-route-limit" in bet.keys():
                cfg["no_malformed_route_limit"] = True
            # write the  bfd_liveness_detection to bgp global config dictionary
            cfg_dict["bgp_error_tolerance"] = cfg

        # Parse bmp dictionary
        if "bmp" in conf.keys():
            cfg = {}
            bmp = conf["bmp"]
            # Parse authentication dictionary
            if "route-monitoring" in bmp.keys():
                rm_dict = {}
                r_monitoring = bmp["route-monitoring"]

                # Read none attribute value
                if "none" in r_monitoring.keys():
                    rm_dict["none"] = True

                # Read post-policy attribute value
                if "post-policy" in r_monitoring.keys():
                    if r_monitoring["post-policy"].keys(
                        "exclude-non-eligible"
                    ):
                        rm_dict["post_policy_exclude_non_eligible"] = True
                    else:
                        rm_dict["post_policy"] = True

                # Read pre-policy attribute value
                if "pre-policy" in r_monitoring.keys():
                    if r_monitoring["pre-policy"].keys("exclude-non-feasible"):
                        rm_dict["pre_policy_exclude_non_feasible"] = True
                    else:
                        rm_dict["pre_policy"] = True
                cfg["route_monitoring"] = rm_dict
            # Read monitor value
            if "monitor" in bmp.keys():
                if bmp["monitor"] == "disable":
                    cfg["monitor"] = False
                else:
                    cfg["monitor"] = True

            # write the  bmp to bgp global config dictionary
            cfg_dict["bmp"] = cfg

        # Read cluster value
        if "cluster" in conf.keys():
            cfg_dict["cluster_id"] = conf["cluster"]

        # Read damping value
        if "damping" in conf.keys():
            cfg_dict["damping"] = True

        # Read description value
        if "description" in conf.keys():
            cfg_dict["description"] = conf["description"]

        # Read disable value
        if "disable" in conf.keys():
            cfg_dict["disable"] = True

        # Read egress-te-sid-stats value
        if "egress-te-sid-stats" in conf.keys():
            cfg_dict["egress_te_sid_stats"] = True

        # Read enforce-first-as value
        if "enforce-first-as" in conf.keys():
            cfg_dict["enforce_first_as"] = True

        # Read export value
        if "export" in conf.keys():
            cfg_dict["export"] = conf["export"]

        # Read forwarding-context value
        if "forwarding-context" in conf.keys():
            cfg_dict["forwarding_context"] = conf["forwarding-context"]

        # Read hold-time value
        if "hold-time" in conf.keys():
            cfg_dict["hold_time"] = conf["hold-time"]

        # Read holddown-all-stale-labels value
        if "holddown-all-stale-labels" in conf.keys():
            cfg_dict["holddown_all_stale_labels"] = True

        # Read import value
        if "import" in conf.keys():
            cfg_dict["import"] = conf["import"]

        # Read include-mp-next-hop value
        if "include-mp-next-hop" in conf.keys():
            cfg_dict["include_mp_next_hop"] = True

        # Read ipsec-sa value
        if "ipsec-sa" in conf.keys():
            cfg_dict["ipsec_sa"] = conf["ipsec-sa"]

        # Read keep value
        if "keep" in conf.keys():
            cfg_dict["keep"] = conf["keep"]

        # Read local-address value
        if "local-address" in conf.keys():
            cfg_dict["local_address"] = conf["local-address"]

        # Read local-interface value
        if "local-interface" in conf.keys():
            cfg_dict["local_interface"] = conf["local-interface"]

        # Read local-preference value
        if "local-preference" in conf.keys():
            cfg_dict["local_preference"] = conf["local-preference"]

        # Read log-updown value
        if "log-updown" in conf.keys():
            cfg_dict["log_updown"] = True

        # Read mtu-discovery value
        if "mtu-discovery" in conf.keys():
            cfg_dict["mtu_discovery"] = True

        # Read no-advertise-peer-as value
        if "no-advertise-peer-as" in conf.keys():
            cfg_dict["no_advertise_peer_as"] = True

        # Read no-aggregator-id value
        if "no-aggregator-id" in conf.keys():
            cfg_dict["no_aggregator_id"] = True

        # Read no-client-reflect value
        if "no-client-reflect" in conf.keys():
            cfg_dict["no_client_reflect"] = True

        # Read no-precision-timers value
        if "no-precision-timers" in conf.keys():
            cfg_dict["no_precision_timers"] = True

        # Read out-delay value
        if "out-delay" in conf.keys():
            cfg_dict["out_delay"] = conf["out-delay"]

        # Read passive value
        if "passive" in conf.keys():
            cfg_dict["passive"] = True

        # Read peer-as value
        if "peer-as" in conf.keys():
            cfg_dict["peer_as"] = conf["peer-as"]

        # Read precision-timers value
        if "precision-timers" in conf.keys():
            cfg_dict["precision_timers"] = True

        # Read preference value
        if "preference" in conf.keys():
            cfg_dict["preference"] = conf["preference"]

        # Read rfc6514-compliant-safi129 value
        if "rfc6514-compliant-safi129" in conf.keys():
            cfg_dict["rfc6514_compliant_safi129"] = True

        # Read route-server-client value
        if "route-server-client" in conf.keys():
            cfg_dict["route_server_client"] = True

        # Read send-addpath-optimization value
        if "send-addpath-optimization" in conf.keys():
            cfg_dict["send_addpath_optimization"] = True

        # Read sr-preference-override value
        if "sr-preference-override" in conf.keys():
            cfg_dict["sr_preference_override"] = conf["sr-preference-override"]

        # Read stale-labels-holddown-period value
        if "stale-labels-holddown-period" in conf.keys():
            cfg_dict["stale_labels_holddown_period"] = conf[
                "stale-labels-holddown-period"
            ]

        # Read tcp-aggressive-transmission value
        if "tcp-aggressive-transmission" in conf.keys():
            cfg_dict["tcp_aggressive_transmission"] = True

        # Read tcp-mss value
        if "tcp-mss" in conf.keys():
            cfg_dict["tcp_mss"] = conf["tcp-mss"]

        # Read ttl value
        if "ttl" in conf.keys():
            cfg_dict["ttl"] = conf["ttl"]

        # Read unconfigured-peer-graceful-restart value
        if "unconfigured-peer-graceful-restart" in conf.keys():
            cfg_dict["unconfigured_peer_graceful_restart"] = True

        # Read vpn-apply-export value
        if "vpn-apply-export" in conf.keys():
            cfg_dict["vpn_apply_export"] = True

        # Read group name value
        if "name" in conf.keys():
            if type == "neighbor":
                cfg_dict["neighbor_address"] = conf["name"]
            else:
                cfg_dict["name"] = conf["name"]

        # Read as-override value
        if "as-override" in conf.keys():
            cfg_dict["as_override"] = True

        # Read allow
        if "allow" in conf.keys():
            allow_lst = []
            allow = conf["allow"]
            if isinstance(allow, list):
                for item in allow:
                    allow_lst.append(item)
            else:
                allow_lst.append(allow)
            if allow_lst:
                cfg_dict["allow"] = allow_lst

        # Read optimal-route-reflection
        if "optimal-route-reflection" in conf.keys():
            orr_dict = {}
            orr = conf["optimal-route-reflection"]

            if "igp-backup" in orr.keys():
                orr_dict["igp_backup"] = orr.get("igp-backup")

            if "igp-primary" in orr.keys():
                orr_dict["igp_primary"] = orr.get("igp-primary")
            cfg_dict["optimal_route_reflection"] = orr_dict

        # Read group type value
        if "type" in conf.keys():
            cfg_dict["type"] = conf["type"]

        # Read unconfigured-peer-graceful-restart value
        if "unconfigured-peer-graceful-restart" in conf.keys():
            cfg_dict["unconfigured_peer_graceful_restart"] = True

        # Read vpn-apply-export value
        if "vpn-apply-export" in conf.keys():
            cfg_dict["vpn_apply_export"] = True
