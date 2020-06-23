.. _junipernetworks.junos.junos_lag_interfaces_module:


******************************************
junipernetworks.junos.junos_lag_interfaces
******************************************

**Link Aggregation Juniper JUNOS resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages properties of Link Aggregation Group on Juniper JUNOS devices.



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
                                            <div>A list of link aggregation group configurations.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_protection</b>
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
                                            <div>This boolean option indicates if link protection should be enabled for the LAG interface. If value is <code>True</code> link protection is enabled on LAG and if value is <code>False</code> link protection is disabled.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of member interfaces of the link aggregation group. The value can be single interface or list of interfaces.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>primary</li>
                                                                                                                                                                                                <li>backup</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The value of this options configures the member link as either <code>primary</code> or <code>backup</code>. Value <code>primary</code> configures primary interface for link-protection mode and <code>backup</code> configures backup interface for link-protection mode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>member</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the member interface.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>active</li>
                                                                                                                                                                                                <li>passive</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>LAG mode. A value of <code>passive</code> will enable LACP in <code>passive</code> mode that is it will respond to LACP packets and <code>active</code> configures the link to initiate transmission of LACP packets.</div>
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
                                            <div>Name of the link aggregation group (LAG).</div>
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

    
    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ae0 {
    #     description "lag interface";
    # }
    # ae1 {
    #     description "lag interface 1";
    # }

    - name: "Delete LAG attributes of given interfaces (Note: This won't delete the interface itself)"
      junipernetworks.junos.junos_lag_interfaces:
        config:
        - name: ae0
        - name: ae1
        state: deleted

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    # }


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    # }

    - name: Merge provided configuration with device configuration
      junipernetworks.junos.junos_lag_interfaces:
        config:
        - name: ae0
          members:
          - member: ge-0/0/1
            link_type: primary
          - member: ge-0/0/2
            link_type: backup
        state: merged

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad {
    #            ae0;
    #            primary;
    #        }
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    #    ether-options {
    #        802.3ad {
    #            ae0;
    #            backup;
    #        }
    #    }
    # }


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ae0 {
    #     description "lag interface";
    # }
    # ae3 {
    #     description "lag interface 3";
    # }

    - name: Overrides all device LAG configuration with provided configuration
      junipernetworks.junos.junos_lag_interfaces:
        config:
        - name: ae0
          members:
          - member: ge-0/0/2
        - name: ae1
          members:
          - member: ge-0/0/1
          mode: passive
        state: overridden

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad ae1;
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ae0 {
    #     description "lag interface";
    # }
    # ae1 {
    #    aggregated-ether-options {
    #        lacp {
    #            active;
    #        }
    #    }
    # }


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    # }
    # ge-0/0/3 {
    #    description "Ansible configured interface 3";
    # }

    - name: Replace device LAG configuration with provided configuration
      junipernetworks.junos.junos_lag_interfaces:
        config:
        - name: ae0
          members:
          - member: ge-0/0/1
          mode: active
        state: replaced

    # After state:
    # -------------
    # user@junos01# show interfaces
    # ge-0/0/1 {
    #    description "Ansible configured interface 1";
    #    ether-options {
    #        802.3ad ae0;
    #    }
    # }
    # ge-0/0/2 {
    #    description "Ansible configured interface 2";
    # }
    # ae0 {
    #    aggregated-ether-options {
    #        lacp {
    #            active;
    #        }
    #    }
    # }
    # ge-0/0/3 {
    #    description "Ansible configured interface 3";
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


