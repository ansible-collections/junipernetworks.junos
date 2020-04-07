#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos ospf fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from copy import deepcopy

from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.ospf.ospf import (
    OspfArgs,
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


class OspfFacts(object):
    """ The junos ospf fact class
    """

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = OspfArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)
        self.router_id = ""

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for ospf
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
                  <protocols>
                    <ospf/>
                  </protocols>
                  <routing-options>
                    <router-id/>
                  </routing-options>
                </configuration>
                """
            data = connection.get_configuration(filter=config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace")
            )

        resources = data.xpath("configuration/protocols/ospf")
        self.router_id = self._get_xml_dict(
            data.xpath("configuration/routing-options/router-id").pop()
        )

        objs = []
        for resource in resources:
            if resource:
                xml = self._get_xml_dict(resource)
                obj = self.render_config(self.generated_spec, xml)
                if obj:
                    objs.append(obj)

        facts = {}
        if objs:
            facts["ospf"] = []
#            params = utils.validate_config(
#                self.argument_spec, {"config": objs}
#            )

            params = {"config": objs}
            for cfg in params["config"]:
                facts["ospf"].append(utils.remove_empties(cfg))

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
        config = deepcopy(spec)
        config["processes"] = []
        processes = {}
        ospf = conf.get("ospf")

        if ospf.get("area"):
            rendered_areas = []
            areas = ospf.get("area")

            if not isinstance(areas, list):
                areas = [areas]

            for area in areas:
                rendered_area = {}
                rendered_area["area_id"] = area.get("name")
                rendered_area["interfaces"] = []

                interfaces = area["interface"]
                if not isinstance(interfaces, list):
                    interfaces = [interfaces]

                for interface in interfaces:
                    interface_dict = {}
                    interface_dict["name"] = interface.get("name")
                    interface_dict["priority"] = interface.get("priority")
                    rendered_area["interfaces"].append(interface_dict)

                if area.get("stub"):
                    rendered_area["stub"] = {"set": True}
                    if "no-summaries" in area.get("stub").keys():
                        rendered_area["stub"]["no_summary"] = True
                    if "default-metric" in area.get("stub").keys():
                        rendered_area["stub"]["default_metric"] = area[
                            "stub"
                        ].get("default-metric")
                if area.get("nssa"):
                    rendered_area["nssa"] = {"set": True}
                    if "no-summaries" in area.get("nssa").keys():
                        rendered_area["nssa"]["no_summary"] = True
                    if "default-lsa" in area.get("nssa").keys():
                        rendered_area["nssa"]["default-lsa"] = True
                rendered_areas.append(rendered_area)

            processes["areas"] = rendered_areas
            processes["process_id"] = self.router_id["router-id"]
            config["processes"].append(processes)

        return utils.remove_empties(config)
