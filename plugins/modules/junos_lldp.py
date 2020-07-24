#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_lldp
author: Ganesh Nalawade (@ganeshrn)
short_description: (deprecated, removed after 2022-06-01) Manage LLDP configuration
  on Juniper JUNOS network devices
description:
- This module provides declarative management of LLDP service on Juniper JUNOS network
  devices.
version_added: 1.0.0
deprecated:
  why: Updated modules released with more functionality
  alternative: Use M(junos_lldp_global) instead.
  removed_at_date: '2022-06-01'
options:
  interval:
    description:
    - Frequency at which LLDP advertisements are sent (in seconds).
    type: int
  transmit_delay:
    description:
    - Specify the number of seconds the device waits before sending advertisements
      to neighbors after a change is made in local system.
    type: int
  hold_multiplier:
    description:
    - Specify the number of seconds that LLDP information is held before it is discarded.
      The multiplier value is used in combination with the C(interval) value.
    type: int
  state:
    description:
    - Value of C(present) ensures given LLDP configuration is present on device and
      LLDP is enabled, for value of C(absent) LLDP configuration is deleted and LLDP
      is in disabled state. Value C(enabled) ensures LLDP protocol is enabled and
      LLDP configuration if any is configured on remote device, for value of C(disabled)
      it ensures LLDP protocol is disabled any LLDP configuration if any is still
      present.
    default: present
    type: str
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
- name: Enable LLDP service
  junipernetworks.junos.junos_lldp:
    state: enabled

- name: Disable LLDP service
  junipernetworks.junos.junos_lldp:
    state: disabled

- name: Set LLDP parameters
  junipernetworks.junos.junos_lldp:
    interval: 10
    hold_multiplier: 5
    transmit_delay: 30
    state: present

- name: Delete LLDP parameters
  junipernetworks.junos.junos_lldp:
    interval: 10
    hold_multiplier: 5
    transmit_delay: 30
    state: absent
"""

RETURN = """
diff.prepared:
  description: Configuration difference before and after applying change.
  returned: when configuration is changed and diff option is enabled.
  type: str
  sample: >
        [edit]
        +  protocols {
        +      lldp {
        +          disable;
        +      }
        +  }
"""
import collections

from ansible.module_utils.basic import AnsibleModule
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
)

USE_PERSISTENT_CONNECTION = True


def validate_interval(value, module):
    if not 5 <= value <= 32768:
        module.fail_json(msg="interval must be between 5 and 32768")


def validate_hold_multiplier(value, module):
    if not 5 <= value <= 32768:
        module.fail_json(msg="hold_multiplier must be between 2 and 10")


def validate_transmit_delay(value, module):
    if not 1 <= value <= 8192:
        module.fail_json(msg="transmit_delay must be between 2 and 10")


def validate_param_values(module, obj):
    for key in obj:
        # validate the param value (if validator func exists)
        validator = globals().get("validate_%s" % key)
        if callable(validator):
            validator(module.params.get(key), module)


def main():
    """ main entry point for module execution
    """
    argument_spec = dict(
        interval=dict(type="int"),
        transmit_delay=dict(type="int"),
        hold_multiplier=dict(type="int"),
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

    top = "protocols/lldp"

    param_to_xpath_map = collections.OrderedDict()
    param_to_xpath_map.update(
        [
            (
                "interval",
                {"xpath": "advertisement-interval", "leaf_only": True},
            ),
            ("transmit_delay", {"xpath": "transmit-delay", "leaf_only": True}),
            (
                "hold_multiplier",
                {"xpath": "hold-multiplier", "leaf_only": True},
            ),
            (
                "disable",
                {"xpath": "disable", "tag_only": True, "is_key": True},
            ),
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
