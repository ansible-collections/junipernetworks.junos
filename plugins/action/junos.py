#
# (c) 2016 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.action.network import (
    ActionModule as ActionNetworkModule,
)
from ansible.utils.display import Display

display = Display()

CLI_SUPPORTED_MODULES = ["junos_netconf", "junos_ping", "junos_command"]


class ActionModule(ActionNetworkModule):
    def run(self, tmp=None, task_vars=None):
        del tmp  # tmp no longer has any effect

        module_name = self._task.action.split(".")[-1]
        self._config_module = (
            True if module_name in ["junos_config", "config"] else False
        )
        persistent_connection = self._play_context.connection.split(".")[-1]
        warnings = []

        if persistent_connection not in ("netconf", "network_cli"):
            return {
                "failed": True,
                "msg": "Connection type '%s' is not valid for '%s' module. "
                "Please see https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html"
                % (self._play_context.connection, module_name),
            }

        result = super(ActionModule, self).run(task_vars=task_vars)
        if warnings:
            if "warnings" in result:
                result["warnings"].extend(warnings)
            else:
                result["warnings"] = warnings
        return result
