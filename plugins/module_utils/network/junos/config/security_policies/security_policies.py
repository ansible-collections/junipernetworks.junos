#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_security_policies class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from lxml import etree

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
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    build_root_xml_node,
    build_child_xml_node,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.facts import (
    Facts,
)


class Security_policies(ConfigBase):
    """
    The junos_security_policies class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["security_policies"]

    def __init__(self, module):
        super(Security_policies, self).__init__(module)

    def get_security_policies_facts(self):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources
        )
        security_policies_facts = facts["ansible_network_resources"].get(
            "security_policies"
        )
        if not security_policies_facts:
            return {}
        return security_policies_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_security_policies_facts = self.get_security_policies_facts()
        else:
            existing_security_policies_facts = {}
        if self.state == "gathered":
            existing_security_policies_facts = self.get_security_policies_facts()
            result["gathered"] = existing_security_policies_facts

        elif self.state == "parsed":
            security_policies = self._module.params["security_policies"]
            if not security_policies:
                self._module.fail_json(
                    msg="value of security_policies parameter must not be empty for state parsed"
                )
            result["parsed"] = self.get_security_policies_facts(data=security_policies)

        elif self.state == "rendered":
            config_xmls = self.set_config(existing_security_policies_facts)
            if config_xmls:
                result["rendered"] = config_xmls[0]
            else:
                result["rendered"] = ""

        else:
            diff = None
            config_xmls = self.set_config(existing_security_policies_facts)
            with locked_config(self._module):
                diff = load_config(self._module, config_xmls, [])

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

            changed_security_policies_facts = self.get_security_policies_facts()

            result["before"] = existing_security_policies_facts
            if result["changed"]:
                result["after"] = changed_security_policies_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_security_policies_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_security_policies_facts
        resp = self.set_state(want, have)
        return resp

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self.root = build_root_xml_node("security")
        state = self._module.params["state"]
        if state in ("merged", "replaced", "rendered", "overridden") and not want:
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
        elif state == "merged":
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)
        for xml in config_xmls:
            self.root.append(xml)
        return tostring(self.root)

    @staticmethod
    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        security_policies_xml = []
        security_policies_xml.extend(self._state_deleted(want, have))
        security_policies_xml.extend(self._state_merged(want, have))
        return security_policies_xml

    @staticmethod
    def _state_overridden(**kwargs):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        return commands

    @staticmethod
    def _state_merged(self, want):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        security_policies_xml = []
        want = remove_empties(want)
        security_policies_node = build_root_xml_node("policies")

        def build_policies(node, policies):
            for policy in policies:
                policy_node = build_child_xml_node(node, "policy")

                build_child_xml_node(policy_node, "name", policy["name"])

                if "description" in policy:
                    build_child_xml_node(
                        policy_node, "description", policy["description"]
                    )

                if "scheduler-name" in policy:
                    build_child_xml_node(
                        policy_node, "scheduler-name", policy["scheduler_name"]
                    )

                # add match criteria node
                match_node = build_child_xml_node(policy_node, "match")
                match = policy["match"]

                for source_address in match["source_address"]:
                    if source_address == "any_ipv6":
                        build_child_xml_node(match_node, "source-address", "any-ipv6")
                    elif source_address == "any_ipv4":
                        build_child_xml_node(match_node, "source-address", "any-ipv4")
                    elif source_address == "any":
                        build_child_xml_node(match_node, "source-address", "any")
                    elif source_address == "addresses":
                        for address in source_address["addresses"]:
                            build_child_xml_node(match_node, "source-address", address)

                for destination_address in match["destination_address"]:
                    if destination_address == "any_ipv6":
                        build_child_xml_node(
                            match_node, "destination-address", "any-ipv6"
                        )
                    elif destination_address == "any_ipv4":
                        build_child_xml_node(
                            match_node, "destination-address", "any-ipv4"
                        )
                    elif destination_address == "any":
                        build_child_xml_node(match_node, "destination-address", "any")
                    elif destination_address == "addresses":
                        for address in destination_address["addresses"]:
                            build_child_xml_node(
                                match_node, "destination-address", address
                            )
                for application in match["application"]:
                    if application == "any":
                        build_child_xml_node(match_node, "application", "any")
                    elif application == "names":
                        for name in application["names"]:
                            build_child_xml_node(match_node, "application", name)

                if "source_identity" in match:
                    source_identities = match["source_identity"]
                    for source_identity in source_identities:
                        if source_identity == "any":
                            build_child_xml_node(match_node, "source-identity", "any")
                        elif source_identity == "names":
                            for name in source_identity["names"]:
                                build_child_xml_node(
                                    match_node, "source-identity", name
                                )

                # add action node
                then_node = build_child_xml_node(policy_node, "then")
                then = policy["then"]
                if "deny" in then:
                    build_child_xml_node(then_node, "deny")
                if "count" in then:
                    build_child_xml_node(then_node, "count", " ")
                if "log" in then:
                    log_node = build_child_xml_node(then_node, "log")
                    build_child_xml_node(log_node, policy["then"]["log"])
                if "reject" in then:
                    pass
                if "permit" in then:
                    permit_node = build_child_xml_node(then_node, "permit")
                    if "application_services" in then["permit"]:
                        application_services = then["permit"]["application_services"]
                        application_services_node = build_child_xml_node(
                            permit_node, "application-services"
                        )
                        if "ssl_proxy" in application_services:
                            build_child_xml_node(
                                application_services_node, "ssl-proxy", " "
                            )
                        if "uac_policy" in application_services:
                            build_child_xml_node(
                                application_services_node, "uac-policy", " "
                            )
                        if (
                            "application_traffic_control_rule_set"
                            in application_services
                        ):
                            application_traffic_control_node = build_child_xml_node(
                                application_services_node, "application-traffic-control"
                            )
                            build_child_xml_node(
                                application_traffic_control_node,
                                "rule-set",
                                application_services[
                                    "application_traffic_control_rule_set"
                                ],
                            )

        # add zone-pair policies
        if "from_zones" in want.keys():
            from_zones = want.get("from_zones")
            for from_zone in from_zones:
                for to_zone in from_zone["to_zones"]:
                    policy_node = build_child_xml_node(security_policies_node, "policy")
                    build_child_xml_node(
                        policy_node, "from-zone-name", from_zone["name"]
                    )
                    build_child_xml_node(policy_node, "to-zone-name", to_zone["name"])
                    build_policies(policy_node, to_zone["policies"])

        # add global policies
        if "global" in want.keys():
            global_node = build_child_xml_node(security_policies_node, "global")
            global_policies = want.get("global").get("policies")
            build_policies(global_node, global_policies)

        if security_policies_node is not None:
            security_policies_xml.append(security_policies_node)
        return security_policies_xml

    @staticmethod
    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        security_policies_xml = []
        security_policies_root = None
        delete = {"delete": "delete"}
        if have is not None:
            security_policies_root = build_child_xml_node(
                self.root, "security_policies", None, delete
            )

        if security_policies_root is not None:
            security_policies_xml.append(security_policies_root)
        return security_policies_xml
