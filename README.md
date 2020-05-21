DO NOT MERGE THIS

# Juniper Networks Junos Collection
[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/project/github.com/ansible-collections/junipernetworks.junos) <!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/vyos)](https://codecov.io/gh/ansible-collections/junipernetworks.junos)-->

The Ansible Juniper Networks Junos collection includes a variety of Ansible content to help automate the management of Juniper Networks Junos network appliances.

This collection has been tested against Juniper Networks Junos OS 18.4R1.

### Supported connections
The Juniper Networks Junos collection supports ``network_cli`` and ``netconf`` connections.

## Included content

Click the ``Content`` button to see the list of content included in this collection.

## Installing this collection

You can install the Juniper Networks Junos collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install junipernetworks.junos

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: junipernetworks.junos
    version: 0.0.3
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

Alternately, you can call modules by their short name if you list the `junipernetworks.junos` collection in the playbook's `collections`, as follows:

```yaml
---
- hosts: junos01
  gather_facts: false
  connection: network_cli

  collections:
    - junipernetworks.junos

  tasks:
    - name: Merge JUNOS vlan
      junos_vlans:
        config:
          - name: vlan-1
            vlan-id: 1
      state: merged
```


### See Also:

* [Juniper Junos Platform options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Juniper Networks Junos collection repository](https://github.com/ansible-collections/junipernetworks.junos).

You can also join us on:

- Freenode IRC - ``#ansible-network`` Freenode channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.


## Changelogs
<!--Add a link to a changelog.md file or an external docsite to cover this information. -->

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
