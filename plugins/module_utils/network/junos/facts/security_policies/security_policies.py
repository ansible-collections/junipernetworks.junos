#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos security_policies fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
import re
from copy import deepcopy
from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.security_policies.security_policies import (
    Security_policiesArgs,
)

from ansible.module_utils.six import string_types

try:
    from lxml import etree

    HAS_LXML = True
except ImportError:
    HAS_LXML = False

try:
    import xmltodict

    HAS_XMLTODICT = True
except ImportError:
    HAS_XMLTODICT = False


class Security_policiesFacts(object):
    """The junos security_policies fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Security_policiesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(etree.tostring(xml_root), dict_constructor=dict)
        return xml_dict

    def _get_device_data(self, connection, config_filters):
        """
        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filters)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for security_polices
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")

        if not data:
            config_filter = """
                    <configuration>
                        <security>
                            <policies>
                            </policies>
                        </security>
                    </configuration>               
                    """
            data = self._get_device_data(connection, config_filter)

        # split the config into instances of the resource
        if isinstance(data, string_types):
            data = etree.fromstring(to_bytes(data, errors="surrogate_then_replace"))
        objs = {}
        resources = data.xpath("configuration/security/policies")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {}
        if objs:
            facts["security_policies"] = {}
            params = utils.validate_config(self.argument_spec, {"config": objs})

            facts["security_policies"] = utils.remove_empties(params["config"])

        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        security_policies_config = {}

        # Parse facts for security policies
        conf = conf.get("policies")

        if "policy" in conf:
            security_policies_config["from_zones"] = []
            from_zone_dict = {}
            zone_pairs = conf.get("policy")
            if isinstance(zone_pairs, dict):
                zone_pairs = [zone_pairs]
            for zone_pair_policies in zone_pairs:

                if zone_pair_policies["from-zone-name"] not in from_zone_dict:
                    from_zone_dict[zone_pair_policies["from-zone-name"]] = {}
                    from_zone_dict[zone_pair_policies["from-zone-name"]]["name"] = zone_pair_policies["from-zone-name"]
                    from_zone_dict[zone_pair_policies["from-zone-name"]]["to_zones"] = {}

                from_zone = from_zone_dict[zone_pair_policies["from-zone-name"]]

                from_zone["to_zones"][zone_pair_policies["to-zone-name"]] = {}
                to_zone = from_zone["to_zones"][zone_pair_policies["to-zone-name"]]

                to_zone["name"] = zone_pair_policies["to-zone-name"]
                to_zone["policies"] = self.parse_policies(zone_pair_policies["policy"])

            for from_zone in from_zone_dict.values():
                from_zone["to_zones"] = list(from_zone["to_zones"].values())
                security_policies_config["from_zones"].append(from_zone)

        if "global" in conf:
            global_policies = conf.get("global")
            global_policies = global_policies.get("policy")
            security_policies_config["global"] = {}
            security_policies_config["global"]["policies"] = self.parse_policies(global_policies)

        return security_policies_config

    def parse_policies(self, policies):
        policy_list = []

        if isinstance(policies, dict):
            policies = [policies]

        for policy in policies:
            tmp_policy = {}
            tmp_policy["name"] = policy["name"]
            tmp_policy["match"] = {}

            tmp_policy["match"]["source_address"] = {}

            if isinstance(policy["match"]["source-address"], str):
                policy["match"]["source-address"] = [policy["match"]["source-address"]]

            for source_address in policy["match"]["source-address"]:
                if source_address == "any-ipv6":
                    tmp_policy["match"]["source_address"]["any_ipv6"] = True
                elif source_address == "any-ipv4":
                    tmp_policy["match"]["source_address"]["any_ipv4"] = True
                elif source_address == "any":
                    tmp_policy["match"]["source_address"]["any"] = True
                else:
                    if "addresses" not in tmp_policy["match"]["source_address"]:
                        tmp_policy["match"]["source_address"]["addresses"] = []
                    tmp_policy["match"]["source_address"]["addresses"].append(source_address)

            tmp_policy["match"]["destination_address"] = {}

            if isinstance(policy["match"]["destination-address"], str):
                policy["match"]["destination-address"] = [policy["match"]["destination-address"]]

            for destination_address in policy["match"]["destination-address"]:
                if destination_address == "any-ipv6":
                    tmp_policy["match"]["destination_address"]["any_ipv6"] = True
                elif destination_address == "any-ipv4":
                    tmp_policy["match"]["destination_address"]["any_ipv4"] = True
                elif destination_address == "any":
                    tmp_policy["match"]["destination_address"]["any"] = True
                else:
                    if "addresses" not in tmp_policy["match"]["destination_address"]:
                        tmp_policy["match"]["destination_address"]["addresses"] = []
                    tmp_policy["match"]["destination_address"]["addresses"].append(destination_address)

            tmp_policy["match"]["application"] = {}

            if isinstance(policy["match"]["application"], str):
                policy["match"]["application"] = [policy["match"]["application"]]

            for application in policy["match"]["application"]:
                if application == "any":
                    tmp_policy["match"]["application"]["any"] = True
                else:
                    if "application_names" not in tmp_policy["match"]["application"]:
                        tmp_policy["match"]["application"]["application_names"] = []
                    tmp_policy["match"]["application"]["application_names"].append(application)

            tmp_policy["then"] = {}
            if "deny" in tmp_policy["then"]:
                tmp_policy["then"]["deny"] = True
            if "count" in tmp_policy["then"]:
                tmp_policy["then"]["count"] = True

            if "description" in policy:
                tmp_policy["description"] = policy["description"]
            if "scheduler-name" in policy:
                tmp_policy["scheduler_name"] = policy["scheduler-name"]

            test = utils.remove_empties(tmp_policy)
            policy_list.append(test)

        return policy_list
