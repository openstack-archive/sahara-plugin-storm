# Copyright (c) 2015 Telles Nobrega.
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

from sahara.plugins import edp
from sahara.plugins import exceptions as ex
from sahara_plugin_storm.i18n import _


class EdpStormEngine(edp.PluginsStormJobEngine):

    edp_base_version = "1.0.1"

    @staticmethod
    def edp_supported(version):
        return version >= EdpStormEngine.edp_base_version

    def validate_job_execution(self, cluster, job, data):
        if not self.edp_supported(cluster.hadoop_version):
            raise ex.PluginInvalidDataException(
                _('Storm {base} required to run {type} jobs').format(
                    base=EdpStormEngine.edp_base_version, type=job.type))

        super(EdpStormEngine, self).validate_job_execution(cluster, job, data)


class EdpPyleusEngine(edp.PluginsStormPyleusJobEngine):

    edp_base_version = "1.0.1"

    @staticmethod
    def edp_supported(version):
        return version >= EdpPyleusEngine.edp_base_version

    def validate_job_execution(self, cluster, job, data):
        if not self.edp_supported(cluster.hadoop_version):
            raise ex.PluginInvalidDataException(
                _('Storm {base} required to run {type} jobs').format(
                    base=EdpPyleusEngine.edp_base_version, type=job.type))

        super(EdpPyleusEngine, self).validate_job_execution(cluster, job, data)
