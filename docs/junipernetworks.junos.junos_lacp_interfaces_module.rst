.. _junipernetworks.junos.junos_lacp_interfaces_module:


*******************************************
junipernetworks.junos.junos_lacp_interfaces
*******************************************

**LACP interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages Link Aggregation Control Protocol (LACP) attributes of interfaces on Juniper JUNOS devices.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="4">
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
                                            <div>The list of dictionaries of LACP interfaces options.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>force_up</b>
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
                                            <div>This is a boolean argument to control if the port should be up in absence of received link Aggregation Control Protocol Data Unit (LACPDUS). This value is applicable for member interfaces only.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name Identifier of the interface or link aggregation group.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>period</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>fast</li>
                                                                                                                                                                                                <li>slow</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Timer interval for periodic transmission of LACP packets. If the value is set to <code>fast</code> the packets are received every second and if the value is <code>slow</code> the packets are received every 30 seconds. This value is applicable for aggregate interface only.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Priority of the member port. This value is applicable for member interfaces only.</div>
                                            <div>Refer to vendor documentation for valid values.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sync_reset</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>disable</li>
                                                                                                                                                                                                <li>enable</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The argument notifies minimum-link failure out of sync to peer. If the value is <code>disable</code> it disables minimum-link failure handling at LACP level and if value is <code>enable</code> it enables minimum-link failure handling at LACP level. This value is applicable for aggregate interface only.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This dict object contains configurable options related to LACP system parameters for the link aggregation group. This value is applicable for aggregate interface only.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the system ID to use in LACP negotiations for the bundle, encoded as a MAC address.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
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
                                            <div>The system ID to use in LACP negotiations.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the system priority to use in LACP negotiations for the bundle.</div>
                                            <div>Refer to vendor documentation for valid values.</div>
                                                        </td>
            </tr>
                    
                                    
                                                <tr>
                                                                <td colspan="4">
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
                                            <div>The state of the configuration after module completion.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>




Examples
--------

.. code-block:: yaml+jinja

    
    # Using merged
    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #    ether-options {
    #         802.3ad ae0;
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    - name: Merge provided configuration with device configuration
      junipernetworks.junos.junos_lacp_interfaces:
        config:
        - name: ae0
          period: fast
          sync_reset: enable
          system:
            priority: 100
            mac:
              address: 00:00:00:00:00:02
        - name: ge-0/0/3
          port_priority: 100
          force_up: true
        state: merged

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             periodic fast;
    #             sync-reset enable;
    #             system-priority 100;
    #             system-id 00:00:00:00:00:02;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    # Using replaced
    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             periodic fast;
    #             sync-reset enable;
    #             system-priority 100;
    #             system-id 00:00:00:00:00:02;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    - name: Replace device LACP interfaces configuration with provided configuration
      junipernetworks.junos.junos_lacp_interfaces:
        config:
        - name: ae0
          period: slow
        state: replaced

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             periodic slow;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    # Using overridden
    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             periodic slow;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    - name: Overrides all device LACP interfaces configuration with provided configuration
      junipernetworks.junos.junos_lacp_interfaces:
        config:
        - name: ae0
          system:
            priority: 300
            mac:
              address: 00:00:00:00:00:03
        - name: ge-0/0/2
          port_priority: 200
          force_up: false
        state: overridden

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 port-priority 200;
    #             }
    #             ae4;
    #         }
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             system-priority 300;
    #             system-id 00:00:00:00:00:03;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    # Using deleted
    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 port-priority 200;
    #             }
    #             ae4;
    #         }
    #     }
    # }
    # ge-0/0/3 {
    #     ether-options {
    #         802.3ad {
    #             lacp {
    #                 force-up;
    #                 port-priority 100;
    #             }
    #             ae0;
    #         }
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             system-priority 300;
    #             system-id 00:00:00:00:00:03;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
    #         }
    #     }
    # }

    - name: "Delete LACP interfaces attributes of given interfaces (Note: This won't delete the interface itself)"
      junipernetworks.junos.junos_lacp_interfaces:
        config:
        - name: ae0
        - name: ge-0/0/3
        - name: ge-0/0/2
        state: deleted

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #     ether-options {
    #         802.3ad ae4;
    #     }
    # }
    # ge-0/0/3 {
    #    ether-options {
    #         802.3ad ae0;
    #     }
    # }
    # ae0 {
    #     description "lag interface merged";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #         }
    #     }
    # }
    # ae4 {
    #     description "test aggregate interface";
    #     aggregated-ether-options {
    #         lacp {
    #             passive;
    #             link-protection;
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

- Ganesh Nalawade (@ganeshrn)


