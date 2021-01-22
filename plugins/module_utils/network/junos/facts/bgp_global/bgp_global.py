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
                </configuration>
                """
            data = self.get_connection(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace")
            )
        objs = {}
        resources = data.xpath("configuration/protocols/bgp")
        autonomous_system = data.xpath(
            "configuration/routing-options/autonomous-system"
        )
        if autonomous_system:
            self.autonomous_system = self._get_xml_dict(
                autonomous_system.pop()
            )
        else:
            self.autonomous_system = ""
        for resource in resources:
            if resource:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)
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
        # Read accept-remote-nexthop value
        if "accept-remote-nexthop" in bgp.keys():
            bgp_global["accept_remote_nexthop"] = True

        # Read add-path-display-ipv4-address value
        if "add-path-display-ipv4-address" in bgp.keys():
            bgp_global["add_path_display_ipv4_address"] = True

        # Parse advertise-bgp-static dictionary
        if "advertise-bgp-static" in bgp.keys():
            cfg = {}
            if (
                bgp.get("advertise-bgp-static")
                and "advertise-bgp-static" in bgp.keys()
            ):
                if "policy" in bgp["advertise-bgp-static"]:
                    cfg["policy"] = bgp["advertise-bgp-static"].get("policy")
            else:
                cfg["set"] = True
            bgp_global["advertise_bgp_static"] = cfg

        # Parse advertise-external dictionary
        if "advertise-external" in bgp.keys():
            cfg = {}
            if "conditional" in bgp["advertise-bgp-static"].keys():
                cfg["conditional"] = True
            else:
                cfg["set"] = True
            bgp_global["advertise_external"] = cfg

        # Read advertise-from-main-vpn-tables value
        if "advertise-from-main-vpn-tables" in bgp.keys():
            bgp_global["advertise_from_main_vpn_tables"] = True

        # Read advertise-inactive value
        if "advertise-inactive" in bgp.keys():
            bgp_global["advertise_inactive"] = True

        # Read advertise-peer-as value
        if "advertise-peer-as" in bgp.keys():
            bgp_global["advertise_peer_as"] = True

        # Read authentication-algorithm value
        if "authentication-algorithm" in bgp.keys():
            bgp_global["authentication_algorithm"] = bgp[
                "authentication-algorithm"
            ]

        # Read authentication-key value
        if "authentication-key" in bgp.keys():
            bgp_global["authentication_key"] = bgp["authentication-key"]

        # Read authentication-key-chain value
        if "authentication-key-chain" in bgp.keys():
            bgp_global["authentication_key_chain"] = bgp[
                "authentication-key-chain"
            ]

        # Parse bfd-liveness-detection dictionary
        if "bfd-liveness-detection" in bgp.keys():
            cfg = {}
            bld = bgp["bfd-liveness-detection"]
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
            bgp_global["bfd_liveness_detection"] = cfg

        # Parse bgp-error-tolerance dictionary
        if "bgp-error-tolerance" in bgp.keys():
            cfg = {}
            bet = bgp["bgp-error-tolerance"]
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
            bgp_global["bgp_error_tolerance"] = cfg

        # Parse bmp dictionary
        if "bmp" in bgp.keys():
            cfg = {}
            bmp = bgp["bmp"]
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
            bgp_global["bmp"] = cfg

        # Read cluster value
        if "cluster" in bgp.keys():
            bgp_global["cluster_id"] = bgp["cluster"]

        # Read damping value
        if "damping" in bgp.keys():
            bgp_global["damping"] = True

        # Read description value
        if "description" in bgp.keys():
            bgp_global["description"] = bgp["description"]

        # Read disable value
        if "disable" in bgp.keys():
            bgp_global["disable"] = True

        # Read egress-te-sid-stats value
        if "egress-te-sid-stats" in bgp.keys():
            bgp_global["egress_te_sid_stats"] = True

        # Read enforce-first-as value
        if "enforce-first-as" in bgp.keys():
            bgp_global["enforce_first_as"] = True

        # Read export value
        if "export" in bgp.keys():
            bgp_global["export"] = bgp["export"]

        # Read forwarding-context value
        if "forwarding-context" in bgp.keys():
            bgp_global["forwarding_context"] = bgp["forwarding-context"]

        # Read hold-time value
        if "hold-time" in bgp.keys():
            bgp_global["hold_time"] = bgp["hold-time"]

        # Read holddown-all-stale-labels value
        if "holddown-all-stale-labels" in bgp.keys():
            bgp_global["holddown_all_stale_labels"] = True

        # Read import value
        if "import" in bgp.keys():
            bgp_global["import"] = bgp["import"]

        # Read include-mp-next-hop value
        if "include-mp-next-hop" in bgp.keys():
            bgp_global["include_mp_next_hop"] = True

        # Read ipsec-sa value
        if "ipsec-sa" in bgp.keys():
            bgp_global["ipsec_sa"] = bgp["ipsec-sa"]

        # Read keep value
        if "keep" in bgp.keys():
            bgp_global["keep"] = bgp["keep"]

        # Read local-address value
        if "local-address" in bgp.keys():
            bgp_global["local_address"] = bgp["local-address"]

        # Read local-interface value
        if "local-interface" in bgp.keys():
            bgp_global["local_interface"] = bgp["local-interface"]

        # Read local-preference value
        if "local-preference" in bgp.keys():
            bgp_global["local_preference"] = bgp["local-preference"]

        # Read log-updown value
        if "log-updown" in bgp.keys():
            bgp_global["log_updown"] = True

        # Read mtu-discovery value
        if "mtu-discovery" in bgp.keys():
            bgp_global["mtu_discovery"] = True

        # Read no-advertise-peer-as value
        if "no-advertise-peer-as" in bgp.keys():
            bgp_global["no_advertise_peer_as"] = True

        # Read no-aggregator-id value
        if "no-aggregator-id" in bgp.keys():
            bgp_global["no_aggregator_id"] = True

        # Read no-client-reflect value
        if "no-client-reflect" in bgp.keys():
            bgp_global["no_client_reflect"] = True

        # Read no-precision-timers value
        if "no-precision-timers" in bgp.keys():
            bgp_global["no_precision_timers"] = True

        # Read out-delay value
        if "out-delay" in bgp.keys():
            bgp_global["out_delay"] = bgp["out-delay"]

        # Read passive value
        if "passive" in bgp.keys():
            bgp_global["passive"] = True

        # Read peer-as value
        if "peer-as" in bgp.keys():
            bgp_global["peer_as"] = bgp["peer-as"]

        # Read precision-timers value
        if "precision-timers" in bgp.keys():
            bgp_global["precision_timers"] = True

        # Read preference value
        if "preference" in bgp.keys():
            bgp_global["preference"] = bgp["preference"]

        # Read rfc6514-compliant-safi129 value
        if "rfc6514-compliant-safi129" in bgp.keys():
            bgp_global["rfc6514_compliant_safi129"] = True

        # Read route-server-client value
        if "route-server-client" in bgp.keys():
            bgp_global["route_server_client"] = True

        # Read send-addpath-optimization value
        if "send-addpath-optimization" in bgp.keys():
            bgp_global["send_addpath_optimization"] = True

        # Read sr-preference-override value
        if "sr-preference-override" in bgp.keys():
            bgp_global["sr_preference_override"] = bgp[
                "sr-preference-override"
            ]

        # Read stale-labels-holddown-period value
        if "stale-labels-holddown-period" in bgp.keys():
            bgp_global["stale_labels_holddown_period"] = bgp[
                "stale-labels-holddown-period"
            ]

        # Read tcp-aggressive-transmission value
        if "tcp-aggressive-transmission" in bgp.keys():
            bgp_global["tcp_aggressive_transmission"] = True

        # Read tcp-mss value
        if "tcp-mss" in bgp.keys():
            bgp_global["tcp_mss"] = bgp["tcp-mss"]

        # Read ttl value
        if "ttl" in bgp.keys():
            bgp_global["ttl"] = bgp["ttl"]

        # Read unconfigured-peer-graceful-restart value
        if "unconfigured-peer-graceful-restart" in bgp.keys():
            bgp_global["unconfigured_peer_graceful_restart"] = True

        # Read vpn-apply-export value
        if "vpn-apply-export" in bgp.keys():
            bgp_global["vpn_apply_export"] = True

        utils.remove_empties(bgp_global)
        return bgp_global
