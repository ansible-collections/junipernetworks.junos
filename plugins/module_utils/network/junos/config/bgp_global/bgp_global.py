#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_bgp_global class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    locked_config,
    load_config,
    commit_configuration,
    discard_changes,
    tostring,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
    remove_empties,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.facts import Facts
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    build_root_xml_node,
    build_child_xml_node,
)


class Bgp_global(ConfigBase):
    """
    The junos_bgp_global class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["bgp_global"]

    def __init__(self, module):
        super(Bgp_global, self).__init__(module)

    def get_bgp_global_facts(self, data=None):
        """ Get the 'facts' (the current configuration)
        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources, data=data
        )
        bgp_facts = facts["ansible_network_resources"].get("bgp_global")
        if not bgp_facts:
            return {}
        return bgp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]

        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_bgp_global_facts = self.get_bgp_global_facts()
        else:
            existing_bgp_global_facts = {}
        if state == "gathered":
            existing_bgp_global_facts = self.get_bgp_global_facts()
            result["gathered"] = existing_bgp_global_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed"
                )
            result["parsed"] = self.get_bgp_global_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_bgp_global_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_bgp_global_facts)
            with locked_config(self._module):
                for config_xml in to_list(config_xmls):
                    diff = load_config(self._module, config_xml, [])

                commit = not self._module.check_mode
                if diff:
                    if commit:
                        commit_configuration(self._module)
                    else:
                        discard_changes(self._module)
                    result["changed"] = True

                    if self._module._diff:
                        result["diff"] = {"prepared": diff}

            result["commands"] = config_xmls

            changed_bgp_global_facts = self.get_bgp_global_facts()

            result["before"] = existing_bgp_global_facts
            if result["changed"]:
                result["after"] = changed_bgp_global_facts

            result["warnings"] = warnings

        return result

    def set_config(self, existing_bgp_global_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_bgp_global_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the list xml configuration necessary to migrate the current configuration
                  to the desired configuration
        """
        root = build_root_xml_node("protocols")
        state = self._module.params["state"]
        if state in ("merged", "replaced", "rendered") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state
                )
            )
        if state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state in ("merged", "rendered"):
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)

        for xml in config_xmls:
            root.append(xml)
        return tostring(root)

    def _state_replaced(self, want, have):
        """ The xml configuration generator when state is merged
         :rtype: A list
         :returns: the xml configuration necessary to merge the provided into
                   the current configuration
         """
        bgp_xml = []
        bgp_xml.extend(self._state_deleted(want, have))
        bgp_xml.extend(self._state_merged(want, have))

        return bgp_xml

    def _state_merged(self, want, have):
        """ Select the appropriate function based on the state provided
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the list xml configuration necessary to migrate the current configuration
                  to the desired configuration
        """
        bgp_xml = []

        bgp_root = build_root_xml_node("bgp")

        want = remove_empties(want)

        # Generate config commands for accept-remote-nexthop
        if "accept_remote_next_hop" in want.keys():
            b_val = want.get("accept_remote_next_hop")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "accept-remote-nexthop")

        # Generate config commands for add-path-display-ipv4-address
        if "accept_remote_next_hop" in want.keys():
            b_val = want.get("accept_remote_next_hop")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "add-path-display-ipv4-address")

        # Generate config commands for advertise-bgp-static
        if want.get("advertise_bgp_static"):
            ad_bgp_static_node = build_child_xml_node(
                bgp_root, "advertise-bgp-static"
            )
            ad_bgp_static = want.get("advertise_bgp_static")
            if "policy" in ad_bgp_static.keys():
                build_child_xml_node(
                    ad_bgp_static_node, "policy"
                )

        # Generate config commands for advertise-external
        if want.get("advertise_external"):
            ad_ext_node = build_child_xml_node(
                bgp_root, "advertise-external"
            )
            ad_ext = want.get("advertise_external")
            if "conditional" in ad_ext.keys():
                build_child_xml_node(
                    ad_ext_node, "conditional"
                )

        # Generate config commands for advertise-from-main-vpn-tables
        if "advertise_from_main_vpn_tables" in want.keys():
            b_val = want.get("advertise_from_main_vpn_tables")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "advertise-from-main-vpn-tables")

        # Generate config commands for advertise-inactive
        if "advertise_inactive" in want.keys():
            b_val = want.get("advertise_inactive")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "advertise-inactive")

        # Generate config commands for advertise-peer-as
        if "advertise_peer_as" in want.keys():
            b_val = want.get("advertise_peer_as")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "advertise-peer-as")

        # Generate config commands for authentication-algorithm
        if want.get("authentication_algorithm"):
            build_child_xml_node(
                bgp_root, "authentication-algorithm", want["authentication_algorithm"]
            )

        # Generate config commands for authentication-key
        if want.get("authentication_key"):
            build_child_xml_node(
                bgp_root, "authentication-key", want["authentication_key"]
            )

        # Generate config commands for authentication-key-chain
        if want.get("authentication_key_chain"):
            build_child_xml_node(
                bgp_root, "authentication-key-chain", want["authentication_key_chain"]
            )

        # Generate config commands for bfd-liveness-detection
        if want.get("bfd_liveness_detection"):
            bfd_live_node = build_child_xml_node(
                bgp_root, "bfd-liveness-detection"
            )
            bfd_live_detect = want.get("bfd_liveness_detection")

            # Add node for authentication

            if "authentication" in bfd_live_detect.keys():
                bld_auth = bfd_live_detect["authentication"]
                bld_auth_node = build_child_xml_node(
                    bfd_live_node, "authentication"
                )
                # Add node for algorithm
                if "algorithm" in bld_auth.keys():
                    build_child_xml_node(
                        bld_auth_node, "algorithm", bld_auth["algorithm"]
                    )
                # Add node for key-chain
                if "key_chain" in bld_auth.keys():
                    build_child_xml_node(
                        bld_auth_node, "key-chain", bld_auth["key_chain"]
                    )
                # Add node for loose-check
                if "loose_check" in bld_auth.keys():
                    b_val = bld_auth.get("loose_check")
                    if b_val is not None:
                        if b_val is True:
                            build_child_xml_node(bld_auth_node, "loose-check")
            # Add node for detection-time
            if "detection_time" in bfd_live_detect.keys():
                d_time = bfd_live_detect["detection_time"]
                bld_dtime_node = build_child_xml_node(
                    bfd_live_node, "detection-time"
                )
                # Add node for threshold
                if "threshold" in d_time.keys():
                    build_child_xml_node(
                        bld_dtime_node, "threshold", d_time["threshold"]
                    )
            # Add node for transmit-interval
            if "transmit_interval" in bfd_live_detect.keys():
                t_int = bfd_live_detect["transmit_interval"]
                t_int_node = build_child_xml_node(
                    bfd_live_node, "transmit-interval"
                )
                # Add node for minimum-interval
                if "minimum_interval" in t_int.keys():
                    build_child_xml_node(
                        t_int_node, "minimum-interval", t_int["minimum_interval"]
                    )
            # Add node for holddown-interval
            if "holddown_interval" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node, "holddown-interval", bfd_live_detect["holddown_interval"]
                )
            # Add node for minimum-receive-interval
            if "minimum_receive_interval" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node, "minimum-receive-interval", bfd_live_detect["minimum_receive_interval"]
                )
            # Add node for minimum-interval
            if "minimum_interval" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node, "minimum-interval", bfd_live_detect["minimum_interval"]
                )
            # Add node for multiplier
            if "multiplier" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node, "multiplier", bfd_live_detect["multiplier"]
                )
            # Add node for no-adaptation
            if "no_adaptation" in bfd_live_detect.keys():
                b_val = bfd_live_detect.get("no_adaptation")
                if b_val is not None:
                    if b_val is True:
                        build_child_xml_node(bfd_live_node, "no-adaptation")
            # Add node for session-mode
            if "session_mode" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node, "session-mode", bfd_live_detect["session_mode"]
                )
            # Add node for version
            if "version" in bfd_live_detect.keys():
                build_child_xml_node(
                    bfd_live_node, "version", bfd_live_detect["version"]
                )
        # Generate config commands for bgp-error-tolerance
        if want.get("bgp_error_tolerance"):
            bgp_err_tol_node = build_child_xml_node(
                bgp_root, "bgp-error-tolerance"
            )
            bgp_err_tol = want.get("bgp_error_tolerance")
            # Add node for malformed-route-limit"
            if "malformed_route_limit" in bgp_err_tol.keys():
                build_child_xml_node(
                    bgp_err_tol_node, "malformed-route-limit", bgp_err_tol["malformed_route_limit"]
                )
            # Add node for malformed-update-log-interval
            if "malformed_update_log_interval" in bgp_err_tol.keys():
                build_child_xml_node(
                    bgp_err_tol_node, "malformed-update-log-interval", bgp_err_tol["malformed_update_log_interval"]
                )
            # Generate config commands for no-malformed-route-limit
            if "no_malformed_route_limit" in bgp_err_tol.keys():
                b_val = bgp_err_tol.get("no_malformed_route_limit")
                if b_val is not None:
                    if b_val is True:
                        build_child_xml_node(bgp_err_tol_node, "no-malformed-route-limit")

        # Generate config commands for bmp
        if want.get("bmp"):
            bmp_node = build_child_xml_node(
                bgp_root, "bmp"
            )
            bmp = want.get("bmp")
            # Add node for route-monitoring
            if "route_monitoring" in bmp.keys():
                r_mon_node = build_child_xml_node(
                    bmp_node, "route-monitoring",
                )
                r_mon = bmp["route_monitoring"]
                # Add node for none
                if "none" in r_mon.keys():
                    b_val = r_mon.get("none")
                    if b_val is not None:
                        if b_val is True:
                            build_child_xml_node(r_mon_node, "none")
                # Add node for post-policy
                if "post_policy_exclude_non_eligible" in r_mon.keys():
                    b_val = r_mon.get("post_policy_exclude_non_eligible")
                    if b_val is not None:
                        if b_val is True:
                            policy_node = build_child_xml_node(r_mon_node, "post-policy")
                            build_child_xml_node(policy_node, "exclude-non-eligible")
                elif "post_policy" in r_mon.keys():
                    b_val = r_mon.get("post_policy")
                    if b_val is not None:
                        if b_val is True:
                            build_child_xml_node(r_mon_node, "post-policy")
                # Add node for post-policy
                if "pre_policy_exclude_non_feasible" in r_mon.keys():
                    b_val = r_mon.get("pre_policy_exclude_non_feasible")
                    if b_val is not None:
                        if b_val is True:
                            policy_node = build_child_xml_node(r_mon_node, "pre-policy")
                            build_child_xml_node(policy_node, "exclude-non-eligible")
                elif "pre-policy" in r_mon.keys():
                    b_val = r_mon.get("pre_policy")
                    if b_val is not None:
                        if b_val is True:
                            build_child_xml_node(r_mon_node, "pre-policy")

        # Generate config commands for cluster
        if want.get("cluster_id"):
            build_child_xml_node(
                bgp_root, "cluster", want["cluster_id"]
            )

        # Generate config commands for damping"
        if "damping" in want.keys():
            b_val = want.get("damping")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "damping")

        # Generate config commands for description
        if want.get("description"):
            build_child_xml_node(
                bgp_root, "description", want["description"]
            )

        # Generate config commands for disable"
        if "disable" in want.keys():
            b_val = want.get("disable")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "disable")

        # Generate config commands for egress-te-sid-stats"
        if "egress_te_sid_stats" in want.keys():
            b_val = want.get("egress_te_sid_stats")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "egress-te-sid-stats")

        # Generate config commands for enforce-first-as"
        if "enforce_first_as" in want.keys():
            b_val = want.get("enforce_first_as")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "enforce-first-as")

        # Generate config commands for export
        if want.get("export"):
            build_child_xml_node(
                bgp_root, "export", want["export"]
            )

        # Generate config commands for forwarding-context
        if want.get("forwarding_context"):
            build_child_xml_node(
                bgp_root, "forwarding-context", want["forwarding_context"]
            )

        # Generate config commands for hold-time
        if want.get("hold_time"):
            build_child_xml_node(
                bgp_root, "hold-time", want["hold_time"]
            )

        # Generate config commands for holddown-all-stale-labels"
        if "holddown_all_stale_labels" in want.keys():
            b_val = want.get("holddown_all_stale_labels")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "holddown-all-stale-labels")

        # Generate config commands for import
        if want.get("import"):
            build_child_xml_node(
                bgp_root, "import", want["import"]
            )

        # Generate config commands for include-mp-next-hop"
        if "include_mp_next_hop" in want.keys():
            b_val = want.get("include_mp_next_hop")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "include-mp-next-hop")

        # Generate config commands for ipsec-sa
        if want.get("ipsec_sa"):
            build_child_xml_node(
                bgp_root, "ipsec-sa", want["ipsec_sa"]
            )

        # Generate config commands for keep
        if want.get("keep"):
            build_child_xml_node(
                bgp_root, "keep", want["keep"]
            )

        # Generate config commands for local-address
        if want.get("local_address"):
            build_child_xml_node(
                bgp_root, "local-address", want["local_address"]
            )

        # Generate config commands for local-interface
        if want.get("local_interface"):
            build_child_xml_node(
                bgp_root, "local-interface", want["local_interface"]
            )

        # Generate config commands for local-preference
        if want.get("local_preference"):
            build_child_xml_node(
                bgp_root, "local-preference", want["local_preference"]
            )

        # Generate config commands for log-updown
        if "log_updown" in want.keys():
            b_val = want.get("log_updown")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "log-updown")

        # Generate config commands for mtu-discovery
        if "mtu_discovery" in want.keys():
            b_val = want.get("mtu_discovery")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "mtu-discovery")

        # Generate config commands for no-advertise-peer-as
        if "no_advertise_peer_as" in want.keys():
            b_val = want.get("no_advertise_peer_as")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "no-advertise-peer-as")

        # Generate config commands for no-aggregator-id
        if "no_aggregator_id" in want.keys():
            b_val = want.get("no_aggregator_id")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "no-aggregator-id")

        # Generate config commands for no-client-reflect
        if "no_client_reflect" in want.keys():
            b_val = want.get("no_client_reflect")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "no-client-reflect")

        # Generate config commands for no-precision-timers
        if "no_precision_timers" in want.keys():
            b_val = want.get("no_precision_timers")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "no-precision-timers")

        # Generate config commands for out-delay
        if want.get("out_delay"):
            build_child_xml_node(
                bgp_root, "out-delay", want["out_delay"]
            )

        # Generate config commands for passive
        if "passive" in want.keys():
            b_val = want.get("passive")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "passive")

        # Generate config commands for peer-as
        if want.get("peer_as"):
            build_child_xml_node(
                bgp_root, "peer-as", want["peer_as"]
            )

        # Generate config commands for precision-timers
        if "precision_timers" in want.keys():
            b_val = want.get("precision_timers")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "precision-timers")

        # Generate config commands for preference
        if want.get("preference"):
            build_child_xml_node(
                bgp_root, "preference", want["preference"]
            )

        # Generate config commands for rfc6514-compliant-safi129
        if "rfc6514_compliant_safi129" in want.keys():
            b_val = want.get("rfc6514_compliant_safi129")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "rfc6514-compliant-safi129")

        # Generate config commands for route-server-client
        if "route_server_client" in want.keys():
            b_val = want.get("route_server_client")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "route-server-client")

        # Generate config commands for send-addpath-optimization
        if "send_addpath_optimization" in want.keys():
            b_val = want.get("send_addpath_optimization")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "send-addpath-optimization")

        # Generate config commands for sr-preference-override
        if want.get("sr_preference_override"):
            build_child_xml_node(
                bgp_root, "sr-preference-override", want["sr_preference_override"]
            )

        # Generate config commands for stale-labels-holddown-period
        if want.get("stale_labels_holddown_period"):
            build_child_xml_node(
                bgp_root, "stale-labels-holddown-period", want["stale_labels_holddown_period"]
            )

        # Generate config commands for tcp-aggressive-transmission
        if "tcp_aggressive_transmission" in want.keys():
            b_val = want.get("tcp_aggressive_transmission")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "tcp-aggressive-transmission")

        # Generate config commands for tcp-mss
        if want.get("tcp_mss"):
            build_child_xml_node(
                bgp_root, "tcp-mss", want["tcp_mss"]
            )

        # Generate config commands for ttl
        if want.get("ttl"):
            build_child_xml_node(
                bgp_root, "ttl", want["ttl"]
            )

        # Generate config commands for unconfigured-peer-graceful-restart
        if "unconfigured_peer_graceful_restart" in want.keys():
            b_val = want.get("unconfigured_peer_graceful_restart")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "unconfigured-peer-graceful-restart")

        # Generate config commands for vpn-apply-export
        if "vpn_apply_export" in want.keys():
            b_val = want.get("vpn_apply_export")
            if b_val is not None:
                if b_val is True:
                    build_child_xml_node(bgp_root, "vpn-apply-export")
        bgp_xml.append(bgp_root)

        return bgp_xml

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        bgp_xml = []
        attrib_list = [
            "accept-remote-nexthop",
            "add-path-display-ipv4-address",
            "advertise-bgp-static",
            "advertise-external",
            "advertise-from-main-vpn-tables",
            "advertise-inactive",
            "advertise-peer-as",
            "authentication-algorithm",
            "authentication-key",
            "authentication-key-chain",
            "bfd-liveness-detection",
            "bgp-error-tolerance",
            "bmp",
            "cluster",
            "damping",
            "description",
            "disable",
            "egress-te-sid-stats",
            "enforce-first-as",
            "export",
            "forwarding-context",
            "hold-time",
            "holddown-all-stale-labels",
            "import",
            "include-mp-next-hop",
            "ipsec-sa",
            "keep",
            "local-address",
            "local-interface",
            "local-preference",
            "log-updown",
            "mtu-discovery",
            "no-advertise-peer-as",
            "no-aggregator-id",
            "no-client-reflect",
            "no-precision-timers",
            "out-delay",
            "passive",
            "peer-as",
            "precision-timers",
            "preference",
            "rfc6514-compliant-safi129",
            "route-server-client",
            "send-addpath-optimization",
            "sr-preference-override",
            "stale-labels-holddown-period",
            "tcp-aggressive-transmission",
            "tcp-mss",
            "ttl",
            "unconfigured-peer-graceful-restart",
            "vpn-apply-export",
        ]
        bgp_root = build_root_xml_node("bgp")
        for attrib in attrib_list:
            build_child_xml_node(
                bgp_root, attrib, None, {"delete": "delete"}
            )
        bgp_xml.append(bgp_root)
        return bgp_xml
