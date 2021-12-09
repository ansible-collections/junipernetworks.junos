==============================================
Junipernetworks Junos Collection Release Notes
==============================================

.. contents:: Topics


v2.8.0
======

Minor Changes
-------------

- Add junos_routing_options resource module.
- Add junos_snmp_server resource module.

Deprecated Features
-------------------

- 'router_id' options is deprecated from junos_ospf_interfaces, junos_ospfv2 and junos_ospfv3 resuorce module.

New Modules
-----------

- junos_routing_options - Manage routing-options configuration on Junos devices.

v2.7.1
======

Bugfixes
--------

- Fix ospf router_id overlap issue.

v2.7.0
======

Documentation Changes
---------------------

- Add note for router_id deprecation from ospf-interfaces resource module.
- make sure router_id facts and config operation works fine for ospfv2 and ospfv3 RM

v2.6.0
======

Minor Changes
-------------

- Add junos_ntp_global resource module.

Deprecated Features
-------------------

- Deprecated router_id from ospfv2 resource module.

New Modules
-----------

- junos_ntp_global - Manage NTP configuration on Junos devices.

v2.5.0
======

Minor Changes
-------------

- Improve junos ospfv2 integration and unit tests coverage and router id assignment check implemented.
- Improve junos vlans integration and unit tests coverage and facts gathering logic modification.

Deprecated Features
-------------------

- Deprecated router_id from ospfv3 resource module.

v2.4.0
======

Minor Changes
-------------

- Add junos_logging_global Resource Module.
- Add support for backup_format option in junos_config
- support l3_interface in junos vlans

Deprecated Features
-------------------

- The junos_logging module has been deprecated in favor of the new junos_logging_global resource module and will be removed in a release after '2023-08-01'.

Bugfixes
--------

- fix lacp force-up without port-priority in junos_lacp_interfaces
- fix netconf test-case for lacp revert
- junos_acls failed to parse acl when multiple addresses defined within a single term (https://github.com/ansible-collections/junipernetworks.junos/issues/190)

New Modules
-----------

- junos_logging_global - Manage logging configuration on Junos devices.

v2.3.0
======

Minor Changes
-------------

- Add junos_prefix_lists Resource Module.

v2.2.0
======

Minor Changes
-------------

- Change src element from str to path for junos_scp.
- Improve junos_bgp_address_family unit test coverage.

v2.1.0
======

Minor Changes
-------------

- Add junos_routing_instances Resource Module.
- Add support for available_network_resources key, which allows to fetch the available resources for a platform (https://github.com/ansible-collections/junipernetworks.junos/issues/160).
- Replace unsupported parameter `vlan-id` in junipernetworks.junos.junos_vlans module with `vlan_id`

Security Fixes
--------------

- Mask values of sensitive keys in module result(https://github.com/ansible-collections/junipernetworks.junos/issues/165).

New Modules
-----------

- junos_routing_instances - Manage routing instances on Junos devices.

v2.0.1
======

Minor Changes
-------------

- Add support df_bit and size option for junos_ping (https://github.com/ansible-collections/junipernetworks.junos/pull/136).

v2.0.0
======

Major Changes
-------------

- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.
- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.

Minor Changes
-------------

- Add junos_bgp_address_family resource module.
- Add support for autonomous-system routing-options for bgp global and updating tests and documentation.
- Add support for bgp group and neighbors in bgp_global resource module.
- Add support for configuration caching (single_user_mode).
- Re-use device_info dictionary in cliconf.

New Modules
-----------

- junos_bgp_address_family - Manage BGP Address Family attributes of interfaces on Junos devices.

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
