#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_l2_interface
author: Ganesh Nalawade (@ganeshrn)
short_description: (deprecated, removed after 2022-06-01) Manage L2 Interface on Juniper
  JUNOS network devices
description:
- This module provides declarative management of Layer-2 interface on Juniper JUNOS
  network devices.
version_added: 1.0.0
deprecated:
  why: Updated modules released with more functionality
  alternative: Use M(junipernetworks.junos.junos_l2_interfaces) instead.
  removed_at_date: '2022-06-01'
options:
  name:
    description:
    - Name of the interface excluding any logical unit number.
    type: str
  description:
    description:
    - Description of Interface.
    type: str
  aggregate:
    description:
    - List of Layer-2 interface definitions.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the interface excluding any logical unit number.
        type: str
        required: true
      description:
        description:
        - Description of Interface.
        type: str
      mode:
        description:
        - Mode in which interface needs to be configured.
        choices:
        - access
        - trunk
        type: str
      access_vlan:
        description:
        - Configure given VLAN in access port. The value of C(access_vlan) should be vlan
          name.
        type: str
      trunk_vlans:
        description:
        - List of VLAN names to be configured in trunk port. The value of C(trunk_vlans)
          should be list of vlan names.
        type: list
        elements: str
      native_vlan:
        description:
        - Native VLAN to be configured in trunk port. The value of C(native_vlan) should
          be vlan id.
        type: int
      enhanced_layer:
        description:
        - True if your device has Enhanced Layer 2 Software (ELS).
        type: bool
      unit:
        description:
        - Logical interface number. Value of C(unit) should be of type integer.
        type: int
      filter_input:
        description:
        - The name of input filter of ethernet-switching.
        type: str
      filter_output:
        description:
        - The name of output filter of ethernet-switching.
        type: str
      state:
        description:
        - State of the Layer-2 Interface configuration.
        type: str
        choices:
        - present
        - absent
      active:
        description:
        - Specifies whether or not the configuration is active or deactivated
        type: bool
  mode:
    description:
    - Mode in which interface needs to be configured.
    choices:
    - access
    - trunk
    type: str
  access_vlan:
    description:
    - Configure given VLAN in access port. The value of C(access_vlan) should be vlan
      name.
    type: str
  trunk_vlans:
    description:
    - List of VLAN names to be configured in trunk port. The value of C(trunk_vlans)
      should be list of vlan names.
    type: list
    elements: str
  native_vlan:
    description:
    - Native VLAN to be configured in trunk port. The value of C(native_vlan) should
      be vlan id.
    type: int
  enhanced_layer:
    description:
    - True if your device has Enhanced Layer 2 Software (ELS).
    default: true
    type: bool
  unit:
    description:
    - Logical interface number. Value of C(unit) should be of type integer.
    default: 0
    type: int
  filter_input:
    description:
    - The name of input filter of ethernet-switching.
    type: str
  filter_output:
    description:
    - The name of output filter of ethernet-switching.
    type: str
  state:
    description:
    - State of the Layer-2 Interface configuration.
    type: str
    default: present
    choices:
    - present
    - absent
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
- Tested against vqfx-10000 JUNOS Version 15.1X53-D60.4.
- Recommended connection is C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- This module also works with C(local) connections for legacy playbooks.
extends_documentation_fragment:
- junipernetworks.junos.junos
"""

EXAMPLES = """
- name: Configure interface in access mode
  junipernetworks.junos.junos_l2_interface:
    name: ge-0/0/1
    description: interface-access
    mode: access
    access_vlan: red
    active: true
    state: present

- name: Configure interface in trunk mode
  junipernetworks.junos.junos_l2_interface:
    name: ge-0/0/1
    description: interface-trunk
    mode: trunk
    trunk_vlans:
    - blue
    - green
    native_vlan: 100
    active: true
    state: present

- name: Configure interface in access and trunk mode using aggregate
  junipernetworks.junos.junos_l2_interface:
    aggregate:
    - name: ge-0/0/1
      description: test-interface-access
      mode: access
      access_vlan: red
    - name: ge-0/0/2
      description: test-interface-trunk
      mode: trunk
      trunk_vlans:
      - blue
      - green
      native_vlan: 100
    active: true
    state: present
