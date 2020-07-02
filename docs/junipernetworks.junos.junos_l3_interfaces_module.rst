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
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
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
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
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
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
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
                                                 / <span style="color: red">required</span>                    </div>
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

.. code-block:: yaml+jinja

    
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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;command 1&#x27;, &#x27;command 2&#x27;, &#x27;command 3&#x27;]</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Daniel Mellado (@dmellado)


