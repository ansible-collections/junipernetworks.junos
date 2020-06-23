.. _junipernetworks.junos.junos_interfaces_module:


**************************************
junipernetworks.junos.junos_interfaces
**************************************

**Junos Interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the interfaces on Juniper Junos OS network devices.



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
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The provided configuration</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Interface description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>duplex</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>automatic</li>
                                                                                                                                                                                                <li>full-duplex</li>
                                                                                                                                                                                                <li>half-duplex</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Interface link status. Applicable for Ethernet interfaces only, either in half duplex, full duplex or in automatic state which negotiates the duplex automatically.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Administrative state of the interface.</div>
                                            <div>Set the value to <code>true</code> to administratively enabled the interface or <code>false</code> to disable it.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hold_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The hold time for given interface name.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>down</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The link down hold time in milliseconds.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>up</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The link up hold time in milliseconds.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mtu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>MTU for a specific interface.</div>
                                            <div>Applicable for Ethernet interfaces only.</div>
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
                                            <div>Full name of interface, e.g. ge-0/0/0.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Interface link speed. Applicable for Ethernet interfaces only.</div>
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
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Configured by Ansible-1";
    #    speed 1g;
    #    mtu 1800
    # }
    # ge-0/0/2 {
    #    description "Configured by Ansible-2";
    #    ether-options {
    #        auto-negotiation;
    #    }
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

    # After state:
    # ------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #    ether-options {
    #        auto-negotiation;
    #    }
    # }


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "test interface";
    #    speed 1g;
    # }

    - name: Merge provided configuration with device configuration (default operation
        is merge)
      junipernetworks.junos.junos_interfaces:
        config:
        - name: ge-0/0/1
          description: Configured by Ansible-1
          enabled: true
          mtu: 1800
        - name: ge-0/0/2
          description: Configured by Ansible-2
          enabled: false
        state: merged

    # After state:
    # ------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Configured by Ansible-1";
    #    speed 1g;
    #    mtu 1800
    # }
    # ge-0/0/2 {
    #    disable;
    #    description "Configured by Ansible-2";
    # }


    # Using overridden

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Configured by Ansible-1";
    #    speed 1g;
    #    mtu 1800
    # }
    # ge-0/0/2 {
    #    disable;
    #    description "Configured by Ansible-2";
    #    ether-options {
    #        auto-negotiation;
    #    }
    # }
    # ge-0/0/11 {
    #    description "Configured by Ansible-11";
    # }

    - name: Override device configuration of all interfaces with provided configuration
      junipernetworks.junos.junos_interfaces:
        config:
        - name: ge-0/0/2
          description: Configured by Ansible-2
          enabled: false
          mtu: 2800
        - name: ge-0/0/3
          description: Configured by Ansible-3
        state: overridden

    # After state:
    # ------------
    # user@junos01# show interfaces
    # ge-0/0/2 {
    #    disable;
    #    description "Configured by Ansible-2";
    #    mtu 2800
    # }
    # ge-0/0/3 {
    #    description "Configured by Ansible-3";
    # }


    # Using replaced

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Configured by Ansible-1";
    #    speed 1g;
    #    mtu 1800
    # }
    # ge-0/0/2 {
    #    disable;
    #    mtu 1800;
    #    speed 1g;
    #    description "Configured by Ansible-2";
    #    ether-options {
    #        auto-negotiation;
    #    }
    # }
    # ge-0/0/11 {
    #    description "Configured by Ansible-11";
    # }

    - name: Replaces device configuration of listed interfaces with provided configuration
      junipernetworks.junos.junos_interfaces:
        config:
        - name: ge-0/0/2
          description: Configured by Ansible-2
          enabled: false
          mtu: 2800
        - name: ge-0/0/3
          description: Configured by Ansible-3
        state: replaced

    # After state:
    # ------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Configured by Ansible-1";
    #    speed 1g;
    #    mtu 1800
    # }
    # ge-0/0/2 {
    #    disable;
    #    description "Configured by Ansible-2";
    #    mtu 2800
    # }
    # ge-0/0/3 {
    #    description "Configured by Ansible-3";
    # }
    # ge-0/0/11 {
    #    description "Configured by Ansible-11";
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
                    <b>xml</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                                                        <div>The set of xml rpc payload pushed to the remote device.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;xml 1&#x27;, &#x27;xml 2&#x27;, &#x27;xml 3&#x27;]</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)


