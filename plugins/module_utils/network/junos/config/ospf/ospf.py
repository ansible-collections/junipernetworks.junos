#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_ospf class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.facts import (
    Facts,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    locked_config,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    build_root_xml_node,
    build_child_xml_node,
)


class Ospf(ConfigBase):
    """
    The junos_ospf class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["ospf"]

    def __init__(self, module):
        super(Ospf, self).__init__(module)

    def get_ospf_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources
        )
        ospf_facts = facts["ansible_network_resources"].get("ospf")
        if not ospf_facts:
            return []
        return ospf_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        warnings = list()

        existing_ospf_facts = self.get_ospf_facts()
        config_xmls = self.set_config(existing_ospf_facts)

        with locked_config(self._module):
            for config_xml in to_list(config_xmls):
                diff = self._module._connectionload_config(
                    self._module, config_xml, []
                )

            commit = not self._module.check_mode
            if diff:
                if commit:
                    self._module._connection.commit_configuration(self._module)
                else:
                    self._module._connection.discard_changes(self._module)
                result["changed"] = True

                if self._module._diff:
                    result["diff"] = {"prepared": diff}

        result["xml"] = config_xmls
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
        root = build_root_xml_node("ospf")
        state = self._module.params["state"]
        if state == "overridden":
            config_xmls = self._state_overridden(want, have)
        elif state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state == "merged":
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)

        for xml in config_xmls:
            root.append(xml)

        return self._module._connection.tostring(root)

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        return intf_xml

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        return intf_xml

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        return intf_xml

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        return intf_xml
