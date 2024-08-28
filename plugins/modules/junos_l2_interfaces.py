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
The module file for junos_l2_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: junos_l2_interfaces
short_description: L2 interfaces resource module
description: This module provides declarative management of a Layer-2 interface on
  Juniper JUNOS devices.
version_added: 1.0.0
author: Ganesh Nalawade (@ganeshrn)
options:
  config:
    description: A dictionary of Layer-2 interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of interface, e.g. ge-0/0/1.
        type: str
        required: true
      unit:
        description:
        - Logical interface number. Value of C(unit) should be of type integer.
        type: int
      access:
        description:
        - Configure the interface as a Layer 2 access mode.
        type: dict
        suboptions:
          vlan:
            description:
            - Configure the access VLAN ID.
            type: str
      trunk:
        description:
        - Configure the interface as a Layer 2 trunk mode.
        type: dict
        suboptions:
          allowed_vlans:
            description:
            - List of VLANs to be configured in trunk port. It's used as the VLAN
              range to ADD or REMOVE from the trunk.
            type: list
            elements: str
          native_vlan:
            description:
            - Native VLAN to be configured in trunk port. It is used as the trunk
              native VLAN ID.
            type: str
      enhanced_layer:
        description:
        - True if your device has Enhanced Layer 2 Software (ELS). If the l2 configuration
          is under C(interface-mode) the value is True else if the l2 configuration
          is under C(port-mode) value is False
        type: bool
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
  See U(https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html)
- The module examples uses callback plugin (stdout_callback = yaml) to generate task
  output in yaml format.
