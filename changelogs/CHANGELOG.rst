==============================================
Junipernetworks Junos Collection Release Notes
==============================================

.. contents:: Topics


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
