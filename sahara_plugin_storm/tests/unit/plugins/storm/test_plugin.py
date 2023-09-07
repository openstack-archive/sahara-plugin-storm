# Copyright (c) 2015 TellesNobrega
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import mock

from sahara.plugins import base as pb
from sahara_plugin_storm.plugins.storm import plugin as pl
from sahara_plugin_storm.tests.unit import base


class StormPluginTest(base.SaharaWithDbTestCase):
    def setUp(self):
        super(StormPluginTest, self).setUp()
        self.override_config("plugins", ["storm"])
        self.master_host = "master"
        self.master_inst = "6789"
        self.storm_topology_name = 'topology1'
        pb.setup_plugins()

    def _make_master_instance(self, return_code=0):
        master = mock.Mock()
        master.execute_command.return_value = (return_code,
                                               self.storm_topology_name)
        master.hostname.return_value = self.master_host
        master.id = self.master_inst
        return master

    def _get_cluster(self, name, version):
        cluster_dict = {
            'name': name,
            'plugin_name': 'storm',
            'hadoop_version': version,
            'node_groups': []}
        return cluster_dict

    def test_get_open_port(self):
        plugin_storm = pl.StormProvider()
        cluster = mock.Mock()
        ng = mock.Mock()
        ng.node_processes = ['nimbus']
        cluster.node_groups = [ng]
        ng.cluster = cluster
        ports = plugin_storm.get_open_ports(ng)
        self.assertEqual([8080], ports)
