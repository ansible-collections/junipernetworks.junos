# Juniper Networks Junos Collection

> **⚠️ DEPRECATION NOTICE ⚠️**
>
> **This collection is deprecated and will be removed in version 12.0.0 (scheduled for October 30, 2027).**
>
> **Please migrate to the [juniper.device](https://github.com/Juniper/ansible-junos-stdlib/tree/master/ansible_collections/juniper/device) collection.**
>
> All modules in this collection now redirect to their equivalents in `juniper.device`. The redirects will continue to work until the removal date to ensure backward compatibility.

[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/project/github.com/ansible-collections/junipernetworks.junos) <!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/vyos)](https://codecov.io/gh/ansible-collections/junipernetworks.junos)-->
[![Codecov](https://codecov.io/gh/ansible-collections/junipernetworks.junos/branch/main/graph/badge.svg)](https://codecov.io/gh/ansible-collections/junipernetworks.junos)
[![CI](https://github.com/ansible-collections/junipernetworks.junos/actions/workflows/tests.yml/badge.svg?branch=main&event=schedule)](https://github.com/ansible-collections/junipernetworks.junos/actions/workflows/tests.yml)

The Ansible Juniper Networks Junos collection includes a variety of Ansible content to help automate the management of Juniper Networks Junos network appliances.

This collection has been tested against Juniper Networks Junos OS 18.4R1.

## Support

As a Red Hat Ansible [Certified Content](https://catalog.redhat.com/software/search?target_platforms=Red%20Hat%20Ansible%20Automation%20Platform), this collection is entitled to [support](https://access.redhat.com/support/) through [Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible) (AAP).

If a support case cannot be opened with Red Hat and the collection has been obtained either from [Galaxy](https://galaxy.ansible.com/ui/) or [GitHub](https://github.com/ansible-collections/junipernetworks.junos), there is community support available at no charge.

You can join us on [#network:ansible.com](https://matrix.to/#/#network:ansible.com) room or the [Ansible Forum Network Working Group](https://forum.ansible.com/g/network-wg).

For more information you can check the communication section below.

## Migration Guide

### Module Migration Table

The following table shows the mapping between deprecated modules in this collection and their replacements in `juniper.device`:

| Deprecated Module (junipernetworks.junos) | New Module (juniper.device) |
|-------------------------------------------|------------------------------|
| `junipernetworks.junos.junos_acl_interfaces` | `juniper.device.junos_acl_interfaces` |
| `junipernetworks.junos.junos_acls` | `juniper.device.junos_acls` |
| `junipernetworks.junos.junos_banner` | `juniper.device.junos_banner` |
| `junipernetworks.junos.junos_bgp_address_family` | `juniper.device.junos_bgp_address_family` |
| `junipernetworks.junos.junos_bgp_global` | `juniper.device.junos_bgp_global` |
| `junipernetworks.junos.junos_command` | `juniper.device.junos_command` |
| `junipernetworks.junos.junos_config` | `juniper.device.junos_config` |
| `junipernetworks.junos.junos_facts` | `juniper.device.junos_facts` |
| `junipernetworks.junos.junos_hostname` | `juniper.device.junos_hostname` |
| `junipernetworks.junos.junos_interfaces` | `juniper.device.junos_interfaces` |
| `junipernetworks.junos.junos_l2_interfaces` | `juniper.device.junos_l2_interfaces` |
| `junipernetworks.junos.junos_l3_interfaces` | `juniper.device.junos_l3_interfaces` |
| `junipernetworks.junos.junos_lacp` | `juniper.device.junos_lacp` |
| `junipernetworks.junos.junos_lacp_interfaces` | `juniper.device.junos_lacp_interfaces` |
| `junipernetworks.junos.junos_lag_interfaces` | `juniper.device.junos_lag_interfaces` |
| `junipernetworks.junos.junos_lldp_global` | `juniper.device.junos_lldp_global` |
| `junipernetworks.junos.junos_lldp_interfaces` | `juniper.device.junos_lldp_interfaces` |
| `junipernetworks.junos.junos_logging_global` | `juniper.device.junos_logging_global` |
| `junipernetworks.junos.junos_netconf` | `juniper.device.junos_netconf` |
| `junipernetworks.junos.junos_ntp_global` | `juniper.device.junos_ntp_global` |
| `junipernetworks.junos.junos_ospf_interfaces` | `juniper.device.junos_ospf_interfaces` |
| `junipernetworks.junos.junos_ospfv2` | `juniper.device.junos_ospfv2` |
| `junipernetworks.junos.junos_ospfv3` | `juniper.device.junos_ospfv3` |
| `junipernetworks.junos.junos_package` | `juniper.device.junos_package` |
| `junipernetworks.junos.junos_ping` | `juniper.device.junos_ping` |
| `junipernetworks.junos.junos_prefix_lists` | `juniper.device.junos_prefix_lists` |
| `junipernetworks.junos.junos_routing_instances` | `juniper.device.junos_routing_instances` |
| `junipernetworks.junos.junos_routing_options` | `juniper.device.junos_routing_options` |
| `junipernetworks.junos.junos_rpc` | `juniper.device.junos_rpc` |
| `junipernetworks.junos.junos_security_policies` | `juniper.device.junos_security_policies` |
| `junipernetworks.junos.junos_security_policies_global` | `juniper.device.junos_security_policies_global` |
| `junipernetworks.junos.junos_security_zones` | `juniper.device.junos_security_zones` |
| `junipernetworks.junos.junos_snmp_server` | `juniper.device.junos_snmp_server` |
| `junipernetworks.junos.junos_static_routes` | `juniper.device.junos_static_routes` |
| `junipernetworks.junos.junos_system` | `juniper.device.junos_system` |
| `junipernetworks.junos.junos_user` | `juniper.device.junos_user` |
| `junipernetworks.junos.junos_vlans` | `juniper.device.junos_vlans` |
| `junipernetworks.junos.junos_vrf` | `juniper.device.junos_vrf` |

### Example Migration

**Before (using deprecated collection):**
```yaml
- name: Run show version command
  junipernetworks.junos.junos_command:
    commands:
      - show version
```

**After (using new collection):**
```yaml
- name: Run show version command
  juniper.device.junos_command:
    commands:
      - show version
```

**Note:** The old FQCNs will continue to work via automatic redirects until version 12.0.0, but it's recommended to update your playbooks to use the new `juniper.device` collection.

## Communication

* Join the Ansible forum:
  * [Get Help](https://forum.ansible.com/c/help/6): get help or help others.
  * [Posts tagged with 'juniper'](https://forum.ansible.com/tag/juniper): subscribe to participate in collection-related conversations.
  * [Ansible Network Automation Working Group](https://forum.ansible.com/g/network-wg/): by joining the team you will automatically get subscribed to the posts tagged with [network](https://forum.ansible.com/tags/network).
  * [Social Spaces](https://forum.ansible.com/c/chat/4): gather and interact with fellow enthusiasts.
  * [News & Announcements](https://forum.ansible.com/c/news/5): track project-wide announcements including social events.

* The Ansible [Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn): used to announce releases and important changes.

For more information about communication, see the [Ansible communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against the following Ansible versions: **>=2.16.0**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

### Supported connections

The Juniper Networks Junos collection supports `network_cli` and `netconf` connections.

## Included content

<!--start collection content-->
### Cliconf plugins
Name | Description
--- | ---
[junipernetworks.junos.junos](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_cliconf.rst)|Use junos cliconf to run command on Juniper Junos OS platform

### Netconf plugins
Name | Description
--- | ---
[junipernetworks.junos.junos](https://github.com/ansible-collections/junipernetworks.junos/blob/main/docs/junipernetworks.junos.junos_netconf.rst)|Use junos netconf plugin to run netconf commands on Juniper JUNOS platform

<!--end collection content-->

Click the `Content` button to see the list of content included in this collection.

## Installing this collection

You can install the Juniper Networks Junos collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install junipernetworks.junos

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: junipernetworks.junos
```

## Using this collection

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `junipernetworks.junos.junos_l2_interfaces`.
The following example task replaces configuration changes in the existing configuration on a Juniper Networks Junos network device, using the FQCN:

```yaml
---
- name: "Replace provided configuration with device configuration"
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
```

### See Also:

- [Juniper Junos Platform options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
- [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

**Note: This collection is deprecated. For new issues, bug reports, and contributions, please use the [juniper.device collection repository](https://github.com/Juniper/ansible-junos-stdlib).**

- **Issues**: Report bugs and request features at [https://github.com/Juniper/ansible-junos-stdlib/issues](https://github.com/Juniper/ansible-junos-stdlib/issues)
- **Pull Requests**: Submit contributions at [https://github.com/Juniper/ansible-junos-stdlib/pulls](https://github.com/Juniper/ansible-junos-stdlib/pulls)

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [juniper.device collection repository](https://github.com/Juniper/ansible-junos-stdlib). See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for complete details.

You can also join us on:

- IRC - the `#ansible-network` [irc.libera.chat](https://libera.chat/) channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

### Code of Conduct

This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Release notes

Release notes are available [here](https://github.com/ansible-collections/junipernetworks.junos/blob/main/CHANGELOG.rst).

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
