#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
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
The module file for junos_security_zones
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
  'metadata_version': '1.1',
  'status': ['preview'],
  'supported_by': 'network'
}

DOCUMENTATION = """
---
module: junos_security_zones
version_added: 2.9.0
short_description: Manage security zones on Juniper JUNOS devices
description: This module provides declarative management of security zones on Juniper JUNOS devices
author: Pranav Bhatt (@pranav-bhatt)
requirements:
  - ncclient (>=v0.6.4)
  - xmltodict (>=0.12.0)
notes:
- This module requires the netconf system service be enabled on the device being managed.
- This module works with connection C(netconf). 
- See L(the Junos OS Platform Options,https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
- Tested against JunOS v18.4R1
options:
  config:
    description: Dictionary of security zone parameters
    type: dict
    suboptions:
      functional_zone_management:
        description:
          - Functional zone to configure host for out of band management interfaces
        type: dict
        suboptions:
          description:
            description:
              - Text description of zone
            type: str
          host_inbound_traffic: &host_inbound_traffic
            description:
              - Allowed system services & protocols
            type: dict
            suboptions:
              protocols:
                description:
                  - Protocol type of incoming traffic to accept
                type: dict
                suboptions:
                  all:
                    description:
                      - All protocols
                    type: dict
                    suboptions:
                      enable:
                        description:
                          - Enable all protocols option
                        type: bool
                      except:
                        description:
                          - Disallow all incoming traffic
                        type: bool
                  names:
                    description:
                      - Protocol types of incoming traffic to accept
                    type: list
                    elements: str
              system_services:
                description:
                  - Type of incoming system-service traffic to accept
                type: dict
                suboptions:
                  all:
                    description:
                      - All system services
                    type: dict
                    suboptions:
                      enable:
                        description:
                          - Enable all system services option
                        type: bool
                      except:
                        description:
                          - Disallow all incoming system-service traffic
                        type: bool
                  names:
                    description:
                      - Type of incoming system-service traffic to accept
                    type: list
                    elements: str
          interfaces: &interfaces
            description:
              - Interfaces that are part of this zone
            type: list
            elements: str
          screen: &screen
            description:
              - Name of ids option object applied to the zone
            type: str
      security_zones:
        description:
          - Security zones
        type: list
        elements: dict
        suboptions:
          names:
            description:
              - Name of the security zone
            type: str
          address_book:
            description:
              - Address book entries
            type: dict
            suboptions:
              addresses:
                description:
                  - Define security addresses
                type: list
                elements: dict
                suboptions:
                  name:
                    description:
                      - Name of address
                    type: str
                  ip_prefix:
                    description:
                      - Numeric IPv4 or IPv6 address with prefix
                    type: list
                    elements: str
                  description:
                    description:
                      - Text description of address
                    type: str
                  dns_name:
                    description:
                      - DNS address name
                    type: str
                  range_address:
                    description:
                      - Address range
                    type: dict
                    suboptions:
                      from:
                        description:
                          - Start of address range
                        type: str
                      to:
                        description:
                          - End of address range
                        type: str
                  wildcard_address:
                    description:
                      - Numeric IPv4 wildcard address with in the form of a.d.d.r/netmask
                    type: str
              address_sets:
                description:
                  - Define security address sets
                type: list
                elements: dict
                suboptions:
                  name:
                    description:
                      - Name of address set
                    type: str
                  address:
                    description:
                      - Address to be included in this set
                    type: list
                    elements: str
                  address_set:
                    description:
                      - Define an address-set name
                    type: list
                    elements: str
                  description:
                    description:
                      - Text description of address set
                    type: str
          advance_policy_based_routing_profile:
            description:
              - Enable Advance Policy Based Routing on this zone
            type: str
          application_tracking:
            description:
              - Enable Application tracking support for this zone
            type: bool
          description:
            description:
              - Text description of zone
            type: str
          enable_reverse_reroute:
            description:
              - Enable Reverse route lookup when there is change in ingress interface
            type: bool
          host_inbound_traffic: *host_inbound_traffic
          interfaces: *interfaces
          screen: *screen
          source_identity_log:
            description:
              - Show user and group info in session log for this zone
            type: bool
          tcp_rst:
            description:
              - Send RST for NON-SYN packet not matching TCP session
            type: bool

  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the JunOS device
        by executing the command B(show security policies).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - rendered
    - gathered
    - parsed
    default: merged
    description:
      - The state the configuration should be left in
      - The states I(rendered), I(gathered) and I(parsed) does not perform any change
        on the device.
      - The state I(rendered) will transform the configuration in C(config) option to
        platform specific CLI commands which will be returned in the I(rendered) key
        within the result. For state I(rendered) active connection to remote host is
        not required.
        behaviour for this module.
      - The state I(gathered) will fetch the running configuration from device and transform
        it into structured data in the format as per the resource module argspec and
        the value is returned in the I(gathered) key within the result.
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into JSON format as per the resource module parameters and the
        value is returned in the I(parsed) key within the result. The value of C(running_config)
        option should be the same format as the output of command
        I(show security policies detail) executed on device. For state I(parsed) active
        connection to remote host is not required.
    type: str
"""
EXAMPLES = """





















"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
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
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.security_zones.security_zones import Security_zonesArgs
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.security_zones.security_zones import Security_zones


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Security_zonesArgs.argument_spec,
                           supports_check_mode=True)

    result = Security_zones(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