"""

RETURN = """
diff:
  description: Configuration difference before and after applying change.
  returned: when configuration is changed and diff option is enabled.
  type: str
  sample: >
        [edit interfaces]
        +   ge-0/0/1 {
        +       description "l2 interface configured by Ansible";
        +       unit 0 {
        +           family ethernet-switching {
        +               interface-mode access;
        +               vlan {
        +                   members red;
        +               }
        +           }
        +       }
        +   }
"""
import collections

from copy import deepcopy

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    remove_default_spec,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    junos_argument_spec,
    tostring,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    load_config,
    map_params_to_obj,
    map_obj_to_ele,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos import (
    commit_configuration,
    discard_changes,
    locked_config,
    to_param_list,
)

USE_PERSISTENT_CONNECTION = True


def validate_vlan_id(value, module):
    if value and not 0 <= value <= 4094:
        module.fail_json(msg="vlan_id must be between 1 and 4094")


def validate_param_values(module, obj, param=None):
    if not param:
        param = module.params
    for key in obj:
        # validate the param value (if validator func exists)
        validator = globals().get("validate_%s" % key)
        if callable(validator):
            validator(param.get(key), module)


def main():
    """main entry point for module execution"""
    element_spec = dict(
        name=dict(),
        mode=dict(choices=["access", "trunk"]),
        access_vlan=dict(),
        native_vlan=dict(type="int"),
        trunk_vlans=dict(type="list", elements="str"),
        unit=dict(default=0, type="int"),
        filter_input=dict(),
        filter_output=dict(),
        description=dict(),
        enhanced_layer=dict(default=True, type="bool"),
        state=dict(default="present", choices=["present", "absent"]),
        active=dict(default=True, type="bool"),
    )

    aggregate_spec = deepcopy(element_spec)
    aggregate_spec["name"] = dict(required=True)

    # remove default in aggregate spec, to handle common arguments
    remove_default_spec(aggregate_spec)

    argument_spec = dict(
        aggregate=dict(type="list", elements="dict", options=aggregate_spec)
    )

    argument_spec.update(element_spec)
    argument_spec.update(junos_argument_spec)

    required_one_of = [["name", "aggregate"]]
    mutually_exclusive = [
        ["name", "aggregate"],
        ["access_vlan", "trunk_vlans"],
        ["access_vlan", "native_vlan"],
    ]

    required_if = [
        ("mode", "access", ("access_vlan",)),
        ("mode", "trunk", ("trunk_vlans",)),
    ]

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
        required_one_of=required_one_of,
        required_if=required_if,
    )

    warnings = list()
    result = {"changed": False}

    if warnings:
        result["warnings"] = warnings

    top = "interfaces/interface"

    param_to_xpath_map = collections.OrderedDict()
    param_to_xpath_map.update(
        [
            ("name", {"xpath": "name", "is_key": True}),
            ("unit", {"xpath": "name", "top": "unit", "is_key": True}),
            (
                "mode",
                {
                    "xpath": "interface-mode",
                    "top": "unit/family/ethernet-switching",
                },
            ),
            (
                "access_vlan",
                {
                    "xpath": "members",
                    "top": "unit/family/ethernet-switching/vlan",
                },
            ),
            (
                "trunk_vlans",
                {
                    "xpath": "members",
                    "top": "unit/family/ethernet-switching/vlan",
                },
            ),
            (
                "filter_input",
                {
                    "xpath": "input",
                    "top": "unit/family/ethernet-switching/filter",
                },
            ),
            (
                "filter_output",
                {
                    "xpath": "output",
                    "top": "unit/family/ethernet-switching/filter",
                },
            ),
            ("native_vlan", {"xpath": "native-vlan-id"}),
            ("description", "description"),
        ]
    )

    params = to_param_list(module)

    requests = list()
    for param in params:
        # if key doesn't exist in the item, get it from module.params
        for key in param:
            if param.get(key) is None:
                param[key] = module.params[key]

        item = param.copy()

        validate_param_values(module, param_to_xpath_map, param=item)

        param_to_xpath_map["mode"]["xpath"] = (
            "interface-mode" if param["enhanced_layer"] else "port-mode"
        )

        want = map_params_to_obj(module, param_to_xpath_map, param=item)
        requests.append(map_obj_to_ele(module, want, top, param=item))

    diff = None
    with locked_config(module):
        for req in requests:
            diff = load_config(
                module, tostring(req), warnings, action="replace"
            )

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
