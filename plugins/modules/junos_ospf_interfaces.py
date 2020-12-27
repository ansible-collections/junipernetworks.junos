#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for junos_ospf_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """
---
module: junos_ospf_interfaces
version_added: 1.0.0
short_description:  OSPF Interfaces Resource Module.
description:
  - This module manages OSPF(v2/v3) configuration of interfaces on devices running Juniper JUNOS.
author: Rohit Thakur (@rohitthakur2590)
requirements:
  - ncclient (>=v0.6.4)
  - xmltodict (>=0.12.0)
notes:
  - This module requires the netconf system service be enabled on the device being managed.
  - This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
  - Tested against JunOS v18.4R1
options:
  config:
    description: A list of OSPF configuration for interfaces.
    type: list
    elements: dict
    suboptions:
      router_id:
        description:
        - The OSPFv3 router id.
        type: str
        required: true
      name:
        description:
          - Name/Identifier of the interface.
        type: str
        required: True
      address_family:
        description:
          - OSPF settings on the interfaces in address-family context.
        type: list
        elements: dict
        suboptions:
          afi:
            description:
              - Address Family Identifier (AFI) for OSPF settings on the interfaces.
            type: str
            choices: ['ipv4', 'ipv6']
            required: True
          processes:
            description:
              - Interfaces configuration for an OSPF process.
            type: dict
            suboptions:
              area:
                description: Specify the area-id
                type: dict
                suboptions:
                  area_id:
                    description: Specify area id.
                    type: str
              authentication:
                description: Specify authentication type
                type: dict
                suboptions:
                  simple_password:
                    description:
                      - Specify password for authentication.
                    type: str
                  md5:
                    description:
                      - Specify md5 based authentication.
                    type: dict
                    suboptions:
                      key_id:
                        description: Specify md5 key-id
                        type: str
                      key_value:
                        description: Specify key value
                        type: str
                      start_time:
                        description: Specify start time for key transmission
                        type: str
              interface_type:
                description: Specify type of interface
                type: str
                choices: ["nbma", "p2mp", "p2p"]
              bandwidth_based_metrics:
                description: Specify list of bandwidth based metrics
                type: list
                elements: dict
                suboptions:
                  bandwidth:
                    description:
                      - BW to apply metric to.
                    type: str
                    choices: [1g, 10g]
                  metric:
                    description: Specify metric
                    type: int
              priority:
                description:
                  - Priority for the interface.
                type: int
              metric:
                description:
                  - Metric applied to the interface.
                type: int
              te_metric:
                description:
                  - Traffic engineering metric applied to the interface.
                type: int
              mtu:
                description:
                  -  Maximum OSPF packet size
                type: int
              ipsec_sa:
                description:
                  - IPSec security association name
                type: str
              secondary:
                description:
                  - Treat interface as secondary
                type: bool
              flood_reduction:
                description:
                  - Enable flood reduction.
                type: bool
              demand_circuit:
                description:
                  -  Interface functions as a demand circuit.
                type: bool
              no_advertise_adjacency_segment:
                 description:
                   - Do not advertise an adjacency segment for this interface.
                 type: bool
              no_eligible_backup:
                description:
                  - Not eligible to backup traffic from protected interfaces.
                type: bool
              no_eligible_remote_backup:
                description:
                  - Not eligible for Remote-LFA backup traffic from protected interfaces.
                type: bool
              no_interface_state_traps:
                description:
                  - Do not send interface state change traps.
                type: bool
              no_neighbor_down_notification:
                description:
                  - Don't inform other protocols about neighbor down events.
                type: bool
              node_link_protection:
                description:
                  - Protect interface from both link and node faults.
                type: str
              dead_interval:
                description:
                  - Dead interval (seconds).
                type: int
              hello_interval:
                description:
                  - Hello interval (seconds).
                type: int
              poll_interval:
                description:
                  - Poll interval (seconds).
                type: int
              retransmit_interval:
                description:
                  - Retransmit interval (seconds).
                type: int
              transit_delay:
                description:
                  - Transit delay (seconds).
                type: int
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show protocols ospf).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result
    type: str
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - parsed
    - gathered
    - rendered
    default: merged
"""
EXAMPLES = """

"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.ospf_interfaces.ospf_interfaces import (
    Ospf_interfacesArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ospf_interfaces.ospf_interfaces import (
    Ospf_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    module = AnsibleModule(
        argument_spec=Ospf_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )
    result = Ospf_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
