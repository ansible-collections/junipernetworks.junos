#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_lldp_interface
author: Ganesh Nalawade (@ganeshrn)
short_description: (deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration
  on Juniper JUNOS network devices
description:
- This module provides declarative management of LLDP interfaces configuration on
  Juniper JUNOS network devices.
version_added: 1.0.0
deprecated:
  why: Updated modules released with more functionality
  alternative: Use M(junipernetworks.junos.junos_lldp_interfaces) instead.
  removed_at_date: '2022-06-01'
options:
  name:
    description:
    - Name of the interface LLDP should be configured on.
    type: str
  state:
    description:
    - Value of C(present) ensures given LLDP configured on given I(interfaces) and
      is enabled, for value of C(absent) LLDP configuration on given I(interfaces)
      deleted. Value C(enabled) ensures LLDP protocol is enabled on given I(interfaces)
      and for value of C(disabled) it ensures LLDP is disabled on given I(interfaces).
    type: str
    default: present
    choices:
    - present
    - absent
    - enabled
    - disabled
  active:
    description:
    - Specifies whether or not the configuration is active or deactivated
    default: true
    type: bool
requirements:
- ncclient (>=v0.5.2)
notes:
- This module requires the netconf system service be enabled on the remote device
  being managed.
- Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
- Recommended connection is C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- This module also works with C(local) connections for legacy playbooks.
extends_documentation_fragment:
- junipernetworks.junos.junos
"""

EXAMPLES = """
- name: Configure LLDP on specific interfaces
  junipernetworks.junos.junos_lldp_interface:
    name: ge-0/0/5
    state: present

- name: Disable LLDP on specific interfaces
  junipernetworks.junos.junos_lldp_interface:
    name: ge-0/0/5
    state: disabled

- name: Enable LLDP on specific interfaces
  junipernetworks.junos.junos_lldp_interface:
    name: ge-0/0/5
    state: enabled

- name: Delete LLDP configuration on specific interfaces
  junipernetworks.junos.junos_lldp_interface:
    name: ge-0/0/5
    state: present

- name: Deactivate LLDP on specific interfaces
  junipernetworks.junos.junos_lldp_interface:
    name: ge-0/0/5
    state: present
    active: false

- name: Activate LLDP on specific interfaces
  junipernetworks.junos.junos_lldp_interface:
    name: ge-0/0/5
    state: present
    active: true
"""

RETURN = """
diff.prepared:
  description: Configuration difference before and after applying change.
  returned: when configuration is changed and diff option is enabled.
  type: str
  sample: >
        [edit protocols lldp]
        +    interface ge-0/0/5;
"""
import collections

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    junos_argument_spec,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    load_config,
    map_params_to_obj,
    map_obj_to_ele,
    tostring,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    commit_configuration,
    discard_changes,
    locked_config,
)

USE_PERSISTENT_CONNECTION = True


def main():
    """main entry point for module execution"""
    argument_spec = dict(
        name=dict(),
        state=dict(
            default="present",
            choices=["present", "absent", "enabled", "disabled"],
        ),
        active=dict(default=True, type="bool"),
    )

    argument_spec.update(junos_argument_spec)

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True
    )

    warnings = list()
    result = {"changed": False}

    if warnings:
        result["warnings"] = warnings

    top = "protocols/lldp/interface"

    param_to_xpath_map = collections.OrderedDict()
    param_to_xpath_map.update(
        [
            ("name", {"xpath": "name", "is_key": True}),
            ("disable", {"xpath": "disable", "tag_only": True}),
        ]
    )

    item = module.params.copy()
    state = item.get("state")
    item["disable"] = True if state in ("disabled", "absent") else False

    if state in ("enabled", "disabled"):
        item["state"] = "present"

    want = map_params_to_obj(module, param_to_xpath_map, param=item)
    ele = map_obj_to_ele(module, want, top, param=item)

    with locked_config(module):
        diff = load_config(module, tostring(ele), warnings, action="merge")

        commit = not module.check_mode
        if diff:
            if commit:
                commit_configuration(module)
            else:
                discard_changes(module)
            result["changed"] = True

            if module._diff:
                result["diff"] = {"prepared": diff}

    module.exit_json(**result)


if __name__ == "__main__":
    main()
