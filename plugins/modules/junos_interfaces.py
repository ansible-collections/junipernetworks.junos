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
The module file for junos_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: junos_interfaces
short_description: Junos Interfaces resource module
description: This module manages the interfaces on Juniper Junos OS network devices.
version_added: 1.0.0
author: Ganesh Nalawade (@ganeshrn)
options:
  config:
    description: The provided configuration
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of interface, e.g. ge-0/0/0.
        type: str
        required: true
      description:
        description:
        - Interface description.
        type: str
      duplex:
        description:
        - Interface link status. Applicable for Ethernet interfaces only, either in
          half duplex, full duplex or in automatic state which negotiates the duplex
          automatically.
        type: str
        choices:
        - automatic
        - full-duplex
        - half-duplex
      enabled:
        default: true
        description:
        - Administrative state of the interface.
        - Set the value to C(true) to administratively enabled the interface or C(false)
          to disable it.
        type: bool
      hold_time:
        description:
        - The hold time for given interface name.
        type: dict
        suboptions:
          down:
            description:
            - The link down hold time in milliseconds.
            type: int
          up:
            description:
            - The link up hold time in milliseconds.
            type: int
      mtu:
        description:
        - MTU for a specific interface.
        - Applicable for Ethernet interfaces only.
        type: int
      speed:
        description:
        - Interface link speed. Applicable for Ethernet interfaces only.
        type: str
      units:
        description:
          - Specify Logical interfaces units.
        type: list
        elements: dict
        suboptions:
          name:
            description:
              - Specify interface unit number.
            type: int
          description:
            description: Specify logical interface description.
            type: str
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show interfaces).
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
    - gathered
    - parsed
    - rendered
    default: merged
    description:
    - The state of the configuration after module completion
    type: str
requirements:
- ncclient (>=v0.6.4)
notes:
- This module requires the netconf system service be enabled on the remote device
  being managed.
