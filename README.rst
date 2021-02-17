..
      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

      Convention for heading levels in Open vSwitch documentation:

      =======  Heading 0 (reserved for the title in a document)
      -------  Heading 1
      ~~~~~~~  Heading 2
      +++++++  Heading 3
      '''''''  Heading 4

      Avoid deeper levels because they do not render well.

=================
Description
=================

This fork of the master branch of OVS supports GTP-U tunneling. It takes care only of the mandatory part of the GTP-U tunneling. This tunneling is similar to the other layer 3 tunneling - lisp. Similar to the case with lisp tunneling,  The GTP tunneling code attaches a header with harcoded source and destination MAC address 06:00:00:00:00:00. This address has all bits set to 0, except the locally administered bit, in order to avoid potential collisions with existing allocations. In order for packets to reach their intended destination, the destination MAC address needs to be rewritten.

GTP is a layer 3 tunneling mechanism, meaning that encapsulated packets do not carry Ethernet headers, and ARP requests shouldn't be sent over the tunnel. Because of this, there are some additional steps required for setting up GTP tunnels in Open vSwitch, until support for L3 tunnels will improve.

There is an installation script *install.sh* included in the repository which can automate the installation of OVS on your machine along with the dependencies. Alternatively you can follow ovs installation guides on openvswitch.org web page.
you can install the dependencies by the following command

``$ apt-get -y install git wget dh-autoreconf libssl-dev libtool libc6-dev``

Before installing OVS ensure that you have python2.7 or any later version installed on your machine (by default python is > 2.7 on Ubuntu 16) and python six module is also installed.If you do not have python six installed, you can install it by the following commands::

	$ wget https://pypi.python.org/packages/b3/b2/238e2590826bfdd113244a40d9d3eb26918bd798fc187e2360a8367068db/six-1.10.0.tar.gz#md5=34eed507548117b2ab523ab14b2f8b55
	$ tar -xvf six-1.10.0.tar.gz
	$ cd six-1.10.0
	$ sudo python setup.py install

alternativ
After the OVS is installed, you can install mininet by the following command. Installing mininet is optional. In my scenario I am using mininet to simulate a virtual topology and demonstrate GTP-U tunneling.

``$ apt-get install mininet``


Setting up the GTP tunneling port on OVS ::
-----------------------------------------

``$ ovs-vsctl add-br br1``

# flow based tunneling port

``$ ovs-vsctl add-port br1 gtp0 -- set interface gtp0 type=gtp options:remote_ip=flow options:key=flow``

or

# port based tunneling port

``$ ovs-vsctl add-port br1 gtp1 -- set interface gtp1 type=gtp options:remote_ip=<IP of the destination> options:key=flow``



