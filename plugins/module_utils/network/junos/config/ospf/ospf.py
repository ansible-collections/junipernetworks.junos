# Copyright (C) 2020  Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
The junos_ospfv2 class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    remove_empties,
    to_list,
)

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.facts import (
    Facts,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    locked_config,
    load_config,
    commit_configuration,
    discard_changes,
    tostring,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    build_root_xml_node,
    build_child_xml_node,
)


class Ospf(ConfigBase):
    """
    The junos_ospfv2 class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["ospf"]

    def __init__(self, module):
        super(Ospf, self).__init__(module)

    def get_ospf_facts(self, data=None):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources, data=data
        )
        ospf_facts = facts["ansible_network_resources"].get("junos_ospfv2")
        if not ospf_facts:
            return []
        return ospf_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]
        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_ospf_facts = self.get_ospf_facts()
        else:
            existing_ospf_facts = []
        if state == "gathered":
            existing_ospf_facts = self.get_ospf_facts()
            result["gathered"] = existing_ospf_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed"
                )
            result["parsed"] = self.get_ospf_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_ospf_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_ospf_facts)
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

            changed_ospf_facts = self.get_ospf_facts()

            result["before"] = existing_ospf_facts
            if result["changed"]:
                result["after"] = changed_ospf_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_ospf_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_ospf_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self.router_id = None
        self.root = build_root_xml_node("configuration")
        self.protocols = build_child_xml_node(self.root, "protocols")
        self.routing_options = build_child_xml_node(
            self.root, "routing-options"
        )
        state = self._module.params["state"]
        if (
            state in ("merged", "replaced", "overridden", "rendered")
            and not want
        ):
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state
                )
            )
        config_xmls = []
        if state == "overridden":
            config_xmls = self._state_overridden(want, have)
        elif state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state in ("merged", "rendered"):
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)

        for xml in config_xmls:
            self.protocols.append(xml)

        return [tostring(xml) for xml in self.root.getchildren()]

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        ospf_xml = []
        ospf_xml.extend(self._state_deleted(want, have))
        ospf_xml.extend(self._state_merged(want, have))
        return ospf_xml

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        ospf_xml = []
        ospf_xml.extend(self._state_deleted(None, have))
        ospf_xml.extend(self._state_merged(want, have))
        return ospf_xml

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        ospf_xml = []
        delete = {"delete": "delete"}

        if not want:
            ospf_node = build_child_xml_node(self.protocols, "ospf")
            ospf_node.attrib.update(delete)
            if have:
                router_id = have[0].get("router_id")
                if router_id:
                    build_child_xml_node(
                        self.routing_options,
                        "router-id",
                        self.router_id,
                        attrib=delete,
                    )
            return ospf_node

        ospf_xml = self._state_merged(want, have, delete=delete)
        return ospf_xml

    def _state_merged(self, want, have, delete=None):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        ospf_xml = []
        protocol = build_root_xml_node("ospf")
        for ospf in want:
            ospf = remove_empties(ospf)
            self.router_id = ospf.get("router_id")
            build_child_xml_node(
                self.routing_options, "router-id", self.router_id
            )

            if ospf.get("spf_options"):
                spf_options_node = build_child_xml_node(
                    protocol, "spf-options"
                )
                if delete and not ospf.get("spf_options").values():
                    spf_options_node.attrib.update(delete)

                if ospf["spf_options"].get("delay"):
                    delay_node = build_child_xml_node(
                        spf_options_node,
                        "delay",
                        ospf["spf_options"].get("delay"),
                    )
                    if delete:
                        delay_node.attrib.update(delete)

                if ospf["spf_options"].get("holddown"):
                    holddown_node = build_child_xml_node(
                        spf_options_node,
                        "holddown",
                        ospf["spf_options"].get("holddown"),
                    )
                    if delete:
                        holddown_node.attrib.update(delete)

                if ospf["spf_options"].get("delay"):
                    delay_node = build_child_xml_node(
                        spf_options_node,
                        "rapid-runs",
                        ospf["spf_options"].get("rapid_runs"),
                    )
                    if delete:
                        delay_node.attrib.update(delete)

            if ospf.get("overload"):
                overload_node = build_child_xml_node(protocol, "overload")
                if ospf["overload"].get("timeout"):
                    build_child_xml_node(
                        overload_node,
                        "timeout",
                        ospf["overload"].get("timeout"),
                    )
                if delete:
                    overload_node.attrib.update(delete)

            if ospf.get("external_preference"):
                ext_pref_node = build_child_xml_node(
                    protocol,
                    "external-preference",
                    ospf["externall_preference"],
                )
                if delete:
                    ext_pref_node.attrib.update(delete)

            if ospf.get("preference"):
                pref_node = build_child_xml_node(
                    protocol, "preference", ospf["preference"]
                )
                if delete:
                    pref_node.attrib.update(delete)

            if ospf.get("prefix_export_limit"):
                prefix_export_node = build_child_xml_node(
                    protocol,
                    "prefix-export-limit",
                    ospf["prefix_export_limit"],
                )
                if delete:
                    prefix_export_node.attrib.update(delete)

            if ospf.get("reference_bandwidth"):
                ref_bw_node = build_child_xml_node(
                    protocol,
                    "reference-bandwidth",
                    ospf.get("reference_bandwidth"),
                )
                if delete:
                    ref_bw_node.attrib.update(delete)

            if "rfc1583compatibility" in ospf.keys():
                if not ospf["rfc1583compatibility"]:
                    build_child_xml_node(protocol, "no-rfc-1583")

            for area in ospf["areas"]:
                area_node = build_child_xml_node(protocol, "area")
                area_id = area.get("area_id")
                build_child_xml_node(area_node, "name", area_id)
                if area.get("area_range"):
                    area_range_node = build_child_xml_node(
                        area_node, "area-range"
                    )
                    build_child_xml_node(
                        area_range_node, "name", area["area_range"]
                    )
                    if delete:
                        area_range_node.attrib.update(delete)

                for intf in area.get("interfaces"):
                    intf_node = build_child_xml_node(area_node, "interface")
                    build_child_xml_node(intf_node, "name", intf.get("name"))
                    if delete:
                        if have:
                            existing_config = have[0]
                            for existing_area in existing_config["areas"]:
                                if existing_area["area_id"] == area_id:
                                    if len(existing_area["interfaces"]) == 1:
                                        area_node.attrib.update(delete)
                                    else:
                                        intf_node.attrib.update(delete)

                    if intf.get("priority"):
                        build_child_xml_node(
                            intf_node, "priority", intf.get("priority")
                        )

                    if intf.get("flood_reduction"):
                        build_child_xml_node(intf_node, "flood-reduction")

                    if intf.get("metric"):
                        build_child_xml_node(
                            intf_node, "metric", intf["metric"]
                        )

                    if intf.get("passive"):
                        build_child_xml_node(intf_node, "passive")

                    if intf.get("bandwidth_based_metrics"):
                        bw_metrics_node = build_child_xml_node(
                            intf_node, "bandwidth-based-metrics"
                        )
                        bw_metrics = intf.get("bandwidth_based_metrics")
                        for bw_metric in bw_metrics:
                            bw_metric_node = build_child_xml_node(
                                bw_metrics_node, "bandwidth"
                            )
                            build_child_xml_node(
                                bw_metric_node,
                                "name",
                                bw_metric.get("bandwidth"),
                            )
                            build_child_xml_node(
                                bw_metric_node,
                                "metric",
                                bw_metric.get("metric"),
                            )
                    if intf.get("timers"):
                        if intf["timers"].get("dead_interval"):
                            build_child_xml_node(
                                intf_node,
                                "dead-interval",
                                intf["timers"].get("dead_interval"),
                            )
                        if intf["timers"].get("hello_interval"):
                            build_child_xml_node(
                                intf_node,
                                "hello-interval",
                                intf["timers"].get("hello_interval"),
                            )
                        if intf["timers"].get("poll_interval"):
                            build_child_xml_node(
                                intf_node,
                                "poll-interval",
                                intf["timers"].get("poll_interval"),
                            )
                        if intf["timers"].get("retransmit_interval"):
                            build_child_xml_node(
                                intf_node,
                                "retransmit-interval",
                                intf["timers"].get("retransmit_interval"),
                            )

                if area.get("stub"):
                    if area["stub"]["set"]:
                        stub_node = build_child_xml_node(area_node, "stub")
                        if area["stub"].get("default_metric"):
                            build_child_xml_node(
                                stub_node,
                                "default-metric",
                                area["stub"].get("default_metric"),
                            )
        ospf_xml.append(protocol)
        return ospf_xml