- Tested against vSRX JUNOS version 18.4R1.
- This module works with connection C(netconf).
- See L(the Junos OS Platform Options,https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     description "test interface";
#     speed 1g;
# }
# fe-0/0/2 {
#     vlan-tagging;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/3 {
#     description "Configured by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }

- name: Merge provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_interfaces:
    config:
      - name: ge-0/0/1
        description: Configured by Ansible-1
        enabled: true
        units:
          - name: 0
            description: "This is logical intf unit0"
        mtu: 1800
      - name: ge-0/0/2
        description: Configured by Ansible-2
        enabled: false
    state: merged

# Task Output
# -----------
#
# before:
# - description: test interface
#   enabled: true
#   name: ge-0/0/1
#   speed: 1g
# - enabled: true
#   name: fe-0/0/2
# - description: Configured by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface><nc:name>ge-0/0/1</nc:name>
#   <nc:description>Configured by Ansible-1</nc:description><nc:mtu>1800</nc:mtu><nc:unit><nc:name>0</nc:name>
#   <nc:description>This is logical intf unit0</nc:description></nc:unit></nc:interface><nc:interface><nc:name>ge-0/0/2</nc:name>
#   <nc:description>Configured by Ansible-2</nc:description><nc:disable/></nc:interface></nc:interfaces>
# after:
# - description: Configured by Ansible-1
#   enabled: true
#   mtu: 1800
#   name: ge-0/0/1
#   speed: 1g
#   units:
#   - description: This is logical intf unit0
#     name: 0
# - enabled: true
#   name: fe-0/0/2
# - description: Configured by Ansible-2
#   enabled: false
#   name: ge-0/0/2
# - description: Configured by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0

# After state:
# ------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     description "Configured by Ansible-1";
#     speed 1g;
#     mtu 1800;
#     unit 0 {
#         description "This is logical intf unit0";
#     }
# }
# fe-0/0/2 {
#     vlan-tagging;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/2 {
#     description "Configured by Ansible-2";
#     disable;
# }
# ge-0/0/3 {
#     description "Configured by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }

# Using deleted

# Before state:
# -------------
#
# ge-0/0/1 {
#     description "Configured by Ansible-1";
#     speed 1g;
#     mtu 1800;
#     unit 0 {
#         description "This is logical intf unit0";
#     }
# }
# fe-0/0/2 {
#     vlan-tagging;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/2 {
#     description "Configured by Ansible-2";
#     disable;
# }
# ge-0/0/3 {
#     description "Configured by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }

- name: "Delete given options for the interface (Note: This won't delete the interface itself if any other values are configured for interface)"
  junipernetworks.junos.junos_interfaces:
    config:
      - name: ge-0/0/1
        description: Configured by Ansible-1
        speed: 1g
        mtu: 1800
      - name: ge-0/0/2
        description: Configured by Ansible -2
    state: deleted

# Task Output
# -----------
#
# before:
# - description: Configured by Ansible-1
#   enabled: true
#   mtu: 1800
#   name: ge-0/0/1
#   speed: 1g
#   units:
#   - description: This is logical intf unit0
#     name: 0
# - enabled: true
#   name: fe-0/0/2
# - description: Configured by Ansible-2
#   enabled: false
#   name: ge-0/0/2
# - description: Configured by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface>
#   <nc:name>ge-0/0/1</nc:name><nc:description delete="delete"/>
#   <nc:speed delete="delete"/><nc:mtu delete="delete"/><nc:link-mode delete="delete"/>
#   <nc:disable delete="delete"/><nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time><nc:unit>
#   <nc:name>0</nc:name><nc:description delete="delete"/></nc:unit></nc:interface><nc:interface><nc:name>ge-0/0/2</nc:name>
#   <nc:description delete="delete"/><nc:speed delete="delete"/><nc:mtu delete="delete"/><nc:link-mode delete="delete"/>
#   <nc:disable delete="delete"/><nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface>
#   </nc:interfaces>
# after:
# - enabled: true
#   name: ge-0/0/1
# - enabled: true
#   name: fe-0/0/2
# - description: Configured by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0

# After state:
# ------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     unit 0;
# }
# fe-0/0/2 {
#     vlan-tagging;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/3 {
#     description "Configured by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }

# Using overridden

# Before state:
# -------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     unit 0;
# }
# fe-0/0/2 {
#     vlan-tagging;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/3 {
#     description "Configured by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }

- name: Override device configuration of all interfaces with provided configuration
  junipernetworks.junos.junos_interfaces:
    config:
      - enabled: true
        name: ge-0/0/1
      - enabled: true
        name: fe-0/0/2
        description: Configured by Ansible-2
        enabled: false
        mtu: 2800
      - description: Updated by Ansible-3
        enabled: true
        name: ge-0/0/3
      - enabled: true
        name: fxp0
      - enabled: true
        name: lo0
    state: overridden

# Task Output
# -----------
#
# before:
# - enabled: true
#   name: ge-0/0/1
# - enabled: true
#   name: fe-0/0/2
# - description: Configured by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:interface><nc:name>ge-0/0/1</nc:name><nc:description delete="delete"/>
#   <nc:speed delete="delete"/><nc:mtu delete="delete"/><nc:link-mode delete="delete"/>
#   <nc:disable delete="delete"/><nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/>
#   </nc:hold-time></nc:interface><nc:interface><nc:name>fe-0/0/2</nc:name><nc:description delete="delete"/>
#   <nc:speed delete="delete"/><nc:mtu delete="delete"/><nc:link-mode delete="delete"/><nc:disable delete="delete"/>
#   <nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface><nc:interface>
#   <nc:name>ge-0/0/3</nc:name><nc:description delete="delete"/><nc:speed delete="delete"/><nc:mtu delete="delete"/>
#   <nc:link-mode delete="delete"/><nc:disable delete="delete"/><nc:hold-time>
#   <nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface>
#   <nc:interface><nc:name>fxp0</nc:name><nc:description delete="delete"/><nc:speed delete="delete"/>
#   <nc:link-mode delete="delete"/><nc:disable delete="delete"/>
#   <nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/>
#   </nc:hold-time></nc:interface><nc:interface><nc:name>lo0</nc:name>
#   <nc:description delete="delete"/><nc:disable delete="delete"/>
#   <nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/>
#   </nc:hold-time></nc:interface><nc:interface><nc:name>ge-0/0/1</nc:name>
#   </nc:interface><nc:interface><nc:name>fe-0/0/2</nc:name>
#   <nc:description>Configured by Ansible-2</nc:description>
#   <nc:mtu>2800</nc:mtu><nc:disable/></nc:interface><nc:interface>
#   <nc:name>ge-0/0/3</nc:name><nc:description>Updated by Ansible-3</nc:description>
#   </nc:interface><nc:interface><nc:name>fxp0</nc:name></nc:interface><nc:interface>
#   <nc:name>lo0</nc:name></nc:interface></nc:interfaces>
# after:
# - enabled: true
#   name: ge-0/0/1
# - description: Configured by Ansible-2
#   enabled: false
#   mtu: 2800
#   name: fe-0/0/2
# - description: Updated by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0

# After state:
# ------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     unit 0;
# }
# fe-0/0/2 {
#     description "Configured by Ansible-2";
#     disable;
#     vlan-tagging;
#     mtu 2800;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/3 {
#     description "Updated by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }


# Using replaced

# Before state:
# -------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     unit 0;
# }
# fe-0/0/2 {
#     description "Configured by Ansible-2";
#     disable;
#     vlan-tagging;
#     mtu 2800;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/3 {
#     description "Updated by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }

- name: Replace device configuration of listed interfaces with provided configuration
  junipernetworks.junos.junos_interfaces:
    config:
      - name: ge-0/0/2
        description: Configured by Ansible-2
        enabled: false
        mtu: 2800
      - name: ge-0/0/3
        description: Configured by Ansible-3
    state: replaced

# Task Output
# -----------
#
# before:
# - enabled: true
#   name: ge-0/0/1
# - description: Configured by Ansible-2
#   enabled: false
#   mtu: 2800
#   name: fe-0/0/2
# - description: Updated by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface>
#   <nc:name>ge-0/0/2</nc:name><nc:description delete="delete"/><nc:speed delete="delete"/>
#   <nc:mtu delete="delete"/><nc:link-mode delete="delete"/><nc:disable delete="delete"/>
#   <nc:hold-time><nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface>
#   <nc:interface><nc:name>ge-0/0/3</nc:name><nc:description delete="delete"/><nc:speed delete="delete"/>
#   <nc:mtu delete="delete"/><nc:link-mode delete="delete"/><nc:disable delete="delete"/><nc:hold-time>
#   <nc:up delete="delete"/><nc:down delete="delete"/></nc:hold-time></nc:interface><nc:interface><nc:name>ge-0/0/2</nc:name>
#   <nc:description>Configured by Ansible-2</nc:description><nc:mtu>2800</nc:mtu><nc:disable/></nc:interface><nc:interface>
#   <nc:name>ge-0/0/3</nc:name><nc:description>Configured by Ansible-3</nc:description></nc:interface></nc:interfaces>
# after:
# - enabled: true
#   name: ge-0/0/1
# - description: Configured by Ansible-2
#   enabled: false
#   mtu: 2800
#   name: fe-0/0/2
# - description: Configured by Ansible-2
#   enabled: false
#   mtu: 2800
#   name: ge-0/0/2
# - description: Configured by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0

# After state:
# ------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     unit 0;
# }
# fe-0/0/2 {
#     description "Configured by Ansible-2";
#     disable;
#     vlan-tagging;
#     mtu 2800;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/2 {
#     description "Configured by Ansible-2";
#     disable;
#     mtu 2800;
# }
# ge-0/0/3 {
#     description "Configured by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }

# Using gathered

# Before state:
# ------------
#
# vagrant@vsrx# show interfaces
# ge-0/0/1 {
#     unit 0;
# }
# fe-0/0/2 {
#     description "Configured by Ansible-2";
#     disable;
#     vlan-tagging;
#     mtu 2800;
#     unit 10 {
#         vlan-id 10;
#     }
#     unit 11 {
#         vlan-id 11;
#     }
# }
# ge-0/0/2 {
#     description "Configured by Ansible-2";
#     disable;
#     mtu 2800;
# }
# ge-0/0/3 {
#     description "Configured by Ansible-3";
# }
# fxp0 {
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#     }
# }
# lo0 {
#     unit 0 {
#         family inet {
#             address 192.0.2.1/32;
#         }
#     }
# }

- name: Gather junos interfaces as in given arguments
  junipernetworks.junos.junos_interfaces:
    state: gathered

# Task Output
# -----------
#
# gathered:
# - enabled: true
#   name: ge-0/0/1
# - description: Configured by Ansible-2
#   enabled: false
#   mtu: 2800
#   name: fe-0/0/2
# - description: Configured by Ansible-2
#   enabled: false
#   mtu: 2800
#   name: ge-0/0/2
# - description: Configured by Ansible-3
#   enabled: true
#   name: ge-0/0/3
# - enabled: true
#   name: fxp0
# - enabled: true
#   name: lo0

# Using parsed

# parsed.cfg
# ------------
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <interfaces>
#             <interface>
#                 <name>ge-0/0/1</name>
#                 <description>Configured by Ansible</description>
#                 <disable/>
#                 <speed>100m</speed>
#                 <mtu>1024</mtu>
#                 <hold-time>
#                     <up>2000</up>
#                     <down>2200</down>
#                 </hold-time>
#                 <link-mode>full-duplex</link-mode>
#                 <unit>
#                     <name>0</name>
#                     <family>
#                         <ethernet-switching>
#                             <interface-mode>access</interface-mode>
#                             <vlan>
#                                 <members>vlan100</members>
#                             </vlan>
#                         </ethernet-switching>
#                     </family>
#                 </unit>
#             </interface>
#         </interfaces>
#     </configuration>
# </rpc-reply>

# - name: Convert interfaces config to structured data without connecting to the appliance
#   junipernetworks.junos.junos_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed

# Task Output
# -----------
#
# parsed:
# - description: Configured by Ansible
#   duplex: full-duplex
#   enabled: false
#   hold_time:
#     down: 2200
#     up: 2000
#   mtu: 1024
#   name: ge-0/0/1
#   speed: 100m

# Using rendered

- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_interfaces:
    config:
    - name: ge-0/0/2
      description: Configured by Ansible
      mtu: 2048
      speed: 20m
      hold_time:
        up: 3200
        down: 3200
    state: rendered

# Task Output
# -----------
#
# rendered: <nc:interfaces
#     xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#     <nc:interface>
#         <nc:name>ge-0/0/2</nc:name>
#         <nc:description>Configured by Ansible</nc:description>
#         <nc:speed>20m</nc:speed>
#         <nc:mtu>2048</nc:mtu>
#         <nc:hold-time>
#             <nc:up>3200</nc:up>
#             <nc:down>3200</nc:down>
#         </nc:hold-time>
#     </nc:interface>
# </nc:interfaces>"
"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
xml:
  description: The set of xml rpc payload pushed to the remote device.
  returned: always
  type: list
  sample: ['<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
        <interfaces>
            <interface>
                <name>ge-0/0/1</name>
                <description>Configured by Ansible</description>
                <disable/>
                <speed>100m</speed>
                <mtu>1024</mtu>
                <hold-time>
                    <up>2000</up>
                    <down>2200</down>
                </hold-time>
                <link-mode>full-duplex</link-mode>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <interface-mode>access</interface-mode>
                            <vlan>
                                <members>vlan100</members>
                            </vlan>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
        </interfaces>
    </configuration>
</rpc-reply>', 'xml 2', 'xml 3']
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.interfaces.interfaces import (
    InterfacesArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.interfaces.interfaces import (
    Interfaces,
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
        argument_spec=InterfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    result = Interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
