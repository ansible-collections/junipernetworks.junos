==============================================
Junipernetworks Junos Collection Release Notes
==============================================

.. contents:: Topics


v1.3.0
======

Minor Changes
-------------

- Add junos bgp global resource module.
- Add ospf interfaces resource module.

Bugfixes
--------

- changing prefix list type to list and correcting facts gathering (https://github.com/ansible-collections/junipernetworks.junos/issues/131)
- constructing the facts based on the addresses per unit (https://github.com/ansible-collections/junipernetworks.junos/issues/111)
- release version added updated to 1.3.0 for junos_ospf_interfaces and junos_bgp_global module

New Modules
-----------

- junos_bgp_global - Manages BGP Global configuration on devices running Juniper JUNOS.
- junos_ospf_interfaces - OSPF Interfaces Resource Module.

v1.2.1
======

Bugfixes
--------

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Updating unit tests for resource modules (https://github.com/ansible-collections/junipernetworks.junos/pull/127)
- allowing partial config filter for junos commands (https://github.com/ansible-collections/junipernetworks.junos/issues/112)
- checking for units and family attributes in conf dictionary (https://github.com/ansible-collections/junipernetworks.junos/issues/121)

v1.2.0
======

Minor Changes
-------------

- Add ospfv3 resource module.

New Modules
-----------

- junos_ospfv3 - OSPFv3 resource module

v1.1.1
======

Minor Changes
-------------

- Use FQCN to M() references in modules documentation (https://github.com/ansible-collections/junipernetworks.junos/pull/79)

v1.1.0
======

Minor Changes
-------------

- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lacp.
- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lldp_global.
- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lldp_interfaces.
- Gathered state operation enabled, Parsed and rendered state operations implemented for ospfv2, acl_interfaces, vlans and static_routes RM.
- Gathered state operation enabled. Parsed and rendered state operations implemented.
- Gathered state operation enabledand Parsed and rendered state operations implemented.

Bugfixes
--------

- set_config called only when state is not gathered so that gathered opeartion works fine (https://github.com/ansible-collections/junipernetworks.junos/issues/89).
- set_config called only when state is not gathered so that gathered opeartion works fine (https://github.com/ansible-collections/junipernetworks.junos/issues/93).
- set_config called only when state is not gathered so that gathered opeartion works fine for l2_interfaces resource module (https://github.com/ansible-collections/junipernetworks.junos/issues/91).

v1.0.1
======

Bugfixes
--------

- Make `src`, `backup` and `backup_options` in junos_config work when module alias is used (https://github.com/ansible-collections/junipernetworks.junos/pull/83).
- Update docs after sanity fixes to modules.

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- junos - Use junos cliconf to run command on Juniper Junos OS platform

Netconf
~~~~~~~

- junos - Use junos netconf plugin to run netconf commands on Juniper JUNOS platform

New Modules
-----------

- junos_acl_interfaces - ACL interfaces resource module
- junos_acls - ACLs resource module
- junos_banner - Manage multiline banners on Juniper JUNOS devices
- junos_command - Run arbitrary commands on an Juniper JUNOS device
- junos_config - Manage configuration on devices running Juniper JUNOS
- junos_facts - Collect facts from remote devices running Juniper Junos
- junos_interface - (deprecated, removed after 2022-06-01) Manage Interface on Juniper JUNOS network devices
- junos_interfaces - Junos Interfaces resource module
- junos_l2_interface - (deprecated, removed after 2022-06-01) Manage L2 Interface on Juniper JUNOS network devices
- junos_l2_interfaces - L2 interfaces resource module
- junos_l3_interface - (deprecated, removed after 2022-06-01) Manage L3 interfaces on Juniper JUNOS network devices
- junos_l3_interfaces - L3 interfaces resource module
- junos_lacp - Global Link Aggregation Control Protocol (LACP) Junos resource module
- junos_lacp_interfaces - LACP interfaces resource module
- junos_lag_interfaces - Link Aggregation Juniper JUNOS resource module
- junos_linkagg - (deprecated, removed after 2022-06-01) Manage link aggregation groups on Juniper JUNOS network devices
- junos_lldp - (deprecated, removed after 2022-06-01) Manage LLDP configuration on Juniper JUNOS network devices
- junos_lldp_global - LLDP resource module
- junos_lldp_interface - (deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration on Juniper JUNOS network devices
- junos_lldp_interfaces - LLDP interfaces resource module
- junos_logging - Manage logging on network devices
- junos_netconf - Configures the Junos Netconf system service
- junos_ospfv2 - OSPFv2 resource module
- junos_package - Installs packages on remote devices running Junos
- junos_ping - Tests reachability using ping from devices running Juniper JUNOS
- junos_rpc - Runs an arbitrary RPC over NetConf on an Juniper JUNOS device
- junos_scp - Transfer files from or to remote devices running Junos
- junos_static_route - (deprecated, removed after 2022-06-01) Manage static IP routes on Juniper JUNOS network devices
- junos_static_routes - Static routes resource module
- junos_system - Manage the system attributes on Juniper JUNOS devices
- junos_user - Manage local user accounts on Juniper JUNOS devices
- junos_vlan - (deprecated, removed after 2022-06-01) Manage VLANs on Juniper JUNOS network devices
- junos_vlans - VLANs resource module
- junos_vrf - Manage the VRF definitions on Juniper JUNOS devices
