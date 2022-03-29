#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_l3_interface
author: Ganesh Nalawade (@ganeshrn)
short_description: (deprecated, removed after 2022-06-01) Manage L3 interfaces on
  Juniper JUNOS network devices
description:
- This module provides declarative management of L3 interfaces on Juniper JUNOS network
  devices.
version_added: 1.0.0
deprecated:
  why: Updated modules released with more functionality
  alternative: Use M(junipernetworks.junos.junos_l3_interfaces) instead.
  removed_at_date: '2022-06-01'
options:
  name:
    description:
    - Name of the L3 interface.
    type: str
  ipv4:
    description:
    - IPv4 of the L3 interface.
    type: str
  ipv6:
    description:
    - IPv6 of the L3 interface.
    type: str
  unit:
    description:
    - Logical interface number.
    type: int
    default: 0
  filter_input:
    description:
    - The name of input filter.
    type: str
  filter_output:
    description:
    - The name of output filter.
    type: str
  filter6_input:
    description:
    - The name of input filter for ipv6.
    type: str
  filter6_output:
    description:
    - The name of output filter for ipv6.
    type: str
  aggregate:
    description: List of L3 interfaces definitions
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the L3 interface.
        required: true
        type: str
      ipv4:
        description:
        - IPv4 of the L3 interface.
        type: str
      ipv6:
        description:
        - IPv6 of the L3 interface.
        type: str
      unit:
        description:
        - Logical interface number.
        type: int
        default: 0
      filter_input:
        description:
        - The name of input filter.
        type: str
      filter_output:
        description:
        - The name of output filter.
        type: str
      filter6_input:
        description:
        - The name of input filter for ipv6.
        type: str
      filter6_output:
        description:
        - The name of output filter for ipv6.
        type: str
      state:
        description:
        - State of the L3 interface configuration.
        type: str
        choices:
        - present
        - absent
      active:
        description:
        - Specifies whether or not the configuration is active or deactivated
        type: bool
  state:
    description:
    - State of the L3 interface configuration.
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
- Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
- Recommended connection is C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- This module also works with C(local) connections for legacy playbooks.
extends_documentation_fragment:
- junipernetworks.junos.junos
"""

EXAMPLES = """
- name: Set ge-0/0/1 IPv4 address
  junipernetworks.junos.junos_l3_interface:
    name: ge-0/0/1
    ipv4: 192.168.0.1

- name: Remove ge-0/0/1 IPv4 address
  junipernetworks.junos.junos_l3_interface:
    name: ge-0/0/1
    state: absent

- name: Set ipv4 address using aggregate
  junipernetworks.junos.junos_l3_interface:
    aggregate:
    - name: ge-0/0/1
      ipv4: 192.0.2.1
    - name: ge-0/0/2
      ipv4: 192.0.2.2
      ipv6: fd5d:12c9:2201:2::2

- name: Delete ipv4 address using aggregate
  junipernetworks.junos.junos_l3_interface:
    aggregate:
    - name: ge-0/0/1
      ipv4: 192.0.2.1
    - name: ge-0/0/2
      ipv4: 192.0.2.2
    state: absent
"""

RETURN = """
diff:
  description: Configuration difference before and after applying change.
  returned: when configuration is changed and diff option is enabled.
  type: str
  sample: >
        [edit interfaces ge-0/0/1 unit 0 family inet]
        +       address 192.0.2.1/32;
        [edit interfaces ge-0/0/1 unit 0 family inet6]
        +       address fd5d:12c9:2201:1::1/128;
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


def main():
    """main entry point for module execution"""
    element_spec = dict(
        name=dict(),
        ipv4=dict(),
        ipv6=dict(),
        filter_input=dict(),
        filter_output=dict(),
        filter6_input=dict(),
        filter6_output=dict(),
        unit=dict(default=0, type="int"),
        state=dict(
            type="str", default="present", choices=["present", "absent"]
        ),
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
    mutually_exclusive = [["name", "aggregate"]]

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
        required_one_of=required_one_of,
    )

    warnings = list()
    result = {"changed": False}

    if warnings:
        result["warnings"] = warnings

    top = "interfaces/interface"

    param_to_xpath_map = collections.OrderedDict()
    param_to_xpath_map.update(
        [
            (
                "name",
                {"xpath": "name", "parent_attrib": False, "is_key": True},
            ),
            (
                "unit",
                {
                    "xpath": "name",
                    "top": "unit",
                    "parent_attrib": False,
                    "is_key": True,
                },
            ),
            (
                "ipv4",
                {
                    "xpath": "inet/address/name",
                    "top": "unit/family",
                    "is_key": True,
                },
            ),
            (
                "ipv6",
                {
                    "xpath": "inet6/address/name",
                    "top": "unit/family",
                    "is_key": True,
                },
            ),
            (
                "filter_input",
                {"xpath": "inet/filter/input", "top": "unit/family"},
            ),
            (
                "filter_output",
                {"xpath": "inet/filter/output", "top": "unit/family"},
            ),
            (
                "filter6_input",
                {"xpath": "inet6/filter/input", "top": "unit/family"},
            ),
            (
                "filter6_output",
                {"xpath": "inet6/filter/output", "top": "unit/family"},
            ),
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
        if not item["ipv4"] and not item["ipv6"]:
            module.fail_json(msg="one of the following is required: ipv4,ipv6")

        want = map_params_to_obj(module, param_to_xpath_map, param=item)
        requests.append(map_obj_to_ele(module, want, top, param=item))

    diff = None
    with locked_config(module):
        for req in requests:
            diff = load_config(module, tostring(req), warnings, action="merge")

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
