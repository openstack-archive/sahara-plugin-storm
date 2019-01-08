Storm Plugin
============

The Storm plugin for sahara provides a way to provision Apache Storm clusters
on OpenStack in a single click and in an easily repeatable fashion.

Currently Storm is installed in standalone mode, with no YARN support.

Images
------

For cluster provisioning, prepared images should be used.

.. list-table:: Support matrix for the `storm` plugin
   :widths: 15 15 20 15 35
   :header-rows: 1

   * - Version
       (image tag)
     - Distribution
     - Build method
     - Version
       (build parameter)
     - Notes

   * - 1.2
     - Ubuntu 16.04
     - sahara-image-create
     - 1.2.1, 1.2.0
     - both versions are supported by the same image tag

   * - 1.1.0
     - Ubuntu 16.04
     - sahara-image-create
     - 1.1.1, 1.1.0
     - both versions are supported by the same image tag

For more information about building image, refer to
:sahara-doc:`Sahara documentation <user/building-guest-images.html>`.

The Storm plugin requires an image to be tagged in the sahara image registry
with two tags: 'storm' and '<Storm version>' (e.g. '1.1.0').

The image requires a username. For more information, refer to the
:sahara-doc:`registering image <user/registering-image.html>` section
of the Sahara documentation.

Note that the Storm cluster is deployed using the scripts available in the
Storm distribution, which allow the user to start all services (nimbus,
supervisors and zookeepers), stop all services and so on. As such Storm is not
deployed as a standard Ubuntu service and if the virtual machines are rebooted,
Storm will not be restarted.

Storm configuration
-------------------

Storm needs few parameters to work and has sensible defaults. If needed they
can be changed when creating the sahara cluster template. No node group
options are available.

Once the cluster is ready, connect with ssh to the master using the `ubuntu`
user and the appropriate ssh key. Storm is installed in `/usr/local/storm` and
should be completely configured and ready to start executing jobs. At the
bottom of the cluster information page from the OpenStack dashboard, a link to
the Storm web interface is provided.

Cluster Validation
------------------

When a user creates a Storm cluster using the Storm plugin, the cluster
topology requested by user is verified for consistency.

Currently there are the following limitations in cluster topology for the
Storm plugin:

+ Cluster must contain exactly one Storm nimbus
+ Cluster must contain at least one Storm supervisor
+ Cluster must contain at least one Zookeeper node

The tested configuration has nimbus, supervisor, and Zookeeper processes each
running on their own nodes.
Another possible configuration is one node with nimbus alone, and additional
nodes each with supervisor and Zookeeper processes together.
