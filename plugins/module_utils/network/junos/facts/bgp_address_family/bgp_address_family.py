#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos bgp_address_family fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from copy import deepcopy
from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.bgp_address_family.bgp_address_family import Bgp_address_familyArgs
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


class Bgp_address_familyFacts(object):
    """ The junos bgp_address_family fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Bgp_address_familyArgs.argument_spec
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

        if not data:
            config_filter = """
                        <configuration>
                            <protocols>
                                <bgp>
                                   <family>
                                   </family>
                                </bgp>
                            </protocols>
                        </configuration>
                        """
            data = self.get_connection(connection, config_filter)

        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace")
            )
        objs = {}
        resources = data.xpath("configuration/protocols/bgp/family")
        autonomous_system = data.xpath(
            "configuration/routing-options/autonomous-system"
        )
        if autonomous_system:
            self.autonomous_system = self._get_xml_dict(
                autonomous_system.pop()
            )
        else:
            self.autonomous_system = ""
        for resource in resources:
            if resource:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)
        facts = {}
        if objs:
            facts["bgp_address_family"] = {}
            params = utils.validate_config(
                self.argument_spec, {"config": objs}
            )
            facts["bgp_address_family"] = utils.remove_empties(params["config"])
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
        nlri_type = [
            'any',
            'flow',
            'multicast',
            'labeled-unicast'
        ]
        bgp_address_family = {}
        bgp = conf.get("family")
        address_family = []

        # Parse 'inet' and populate facts
        if 'inet' in bgp.keys():
            # Declare af dict element of address_family
            af = {}
            af['afi'] = 'inet'

            # Declare af_type dict
            af_type = []
            inet = bgp.get('inet')

            for nlri in nlri_type:
                nlri_dict = self.parse_nlri(inet, nlri)
                if nlri_dict:
                    af_type.append(nlri_dict)

            # Populate af dict entry
            if af_type:
                af['af_type'] = af_type

        # Populate address family entry
        if af:
            address_family.append(af)

        # Populate address family list into address_family dict
        if address_family:
            bgp_address_family['address_family'] = address_family

        return utils.remove_empties(bgp_address_family)

    def parse_nlri(self, cfg, nlri_t):
        """

        :param cfg:
        :return:
        """
        nlri_dict = {}
        if nlri_t in cfg.keys():
            nlri_dict['type'] = nlri_t
            nlri = cfg.get(nlri_t)

            if not nlri:
                nlri_dict['set'] = True
                return nlri_dict
            # Parse accepted-prefix-limit
            if 'accepted-prefix-limit' in nlri.keys():
                apl_dict = self.parse_accepted_prefix_limit(nlri)
                # populate accepted_prefix_limit
                if apl_dict:
                    nlri_dict['accepted_prefix_limit'] = apl_dict

            # Parse add-path
            if 'add-path' in nlri.keys():
                ap_dict = self.parse_add_path(nlri)
                # populate accepted_prefix_limit
                if ap_dict:
                    nlri_dict['add_path'] = ap_dict

            # Parse aigp
            if 'aigp' in nlri.keys():
                aigp_dict = self.parse_aigp(nlri)
                # populate aigp
                if aigp_dict:
                    nlri_dict['aigp'] = aigp_dict

            # Parse and populate damping
            if 'damping' in nlri.keys():
                nlri_dict['damping'] = True

            # Parse defer-initial-multipath-build
            if 'defer-initial-multipath-build' in nlri.keys():
                dimb_dict = self.parse_defer_initial_multipath_build(nlri)
                # populate defer_initial_multipath_build
                if dimb_dict:
                    nlri_dict['defer_initial_multipath_build'] = dimb_dict

            # Parse delay-route-advertisements
            if 'delay-route-advertisements' in nlri.keys():
                dra_dict = self.parse_delay_route_advertisements(nlri)
                # populate delay_route_advertisements
                if dra_dict:
                    nlri_dict['delay_route_advertisements'] = dra_dict

            # Parse forwarding-state-bit
            if 'forwarding-state-bit' in nlri.keys():
                fsb = nlri.get('forwarding-state-bit')
                if 'from-fib' in fsb.keys():
                    nlri_dict['graceful_restart_forwarding_state_bit'] = 'from-fib'
                else:
                    nlri_dict['graceful_restart_forwarding_state_bit'] = 'set'

            # Parse legacy-redirect-ip-action
            # TODO add support in docs and argspec
            # if 'legacy-redirect-ip-action' in nlri.keys():
            #     lria_dict = self.parse_legacy_redirect_ip_action(nlri)
            #     # populate legacy_redirect_ip_action
            #     if lria_dict:
            #         nlri_dict['legacy_redirect_ip_action'] = lria_dict

            # Parse local-ipv4-address
            if 'local-ipv4-address' in nlri.keys():
                nlri_dict['local_ipv4_address'] = nlri.get('local-ipv4-address')

            # Parse loops
            if 'loops' in nlri.keys():
                loops = nlri.get('loops')
                nlri_dict['loops'] = loops.get('loops')

            # Parse no-install
            if 'no-install' in nlri.keys():
                nlri_dict['no_install'] = True

            # Parse no-validate
            if 'no-validate' in nlri.keys():
                nlri_dict['no_validate'] = nlri.get('no-validate')

            # Parse output-queue-priority
            if 'output-queue-priority' in nlri.keys():
                oqp = nlri.get('output-queue-priority')
                if 'expedited' in oqp.keys():
                    nlri_dict['output_queue_priority_expedited'] = True
                if 'priority' in oqp.keys():
                    nlri_dict['output_queue_priority_priority'] = oqp.get('priority')

            # Parse prefix-limit
            if 'prefix-limit' in nlri.keys():
                pl_dict = self.parse_accepted_prefix_limit(nlri)
                # populate delay_route_advertisements
                if pl_dict:
                    nlri_dict['prefix_limit'] = pl_dict

            # Parse rib-group
            if 'rib-group' in nlri.keys():
                nlri_dict['rib_group'] = nlri.get('rib-group')

            # Parse route-refresh-priority
            if 'route-refresh-priority' in nlri.keys():
                oqp = nlri.get('route-refresh-priority')
                if 'expedited' in oqp.keys():
                    nlri_dict['route_refresh_priority_expedited'] = True
                if 'priority' in oqp.keys():
                    nlri_dict['route_refresh_priority_priority'] = oqp.get('priority')

            # Parse secondary-independent-resolution
            if 'secondary-independent-resolution' in nlri.keys():
                nlri_dict['secondary_independent_resolution'] = True

            # Parse strip-nexthop
            if 'strip-nexthop' in nlri.keys():
                nlri_dict['strip_nexthop'] = True

            # Parse withdraw-priority
            if 'withdraw-priority' in nlri.keys():
                oqp = nlri.get('withdraw-priority')
                if 'expedited' in oqp.keys():
                    nlri_dict['withdraw_priority_expedited'] = True
                if 'priority' in oqp.keys():
                    nlri_dict['withdraw_priority_priority'] = oqp.get('priority')
            return nlri_dict

    def parse_accepted_prefix_limit(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        apl_dict = {}
        if 'accepted-prefix-limit' in cfg.keys():
            apl = cfg.get('accepted-prefix-limit')
        else:
            apl = cfg.get('prefix-limit')
        if 'maximum' in apl.keys():
            apl_dict['maximum'] = apl.get('maximum')
        if 'teardown' in apl.keys():
            if not apl.get('teardown'):
                apl_dict['teardown'] = True
            else:
                td = apl.get('teardown')
                if 'idle-timeout' in td.keys():
                    if not td.get('idle-timeout'):
                        apl_dict['idle_timeout'] = True
                    elif 'forever' in td['idle-timeout'].keys():
                        apl_dict['forever'] = True
                    elif 'timeout' in td['idle-timeout'].keys():
                        apl_dict['idle_timeout_value'] = td['idle-timeout'].get('timeout')
                if 'limit-threshold' in td.keys():
                    apl_dict['limit_threshold'] = td.get('limit-threshold')
        return apl_dict

    def parse_add_path(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        ap_dict = {}
        ap = cfg.get('add-path')
        if 'receive' in ap.keys():
            ap_dict['receive'] = True
        if 'send' in ap.keys():
            send = ap.get('send')
            s_dict = {}
            if 'include-backup-path' in send.keys():
                s_dict['include_backup_path'] = send.get('include-backup-path')
            if 'path-count' in send.keys():
                s_dict['path_count'] = send.get('path-count')
            if 'multipath' in send.keys():
                s_dict['multipath'] = True
            if 'path-selection-mode' in send.keys():
                psm = send.get('path-selection-mode')
                psm_dict = {}
                if 'all-paths' in psm.keys():
                    psm_dict['all_paths'] = True
                if 'equal-cost-paths' in psm.keys():
                    psm_dict['equal_cost_paths'] = True
                s_dict['path_selection_mode'] = psm_dict
            if 'prefix-policy' in send.keys():
                s_dict['prefix_policy'] = send.get('prefix-policy')
            ap_dict['send'] = s_dict
        return ap_dict

    def parse_aigp(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        aigp_dict = {}
        aigp = cfg.get('aigp')
        if aigp and 'disable' in aigp.keys():
            aigp_dict['disable'] = True
        else:
            aigp_dict['set'] = True
        return aigp_dict

    def parse_defer_initial_multipath_build(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        dimb_dict = {}
        dimb = cfg.get('defer-initial-multipath-build')
        if 'maximum-delay' in dimb.keys():
            dimb_dict['maximum_delay'] = dimb.get('maximum-delay')
        else:
            dimb_dict['set'] = True
        return dimb_dict

    def parse_legacy_redirect_ip_action(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        lria_dict = {}
        lria = cfg.get('legacy-redirect-ip-action')
        if not lria:
            lria_dict['set'] = True
        else:
            if 'send' in lria.keys():
                lria_dict['send'] = True
            if 'receive' in lria.keys():
                lria_dict['send'] = True
        return lria_dict

    def parse_delay_route_advertisements(self, cfg):
        """

        :param self:
        :param cfg:
        :return:
        """
        dra_dict = {}
        dra = cfg.get('delay-route-advertisements')
        if not dra:
            dra_dict['set'] = True
        else:
            if 'maximum-delay' in dra.keys():
                mxd = dra.get('maximum-delay')
                if 'route-age' in mxd.keys():
                    dra_dict['max_delay_route_age'] = mxd.get('route-age')
                if 'routing-uptime' in mxd.keys():
                    dra_dict['max_delay_routing_uptime'] = mxd.get('routing-uptime')
            if 'minimum-delay' in dra.keys():
                mid = dra.get('minimum-delay')
                if 'inbound-convergence' in mid.keys():
                    dra_dict['min_delay_inbound_convergence'] = mid.get('inbound-convergence')
                if 'routing-uptime' in mid.keys():
                    dra_dict['min_delay_routing_uptime'] = mid.get('routing-uptime')
        return dra_dict
