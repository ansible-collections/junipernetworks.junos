.. _junipernetworks.junos.junos_lacp_module:


********************************
junipernetworks.junos.junos_lacp
********************************

**Global Link Aggregation Control Protocol (LACP) Junos resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of global LACP on Juniper Junos network devices.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A dictionary of LACP global options</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_protection</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>revertive</li>
                                                                                                                                                                                                <li>non-revertive</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Enable LACP link-protection for the system. If the value is set to <code>non-revertive</code> it will not revert links when a better priority link comes up. By default the link will be reverted.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>LACP priority for the system.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
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
   - Tested against vSRX JUNOS version 18.1R1.
   - This module works with connection ``netconf``. See `the Junos OS Platform Options <../network/user_guide/platform_junos.html>`_.



Examples
--------

.. code-block:: yaml+jinja

    
    # Using deleted

    # Before state:
    # -------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    # system-priority 63;
    # link-protection {
    #    non-revertive;
    # }

    - name: Delete global LACP attributes
      junipernetworks.junos.junos_lacp:
        state: deleted

    # After state:
    # ------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    #


    # Using merged

    # Before state:
    # -------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    #

    - name: Merge global LACP attributes
      junipernetworks.junos.junos_lacp:
        config:
          system_priority: 63
          link_protection: revertive
        state: merged

    # After state:
    # ------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    # system-priority 63;
    # link-protection {
    #    non-revertive;
    # }


    # Using replaced

    # Before state:
    # -------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    # system-priority 63;
    # link-protection {
    #    non-revertive;
    # }

    - name: Replace global LACP attributes
      junipernetworks.junos.junos_lacp:
        config:
          system_priority: 30
          link_protection: non-revertive
        state: replaced

    # After state:
    # ------------
    # user@junos01# show chassis aggregated-devices ethernet lacp
    # system-priority 30;
    # link-protection;






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
                      <span style="color: purple">dictionary</span>
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
                      <span style="color: purple">dictionary</span>
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


