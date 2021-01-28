.. _junipernetworks.junos.junos_l3_interfaces_module:


*****************************************
junipernetworks.junos.junos_l3_interfaces
*****************************************

**L3 interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of a Layer 3 interface on Juniper JUNOS devices



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of Layer 3 interface options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 addresses to be set for the Layer 3 logical interface mentioned in <em>name</em> option. The address format is &lt;ipv4 address&gt;/&lt;mask&gt;. The mask is number in range 0-32 for example, 192.0.2.1/24, or <code>dhcp</code> to query DHCP for an IP address</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 address to be set for the specific interface</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 addresses to be set for the Layer 3 logical interface mentioned in <em>name</em> option. The address format is &lt;ipv6 address&gt;/&lt;mask&gt;, the mask is number in range 0-128 for example, 2001:db8:2201:1::1/64 or <code>auto-config</code> to use SLAAC</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 address to be set for the specific interface</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Full name of interface, e.g. ge-0/0/1</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">0</div>
                </td>
                <td>
                        <div>Logical interface number. Value of <code>unit</code> should be of type integer</div>
                </td>
            </tr>

            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>running_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This option is used only with state <em>parsed</em>.</div>
                        <div>The value of this option should be the output received from the Junos device by executing the command <b>show interfaces</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result</div>
                </td>
            </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module requires the netconf system service be enabled on the device being managed.
   - This module works with connection ``netconf``. See `the Junos OS Platform Options <../network/user_guide/platform_junos.html>`_.
   - Tested against JunOS v18.4R1



Examples
--------

