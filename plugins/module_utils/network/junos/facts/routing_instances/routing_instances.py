#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos routing_instances fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import q
from copy import deepcopy
from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.routing_instances.routing_instances import Routing_instancesArgs
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



class Routing_instancesFacts(object):
    """ The junos routing_instances fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Routing_instancesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_connection(self, connection, config_filter):
        """
        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filter)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for bgp_address_family
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")
        if not HAS_XMLTODICT:
            self._module.fail_json(msg="xmltodict is not installed.")

        if not data:
            config_filter = """
                        <configuration>
                           <routing-instances/>
                        </configuration>
                        """
            data = self.get_connection(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace")
            )
        objs = {}
        resources = data.xpath("configuration/routing-instances")
        autonomous_system_path = data.xpath(
            "configuration/routing-options/autonomous-system"
        )
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)


        facts = {}
        if objs:
            facts["routing_instances"] = []
            params = utils.validate_config(
                self.argument_spec, {"config": objs}
            )

            for cfg in params["config"]:
                facts["routing_instances"].append(
                    utils.remove_empties(cfg)
                )
        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(
            etree.tostring(xml_root), dict_constructor=dict
        )
        return xml_dict

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        routing_instances_config = []

        # Parse facts for routing instances node
        conf = conf.get("routing-instances")

        # Parse routing instances
        routing_instances = conf.get("instance")
        if isinstance(routing_instances, list):
            for instance in routing_instances:
                instance_dict = self.parse_instance(instance)
                routing_instances_config.append(instance_dict)
        else:
            instance_dict = self.parse_instance(routing_instances)
            routing_instances_config.append(instance_dict)

        return routing_instances_config

    def parse_instance(self, instance):
        """

        :param instance:
        :return:
        """
        instance_dict = {}
        # read instance name
        instance_dict["name"] = instance["name"]

        # read connection-id-advertise TODO

        # read egress-protection TODO

        # read description
        if instance.get("description"):
            instance_dict["description"] = instance["description"]

        # read instance role
        if instance.get("instance-role"):
            instance_dict["instance_role"] = instance["instance-role"]

        # read instance type
        if instance.get("instance-type"):
            instance_dict["type"] = instance["instance-type"]

        # read interfaces TODO

        # read l2vpn-id
        if instance.get("l2vpn-id"):
            instance_dict["l2vpn_id"] = instance["l2vpn-id"].get("community")

        # read no-irb-layer2-copy TODO
        if instance.get("no-irb-layer2-copy"):
            instance_dict["no_irb_layer_2_copy"] = True

        # read no_local_switching TODO
        if instance.get("no-local-switching"):
            instance_dict["no_local_switching"] = True

        # read no-vrf-advertise TODO
        if instance.get("no-vrf-advertise"):
            instance_dict["no_vrf_advertise"] = True

        # read no_vrf_propagate_ttl TODO
        if instance.get("no-vrf-propagate-ttl"):
            instance_dict["no_vrf_propagate_ttl"] = True

        # read  protocols list TODO

        # read qualified_bum_pruning_mode
        if instance.get("qualified-bum-pruning-mode"):
            instance_dict["qualified_bum_pruning_mode"] = True

        # read routing interface

        # Add entry to routing_instances list
        return utils.remove_empties(instance_dict)