"""

EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# ansible@junos01# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/3 {
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#         }
#     }
# }
# ge-0/0/4 {
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

- name: Merge provided configuration with device configuration
  junipernetworks.junos.junos_l2_interfaces:
    config:
      - name: ge-0/0/3
        access:
          vlan: v101
      - name: ge-0/0/4
        trunk:
          allowed_vlans:
            - vlan30
          native_vlan: 50
    state: merged

# Task Output
# -----------
#
# before:
# - enhanced_layer: true
#   name: ge-0/0/3
#   unit: 0
# - enhanced_layer: true
#   name: ge-0/0/4
#   unit: 0
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# 	<nc:interface>
# 		<nc:name>ge-0/0/3</nc:name>
# 		<nc:unit>
# 			<nc:name>0</nc:name>
# 			<nc:family>
# 				<nc:ethernet-switching>
# 					<nc:interface-mode>access</nc:interface-mode>
# 					<nc:vlan>
# 						<nc:members>v101</nc:members>
# 					</nc:vlan>
# 				</nc:ethernet-switching>
# 			</nc:family>
# 		</nc:unit>
# 	</nc:interface>
# 	<nc:interface>
# 		<nc:name>ge-0/0/4</nc:name>
# 		<nc:unit>
# 			<nc:name>0</nc:name>
# 			<nc:family>
# 				<nc:ethernet-switching>
# 					<nc:interface-mode>trunk</nc:interface-mode>
# 					<nc:vlan>
# 						<nc:members>vlan30</nc:members>
# 					</nc:vlan>
# 				</nc:ethernet-switching>
# 			</nc:family>
# 		</nc:unit>
# 		<nc:native-vlan-id>50</nc:native-vlan-id>
# 	</nc:interface>
# </nc:interfaces>
# after:
# - access:
#     vlan: v101
#   enhanced_layer: true
#   name: ge-0/0/3
#   unit: 0
# - enhanced_layer: true
#   name: ge-0/0/4
#   trunk:
#     allowed_vlans:
#     - vlan30
#     native_vlan: '50'
#   unit: 0

# After state:
# ------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/3 {
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#             vlan {
#                 members v101;
#             }
#         }
#     }
# }
# ge-0/0/4 {
#     native-vlan-id 50;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members vlan30;
#             }
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }


# Using overridden

# Before state:
# -------------
# ansible@junos01# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/3 {
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#             vlan {
#                 members v101;
#             }
#         }
#     }
# }
# ge-0/0/4 {
#     native-vlan-id 50;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members vlan30;
#             }
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

- name: Override provided configuration with device configuration
  junipernetworks.junos.junos_l2_interfaces:
    config:
      - name: ge-0/0/4
        trunk:
          allowed_vlans:
            - v101
          native_vlan: 30
    state: overridden

# Task Output
# -----------
#
# before:
# - access:
#     vlan: v101
#   enhanced_layer: true
#   name: ge-0/0/3
#   unit: 0
# - enhanced_layer: true
#   name: ge-0/0/4
#   trunk:
#     allowed_vlans:
#     - vlan30
#     native_vlan: '50'
#   unit: 0
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:interface>
#     <nc:name>ge-0/0/4</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:ethernet-switching>
#           <nc:interface-mode delete="delete"/>
#           <nc:vlan delete="delete"/>
#         </nc:ethernet-switching>
#       </nc:family>
#     </nc:unit>
#     <nc:native-vlan-id delete="delete"/>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/4</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:ethernet-switching>
#           <nc:interface-mode>trunk</nc:interface-mode>
#           <nc:vlan>
#             <nc:members>v101</nc:members>
#           </nc:vlan>
#         </nc:ethernet-switching>
#       </nc:family>
#     </nc:unit>
#     <nc:native-vlan-id>30</nc:native-vlan-id>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/3</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:ethernet-switching>
#           <nc:interface-mode delete="delete"/>
#           <nc:vlan delete="delete"/>
#         </nc:ethernet-switching>
#       </nc:family>
#     </nc:unit>
#     <nc:native-vlan-id delete="delete"/>
#   </nc:interface>
# </nc:interfaces>
# after:
# - enhanced_layer: true
#   name: ge-0/0/4
#   trunk:
#     allowed_vlans:
#     - v101
#     native_vlan: '30'
#   unit: 0

# After state:
# ------------
# user@junos01# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/3 {
#     unit 0 {
#         family ethernet-switching;
#     }
# }
# ge-0/0/4 {
#     native-vlan-id 30;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members v101;
#             }
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

# Using replaced

# Before state:
# -------------
#
# ansible@junos01# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/3 {
#     unit 0 {
#         family ethernet-switching;
#     }
# }
# ge-0/0/4 {
#     native-vlan-id 30;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members v101;
#             }
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

- name: Replace provided configuration with device configuration
  junipernetworks.junos.junos_l2_interfaces:
    config:
      - name: ge-0/0/3
        access:
          vlan: v101
      - name: ge-0/0/4
        trunk:
          allowed_vlans:
            - vlan30
          native_vlan: 50
    state: replaced

# Task Output
# -----------
#
# before:
# - enhanced_layer: true
#   name: ge-0/0/4
#   trunk:
#     allowed_vlans:
#     - v101
#     native_vlan: '30'
#   unit: 0
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:interface>
#     <nc:name>ge-0/0/4</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:ethernet-switching>
#           <nc:interface-mode delete="delete"/>
#           <nc:vlan delete="delete"/>
#         </nc:ethernet-switching>
#       </nc:family>
#     </nc:unit>
#     <nc:native-vlan-id delete="delete"/>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/3</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:ethernet-switching>
#           <nc:interface-mode>access</nc:interface-mode>
#           <nc:vlan>
#             <nc:members>v101</nc:members>
#           </nc:vlan>
#         </nc:ethernet-switching>
#       </nc:family>
#     </nc:unit>
#   </nc:interface>
#   <nc:interface>
#     <nc:name>ge-0/0/4</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:ethernet-switching>
#           <nc:interface-mode>trunk</nc:interface-mode>
#           <nc:vlan>
#             <nc:members>vlan30</nc:members>
#           </nc:vlan>
#         </nc:ethernet-switching>
#       </nc:family>
#     </nc:unit>
#     <nc:native-vlan-id>50</nc:native-vlan-id>
#   </nc:interface>
# </nc:interfaces>
# after:
# - access:
#     vlan: v101
#   enhanced_layer: true
#   name: ge-0/0/3
#   unit: 0
# - enhanced_layer: true
#   name: ge-0/0/4
#   trunk:
#     allowed_vlans:
#     - vlan30
#     native_vlan: '50'
#   unit: 0

# After state:
# ------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/3 {
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#             vlan {
#                 members v101;
#             }
#         }
#     }
# }
# ge-0/0/4 {
#     native-vlan-id 50;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members vlan30;
#             }
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

# Using deleted

# Before state:
# -------------
#
# ansible@junos01# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/3 {
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#             vlan {
#                 members v101;
#             }
#         }
#     }
# }
# ge-0/0/4 {
#     native-vlan-id 50;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members vlan30;
#             }
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

- name: "Delete L2 attributes of given interfaces (Note: This won't delete the
    interface itself)."
  junipernetworks.junos.junos_l2_interfaces:
    config:
      - name: ge-0/0/1
      - name: ge-0/0/2
    state: deleted

# Task Output
# -----------
#
# before:
# - access:
#     vlan: v101
#   enhanced_layer: true
#   name: ge-0/0/3
#   unit: 0
# - enhanced_layer: true
#   name: ge-0/0/4
#   trunk:
#     allowed_vlans:
#     - vlan30
#     native_vlan: '50'
#   unit: 0
# commands:
# - <nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:interface>
#     <nc:name>ge-0/0/3</nc:name>
#     <nc:unit>
#       <nc:name>0</nc:name>
#       <nc:family>
#         <nc:ethernet-switching>
#           <nc:interface-mode delete="delete"/>
#           <nc:vlan delete="delete"/>
#         </nc:ethernet-switching>
#       </nc:family>
#     </nc:unit>
#     <nc:native-vlan-id delete="delete"/>
#   </nc:interface>
# </nc:interfaces>
# after:
# - enhanced_layer: true
#   name: ge-0/0/4
#   trunk:
#     allowed_vlans:
#     - vlan30
#     native_vlan: '50'
#   unit: 0

# After state:
# ------------
#
# ansible@junos01# show interfaces
# ge-0/0/1 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/2 {
#     unit 0 {
#         family inet;
#         family inet6;
#     }
# }
# ge-0/0/3 {
#     unit 0 {
#         family ethernet-switching;
#     }
# }
# ge-0/0/4 {
#     native-vlan-id 50;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members vlan30;
#             }
#         }
#     }
# }
# fxp0 {
#     enable;
#     unit 0 {
#         family inet {
#             dhcp;
#         }
#         family inet6;
#     }
# }

# Using gathered

# Before state:
# -------------
#
# user@junos01# show interfaces
# ge-0/0/1 {
#     description "Configured by Ansible";
#     disable;
#     speed 100m;
#     mtu 1024;
#     hold-time up 2000 down 2200;
#     link-mode full-duplex;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode access;
#             vlan {
#                 members vlan100;
#             }
#         }
#     }
# }
# ge-0/0/2 {
#     description "Configured by Ansible";
#     native-vlan-id 400;
#     speed 10m;
#     mtu 2048;
#     hold-time up 3000 down 3200;
#     unit 0 {
#         family ethernet-switching {
#             interface-mode trunk;
#             vlan {
#                 members [ vlan200 vlan300 ];
#             }
#         }
#     }
# }
# em1 {
#     description TEST;
# }
# fxp0 {
#     description ANSIBLE;
#     speed 1g;
#     link-mode automatic;
#     unit 0 {
#         family inet {
#             address 10.8.38.38/24;
#         }
#     }
# }

- name: Gather junos layer 2 interfaces facts
  junipernetworks.junos.junos_l2_interfaces:
    state: gathered

# Task Output
# -----------
#
# gathered:
# - access:
#     vlan: vlan100
#   enhanced_layer: true
#   name: ge-0/0/1
#   unit: 0
# - enhanced_layer: true
#   name: ge-0/0/2
#   trunk:
#     allowed_vlans:
#     - vlan200
#     - vlan300
#     native_vlan: '400'
#   unit: 0

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

- name: Convert interfaces config to argspec without connecting to the appliance
  junipernetworks.junos.junos_l2_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Task Output
# -----------
#
# parsed:
# - access:
#     vlan: vlan100
#   enhanced_layer: true
#   name: ge-0/0/1
#   unit: 0
# - enhanced_layer: true
#   name: ge-0/0/2
#   trunk:
#     allowed_vlans:
#     - vlan200
#     - vlan300
#     native_vlan: '400'
#   unit: 0

# Using rendered

- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_l2_interfaces:
    config:
      - name: ge-0/0/1
        access:
          vlan: vlan100
      - name: ge-0/0/2
        trunk:
          allowed_vlans:
            - vlan200
            - vlan300
          native_vlan: '400'
    state: rendered

# Task Output
# -----------
#
# "rendered": "<nc:interfaces xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#     <nc:interface>
#         <nc:name>ge-0/0/1</nc:name>
#         <nc:unit>
#             <nc:name>0</nc:name>
#             <nc:family>
#                 <nc:ethernet-switching>
#                     <nc:interface-mode>access</nc:interface-mode>
#                     <nc:vlan>
#                         <nc:members>vlan100</nc:members>
#                     </nc:vlan>
#                 </nc:ethernet-switching>
#             </nc:family>
#         </nc:unit>
#     </nc:interface>
#     <nc:interface>
#         <nc:name>ge-0/0/2</nc:name>
#         <nc:unit>
#             <nc:name>0</nc:name>
#             <nc:family>
#                 <nc:ethernet-switching>
#                     <nc:interface-mode>trunk</nc:interface-mode>
#                     <nc:vlan>
#                         <nc:members>vlan200</nc:members>
#                         <nc:members>vlan300</nc:members>
#                     </nc:vlan>
#                 </nc:ethernet-switching>
#             </nc:family>
#         </nc:unit>
#         <nc:native-vlan-id>400</nc:native-vlan-id>
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
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['<nc:interfaces
    xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
    <nc:interface>
        <nc:name>ge-0/0/1</nc:name>
        <nc:unit>
            <nc:name>0</nc:name>
            <nc:family>
                <nc:ethernet-switching>
                    <nc:interface-mode>access</nc:interface-mode>
                    <nc:vlan>
                        <nc:members>vlan100</nc:members>
                    </nc:vlan>
                </nc:ethernet-switching>
            </nc:family>
        </nc:unit>
    </nc:interface>
    <nc:interface>
        <nc:name>ge-0/0/2</nc:name>
        <nc:unit>
            <nc:name>0</nc:name>
            <nc:family>
                <nc:ethernet-switching>
                    <nc:interface-mode>trunk</nc:interface-mode>
                    <nc:vlan>
                        <nc:members>vlan200</nc:members>
                        <nc:members>vlan300</nc:members>
                    </nc:vlan>
                </nc:ethernet-switching>
            </nc:family>
        </nc:unit>
        <nc:native-vlan-id>400</nc:native-vlan-id>
    </nc:interface>
</nc:interfaces>', 'xml 2', 'xml 3']
rendered:
  description: The provided configuration in the
    task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
gathered:
  description: Facts about the network resource gathered
    from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed
    into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.l2_interfaces.l2_interfaces import (
    L2_interfacesArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.l2_interfaces.l2_interfaces import (
    L2_interfaces,
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
        argument_spec=L2_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    result = L2_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
