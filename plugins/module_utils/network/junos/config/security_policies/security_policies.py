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
            return []
        return security_policies_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        state = self._module.params["state"]
        result = {"changed": False}

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_security_policies_facts = self.get_security_policies_facts()
        else:
            existing_security_policies_facts = {}
        if state == "gathered":
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
                for config_xml in config_xmls:
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
        return to_list(resp)

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        state = self._module.params["state"]
        if state == "overridden":
            kwargs = {}
            commands = self._state_overridden(**kwargs)
        elif state == "deleted":
            kwargs = {}
            commands = self._state_deleted(**kwargs)
        elif state == "merged":
            kwargs = {}
            commands = self._state_merged(**kwargs)
        elif state == "replaced":
            kwargs = {}
            commands = self._state_replaced(**kwargs)
        return commands

    @staticmethod
    def _state_gathered(**kwargs):
        """The command generator when state is gathered

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        return commands

    @staticmethod
    def _state_replaced(**kwargs):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        return commands

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
    def _state_merged(**kwargs):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        return commands

    @staticmethod
    def _state_deleted(**kwargs):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []
        return commands
