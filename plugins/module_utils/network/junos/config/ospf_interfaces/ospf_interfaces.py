#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_ospf_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type


from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    remove_empties,
    to_list,
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

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.facts import Facts

import q

class Ospf_interfaces(ConfigBase):
    """
    The junos_ospf_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ospf_interfaces',
    ]

    def __init__(self, module):
        super(Ospf_interfaces, self).__init__(module)

    def get_ospf_interfaces_facts(self, data=None):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources, data=data
        )
        ospf_interfaces_facts = facts["ansible_network_resources"].get("junos_ospf_interfaces")
        if not ospf_interfaces_facts:
            return []
        return ospf_interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        state = self._module.params["state"]
        warnings = list()

        if self.state in self.ACTION_STATES:
            existing_ospf_interfaces_facts = self.get_ospf_interfaces_facts()
        else:
            existing_ospf_interfaces_facts = []
        if state == "gathered":
            existing_ospf_interfaces_facts = self.get_ospf_interfaces_facts()
            result["gathered"] = existing_ospf_interfaces_facts
        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed"
                )
            result["parsed"] = self.get_ospf_interfaces_facts(data=running_config)
        elif self.state == "rendered":
            config_xmls = self.set_config(existing_ospf_interfaces_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            config_xmls = self.set_config(existing_ospf_interfaces_facts)
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

            changed_ospf_interfaces_facts = self.get_ospf_interfaces_facts()

            result["before"] = existing_ospf_interfaces_facts
            if result["changed"]:
                result["after"] = changed_ospf_interfaces_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_ospf_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_ospf_interfaces_facts
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
        ospf_interfaces_xml = []
        ospf_interfaces_xml.extend(self._state_deleted(want, have))
        ospf_interfaces_xml.extend(self._state_merged(want, have))
        return ospf_interfaces_xml

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        ospf_interfaces_xml = []
        ospf_interfaces_xml.extend(self._state_deleted(None, have))
        ospf_interfaces_xml.extend(self._state_merged(want, have))
        return ospf_interfaces_xml

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        ospf_interfaces_xml = []
        delete = {"delete": "delete"}

        if not want:
            ospf_interfacesnode = build_child_xml_node(self.protocols, "ospf")
            ospf_interfacesnode.attrib.update(delete)
            if have:
                router_id = have[0].get("router_id")
                if router_id:
                    build_child_xml_node(
                        self.routing_options,
                        "router-id",
                        self.router_id,
                        attrib=delete,
                    )
            return ospf_interfacesnode

        ospf_interfaces_xml = self._state_merged(want, have, delete=delete)
        return ospf_interfaces_xml

    def _state_merged(self, want, have, delete=None):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        ospf_interfaces_xml = []
        q(want)
        q(have)
        protocol = build_root_xml_node("ospf")
        for ospf_interfaces in want:
            ospf_interfaces = remove_empties(ospf_interfaces)
            self.router_id = ospf_interfaces.get("router_id")
            build_child_xml_node(
                self.routing_options, "router-id", self.router_id
            )

            if ospf_interfaces.get("spf_options"):
                spf_options_node = build_child_xml_node(
                    protocol, "spf-options"
                )
                if delete and not ospf_interfaces.get("spf_options").values():
                    spf_options_node.attrib.update(delete)

                if ospf_interfaces["spf_options"].get("delay"):
                    delay_node = build_child_xml_node(
                        spf_options_node,
                        "delay",
                        ospf_interfaces["spf_options"].get("delay"),
                    )
                    if delete:
                        delay_node.attrib.update(delete)

                if ospf_interfaces["spf_options"].get("holddown"):
                    holddown_node = build_child_xml_node(
                        spf_options_node,
                        "holddown",
                        ospf_interfaces["spf_options"].get("holddown"),
                    )
                    if delete:
                        holddown_node.attrib.update(delete)

                if ospf_interfaces["spf_options"].get("delay"):
                    delay_node = build_child_xml_node(
                        spf_options_node,
                        "rapid-runs",
                        ospf_interfaces["spf_options"].get("rapid_runs"),
                    )
                    if delete:
                        delay_node.attrib.update(delete)

            if ospf_interfaces.get("overload"):
                overload_node = build_child_xml_node(protocol, "overload")
                if ospf_interfaces["overload"].get("timeout"):
                    build_child_xml_node(
                        overload_node,
                        "timeout",
                        ospf_interfaces["overload"].get("timeout"),
                    )
                if delete:
                    overload_node.attrib.update(delete)

            if ospf_interfaces.get("external_preference"):
                ext_pref_node = build_child_xml_node(
                    protocol,
                    "external-preference",
                    ospf_interfaces["externall_preference"],
                )
                if delete:
                    ext_pref_node.attrib.update(delete)

            if ospf_interfaces.get("preference"):
                pref_node = build_child_xml_node(
                    protocol, "preference", ospf_interfaces["preference"]
                )
                if delete:
                    pref_node.attrib.update(delete)

            if ospf_interfaces.get("prefix_export_limit"):
                prefix_export_node = build_child_xml_node(
                    protocol,
                    "prefix-export-limit",
                    ospf_interfaces["prefix_export_limit"],
                )
                if delete:
                    prefix_export_node.attrib.update(delete)

            if ospf_interfaces.get("reference_bandwidth"):
                ref_bw_node = build_child_xml_node(
                    protocol,
                    "reference-bandwidth",
                    ospf_interfaces.get("reference_bandwidth"),
                )
                if delete:
                    ref_bw_node.attrib.update(delete)

            if "rfc1583compatibility" in ospf_interfaces.keys():
                if not ospf_interfaces["rfc1583compatibility"]:
                    build_child_xml_node(protocol, "no-rfc-1583")
            q(ospf_interfaces)
            for af in ospf_interfaces["address_family"]:
                area_node = build_child_xml_node(protocol, "area")
                processes = af.get("processes")
                area = processes.get("area")
                area_id = area.get("area_id")
                build_child_xml_node(area_node, "name", area_id)

                intf_node = build_child_xml_node(area_node, "interface")
                build_child_xml_node(intf_node, "name", ospf_interfaces.get("name"))
                if delete:
                    if have:
                        existing_config = have[0]
                        for existing_area in existing_config["areas"]:
                            if existing_area["area_id"] == area_id:
                                if len(existing_area["interfaces"]) == 1:
                                    area_node.attrib.update(delete)
                                else:
                                   intf_node.attrib.update(delete)

                if processes.get("priority"):
                    build_child_xml_node(
                        intf_node, "priority", processes.get("priority")
                    )

                if processes.get("flood_reduction"):
                    build_child_xml_node(intf_node, "flood-reduction")

                if processes.get("metric"):
                    build_child_xml_node(
                        intf_node, "metric", processes["metric"]
                    )

                if processes.get("passive"):
                    build_child_xml_node(intf_node, "passive")

                if processes.get("bandwidth_based_metrics"):
                    bw_metrics_node = build_child_xml_node(
                        intf_node, "bandwidth-based-metrics"
                    )
                    bw_metrics = processes.get("bandwidth_based_metrics")
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
                if processes.get("dead_interval"):
                    build_child_xml_node(intf_node, "dead-interval", processes.get("dead_interval"),)
                if processes.get("hello_interval"):
                    build_child_xml_node(intf_node, "hello-interval", processes.get("hello_interval"),)
                if processes.get("poll_interval"):
                    build_child_xml_node(intf_node, "poll-interval", processes.get("poll_interval"),)
                if processes.get("retransmit_interval"):
                    build_child_xml_node(intf_node, "retransmit-interval", processes.get("retransmit_interval"),)

        ospf_interfaces_xml.append(protocol)
        q(ospf_interfaces_xml)
        return ospf_interfaces_xml
