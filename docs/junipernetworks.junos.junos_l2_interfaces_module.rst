.. _junipernetworks.junos.junos_l2_interfaces_module:


*****************************************
junipernetworks.junos.junos_l2_interfaces
*****************************************

**L2 interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of a Layer-2 interface on Juniper JUNOS devices.



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
                                            <div>A dictionary of Layer-2 interface options</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Configure the interface as a Layer 2 access mode.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Configure the access VLAN ID.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enhanced_layer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>True if your device has Enhanced Layer 2 Software (ELS). If the l2 configuration is under <code>interface-mode</code> the value is True else if the l2 configuration is under <code>port-mode</code> value is False</div>
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
                                            <div>Full name of interface, e.g. ge-0/0/1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trunk</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Configure the interface as a Layer 2 trunk mode.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allowed_vlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of VLANs to be configured in trunk port. It&#x27;s used as the VLAN range to ADD or REMOVE from the trunk.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>native_vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Native VLAN to be configured in trunk port. It is used as the trunk native VLAN ID.</div>
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
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Logical interface number. Value of <code>unit</code> should be of type integer.</div>
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
   - This module requires the netconf system service be enabled on the remote device being managed.
   - Tested against vSRX JUNOS version 18.4R1.
   - This module works with connection ``netconf``. See `the Junos OS Platform Options <../network/user_guide/platform_junos.html>`_.



Examples
--------

.. code-block:: yaml+jinja

    
    # Using deleted

    # Before state:
    # -------------
    #
    # ansible@junos01# show interfaces
    # ge-0/0/1 {
    #    description "L2 interface";
    #    speed 1g;
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode access;
    #            vlan {
    #                members vlan30;
    #            }
    #        }
    #    }
    #}
    #ge-0/0/2 {
    #    description "non L2 interface";
    #    unit 0 {
    #        family inet {
    #            address 192.168.56.14/24;
    #        }
    #    }

    - name: "Delete L2 attributes of given interfaces (Note: This won't delete the
        interface itself)."
      junipernetworks.junos.junos_l2_interfaces:
        config:
        - name: ge-0/0/1
        - name: ge-0/0/2
        state: deleted

    # After state:
    # ------------
    #
    # ansible@junos01# show interfaces
    # ge-0/0/1 {
    #    description "L2 interface";
    #    speed 1g;
    # }
    #ge-0/0/2 {
    #    description "non L2 interface";
    #    unit 0 {
    #        family inet {
    #            address 192.168.56.14/24;
    #        }
    #    }


    # Using merged

    # Before state:
    # -------------
    # ansible@junos01# show interfaces
    # ge-0/0/3 {
    #    description "test interface";
    #    speed 1g;
    #}
    # ge-0/0/4 {
    #    description interface-trunk;
    #    native-vlan-id 100;
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode trunk;
    #            vlan {
    #                members [ vlan40 ];
    #            }
    #        }
    #    }
    # }

    - name: Merge provided configuration with device configuration (default operation
        is merge)
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

    # After state:
    # ------------
    # user@junos01# show interfaces
    # ge-0/0/3 {
    #    description "test interface";
    #    speed 1g;
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode access;
    #            vlan {
    #                members v101;
    #            }
    #        }
    #    }
    # }
    # ge-0/0/4 {
    #    description interface-trunk;
    #    native-vlan-id 50;
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode trunk;
    #            vlan {
    #                members [ vlan40 vlan30 ];
    #            }
    #        }
    #    }
    # }


    # Using overridden

    # Before state:
    # -------------
    # ansible@junos01# show interfaces
    # ge-0/0/3 {
    #    description "test interface";
    #    speed 1g;
    #}
    # ge-0/0/4 {
    #    description interface-trunk;
    #    native-vlan-id 100;
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode trunk;
    #            vlan {
    #                members [ vlan40 ];
    #            }
    #        }
    #    }
    # }
    # ge-0/0/5 {
    #    description "Configured by Ansible-11";
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode access;
    #            vlan {
    #                members v101;
    #            }
    #        }
    #    }
    # }

    - name: Override provided configuration with device configuration
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
        state: overridden

    # After state:
    # ------------
    # user@junos01# show interfaces
    # ge-0/0/3 {
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode access;
    #            vlan {
    #                members v101;
    #            }
    #        }
    #    }
    # }
    # ge-0/0/4 {
    #    description interface-trunk;
    #    native-vlan-id 50;
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode trunk;
    #            vlan {
    #                members [ vlan30 ];
    #            }
    #        }
    #    }
    # }


    # Using replaced

    # Before state:
    # -------------
    # ansible@junos01# show interfaces
    # ge-0/0/3 {
    #    description "test interface";
    #    speed 1g;
    #}
    # ge-0/0/4 {
    #    description interface-trunk;
    #    native-vlan-id 100;
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode trunk;
    #            vlan {
    #                members [ vlan40 ];
    #            }
    #        }
    #    }
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

    # After state:
    # ------------
    # user@junos01# show interfaces
    # ge-0/0/3 {
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode access;
    #            vlan {
    #                members v101;
    #            }
    #        }
    #    }
    # }
    # ge-0/0/4 {
    #    description interface-trunk;
    #    native-vlan-id 50;
    #    unit 0 {
    #        family ethernet-switching {
    #            interface-mode trunk;
    #            vlan {
    #                members [ vlan30 ];
    #            }
    #        }
    #    }
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

- Ganesh Nalawade (@ganeshrn)