.. code-block:: yaml

    # Using deleted

    # Before state:
    # -------------
    #
    # admin# show interfaces
    # ge-0/0/1 {
    #     description "L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 10.200.16.10/24;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     description "non L3 interface";
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #             vlan {
    #                 members 2;
    #             }
    #         }
    #     }
    # }

    - name: Delete JUNOS L3 logical interface
      junipernetworks.junos.junos_l3_interfaces:
        config:
        - name: ge-0/0/1
        - name: ge-0/0/2
      state: deleted

    # After state:
    # ------------
    #
    # admin# show interfaces
    # ge-0/0/1 {
    #     description "deleted L3 interface";
    # }
    # ge-0/0/2 {
    #     description "non L3 interface";
    #     unit 0 {
    #         family ethernet-switching {
    #             interface-mode access;
    #             vlan {
    #                 members 2;
    #             }
    #         }
    #     }
    # }
    # Using merged
    # Before state
    # ------------
    #
    # admin# show interfaces
    # ge-0/0/1 {
    #     description "L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 10.200.16.10/24;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     description "non configured interface";
    #     unit 0;
    # }
    - name: Merge provided configuration with device configuration (default operation is merge)
      junipernetworks.junos.junos_l3_interfaces:
        config:
        - name: ge-0/0/1
          ipv4:
          - address: 192.168.1.10/24
          ipv6:
          - address: 8d8d:8d01::1/64
        - name: ge-0/0/2
          ipv4:
          - address: dhcp
        state: merged

    # After state:
    # ------------
    #
    # admin# show interfaces
    # ge-0/0/1 {
    #     description "L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 10.200.16.10/24;
    #             address 192.168.1.10/24;
    #         }
    #         family inet6 {
    #             address 8d8d:8d01::1/64;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     description "L3 interface with dhcp";
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }


    # Using overridden

    # Before state
    # ------------
    #
    # admin# show interfaces
    # ge-0/0/1 {
    #     description "L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 10.200.16.10/24;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     description "L3 interface with dhcp";
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # ge-0/0/3 {
    #     description "another L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 192.168.1.10/24;
    #         }
    #     }
    # }

    - name: Override provided configuration with device configuration
      junipernetworks.junos.junos_l3_interfaces:
        config:
        - name: ge-0/0/1
          ipv4:
          - address: 192.168.1.10/24
          ipv6:
          - address: 8d8d:8d01::1/64
        - name: ge-0/0/2
          ipv6:
          - address: 2001:db8:3000::/64
        state: overridden

    # After state:
    # ------------
    #
    # admin# show interfaces
    # ge-0/0/1 {
    #     description "L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 192.168.1.10/24;
    #         }
    #         family inet6 {
    #             address 8d8d:8d01::1/64;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     description "L3 interface with ipv6";
    #     unit 0 {
    #         family inet6 {
    #             address 2001:db8:3000::/64;
    #         }
    #     }
    # }
    # ge-0/0/3 {
    #     description "overridden L3 interface";
    #     unit 0;
    # }


    # Using replaced

    # Before state
    # ------------
    #
    # admin# show interfaces
    # ge-0/0/1 {
    #     description "L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 10.200.16.10/24;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     description "non configured interface";
    #     unit 0;
    # }
    # ge-0/0/3 {
    #     description "another L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 192.168.1.10/24;
    #         }
    #     }
    # }

    - name: Replace provided configuration with device configuration
      junipernetworks.junos.junos_l3_interfaces:
        config:
        - name: ge-0/0/1
          ipv4:
          - address: 192.168.1.10/24
          ipv6:
          - address: 8d8d:8d01::1/64
        - name: ge-0/0/2
          ipv4:
          - address: dhcp
        state: replaced

    # After state:
    # ------------
    #
    # admin# show interfaces
    # ge-0/0/1 {
    #     description "L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 192.168.1.10/24;
    #         }
    #         family inet6 {
    #             address 8d8d:8d01::1/64;
    #         }
    #     }
    # }
    # ge-0/0/2 {
    #     description "L3 interface with dhcp";
    #     unit 0 {
    #         family inet {
    #             dhcp;
    #         }
    #     }
    # }
    # ge-0/0/3 {
    #     description "another L3 interface";
    #     unit 0 {
    #         family inet {
    #             address 192.168.1.10/24;
    #         }
    #     }
    # }
    # Using gathered
    # Before state:
    # ------------
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
    # ge-1/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.1/24;
    #             address 10.200.16.20/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ge-2/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.2/24;
    #             address 10.200.16.21/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ge-3/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.3/24;
    #             address 10.200.16.22/24;
    #         }
    #         family inet6;
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
    - name: Gather junos layer3 interfaces as in given arguments
      junipernetworks.junos.junos_l3_interfaces:
        state: gathered
    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": [
    #             {
    #                 "ipv4": [
    #                     {
    #                         "address": "192.168.100.1/24"
    #                     },
    #                     {
    #                         "address": "10.200.16.20/24"
    #                     }
    #                 ],
    #                 "name": "ge-1/0/0",
    #                 "unit": "0"
    #             },
    #             {
    #                 "ipv4": [
    #                     {
    #                         "address": "192.168.100.2/24"
    #                     },
    #                     {
    #                         "address": "10.200.16.21/24"
    #                     }
    #                 ],
    #                 "name": "ge-2/0/0",
    #                 "unit": "0"
    #             },
    #             {
    #                 "ipv4": [
    #                     {
    #                         "address": "192.168.100.3/24"
    #                     },
    #                     {
    #                         "address": "10.200.16.22/24"
    #                     }
    #                 ],
    #                 "name": "ge-3/0/0",
    #                 "unit": "0"
    #             },
    #             {
    #                 "ipv4": [
    #                     {
    #                         "address": "10.8.38.38/24"
    #                     }
    #                 ],
    #                 "name": "fxp0",
    #                 "unit": "0"
    #             }
    #         ]
    # After state:
    # ------------
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
    # ge-1/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.1/24;
    #             address 10.200.16.20/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ge-2/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.2/24;
    #             address 10.200.16.21/24;
    #         }
    #         family inet6;
    #     }
    # }
    # ge-3/0/0 {
    #     unit 0 {
    #         family inet {
    #             address 192.168.100.3/24;
    #             address 10.200.16.22/24;
    #         }
    #         family inet6;
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
    # Using parsed
    # parsed.cfg
    # ------------
    #
    # <?xml version="1.0" encoding="UTF-8"?>
    # <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
    #     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
    #         <interfaces>
    #             <interface>
    #                 <name>ge-1/0/0</name>
    #                 <unit>
    #                     <name>0</name>
    #                     <family>
    #                         <inet>
    #                             <address>
    #                                 <name>192.168.100.1/24</name>
    #                             </address>
    #                             <address>
    #                                 <name>10.200.16.20/24</name>
    #                             </address>
    #                         </inet>
    #                         <inet6></inet6>
    #                     </family>
    #                 </unit>
    #             </interface>
    #             <interface>
    #                 <name>ge-2/0/0</name>
    #                 <unit>
    #                     <name>0</name>
    #                     <family>
    #                         <inet>
    #                             <address>
    #                                 <name>192.168.100.2/24</name>
    #                             </address>
    #                             <address>
    #                                 <name>10.200.16.21/24</name>
    #                             </address>
    #                         </inet>
    #                         <inet6></inet6>
    #                     </family>
    #                 </unit>
    #             </interface>
    #         </interfaces>
    #     </configuration>
    # </rpc-reply>
    # - name: Convert interfaces config to argspec without connecting to the appliance
    #   junipernetworks.junos.junos_l3_interfaces:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed
    # Task Output (redacted)
    # -----------------------
    # "parsed": [
    #         {
    #             "ipv4": [
    #                 {
    #                     "address": "192.168.100.1/24"
    #                 },
    #                 {
    #                     "address": "10.200.16.20/24"
    #                 }
    #             ],
    #             "name": "ge-1/0/0",
    #             "unit": "0"
    #         },
    #         {
    #             "ipv4": [
    #                 {
    #                     "address": "192.168.100.2/24"
    #                 },
    #                 {
    #                     "address": "10.200.16.21/24"
    #                 }
    #             ],
    #             "name": "ge-2/0/0",
    #             "unit": "0"
    #         }
    #     ]
    #
    # Using rendered
    - name: Render platform specific xml from task input using rendered state
      junipernetworks.junos.junos_l3_interfaces:
        config:
          - name: ge-1/0/0
            ipv4:
              - address: 192.168.100.1/24
              - address: 10.200.16.20/24
            unit: 0

          - name: ge-2/0/0
            ipv4:
              - address: 192.168.100.2/24
              - address: 10.200.16.21/24
            unit: 0
        state: rendered
    # Task Output (redacted)
    # -----------------------
    # "rendered": "<nc:interfaces
    #     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    #     <nc:interface>
    #         <nc:name>ge-1/0/0</nc:name>
    #         <nc:unit>
    #             <nc:name>0</nc:name>
    #             <nc:family>
    #                 <nc:inet>
    #                     <nc:address>
    #                         <nc:name>192.168.100.1/24</nc:name>
    #                     </nc:address>
    #                     <nc:address>
    #                         <nc:name>10.200.16.20/24</nc:name>
    #                     </nc:address>
    #                 </nc:inet>
    #             </nc:family>
    #         </nc:unit>
    #     </nc:interface>
    #     <nc:interface>
    #         <nc:name>ge-2/0/0</nc:name>
    #         <nc:unit>
    #             <nc:name>0</nc:name>
    #             <nc:family>
    #                 <nc:inet>
    #                     <nc:address>
    #                         <nc:name>192.168.100.2/24</nc:name>
    #                     </nc:address>
    #                     <nc:address>
    #                         <nc:name>10.200.16.21/24</nc:name>
    #                     </nc:address>
    #                 </nc:inet>
    #             </nc:family>
    #         </nc:unit>
    #     </nc:interface>
    # </nc:interfaces>"



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The configuration as structured data after module completion.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration as structured data prior to module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;nc:interfaces xmlns:nc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;nc:interface&gt; &lt;nc:name&gt;ge-1/0/0&lt;/nc:name&gt; &lt;nc:unit&gt; &lt;nc:name&gt;0&lt;/nc:name&gt; &lt;nc:family&gt; &lt;nc:inet&gt; &lt;nc:address&gt; &lt;nc:name&gt;192.168.100.1/24&lt;/nc:name&gt; &lt;/nc:address&gt; &lt;nc:address&gt; &lt;nc:name&gt;10.200.16.20/24&lt;/nc:name&gt; &lt;/nc:address&gt; &lt;/nc:inet&gt; &lt;/nc:family&gt; &lt;/nc:unit&gt; &lt;/nc:interfaces&gt;&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Daniel Mellado (@dmellado)
