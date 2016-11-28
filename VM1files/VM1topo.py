# -*- coding: utf-8 -*-
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import OVSController, RemoteController,Node
from mininet.cli import CLI

class SimplePktSwitch(Topo):
    """Simple topology example."""

    def __init__(self, **opts):
        """Create custom topo."""
	import os
	os.system ('sudo mn -c')
        # Initialize topology
        # It uses the constructor for the Topo cloass
        super(SimplePktSwitch, self).__init__(**opts)

        # Add hosts and switches
        h1 = self.addHost('h1', ip='10.0.0.1',mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='10.0.0.2',mac='00:00:00:00:00:02')

	
        # Adding switches
        s1 = self.addSwitch('s1')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)

	

def run():
    net = Mininet(topo=SimplePktSwitch(),controller=OVSController)
    net.start()

    import os
   
    os.system ('sudo ovs-vsctl add-port s1 gtp1 -- set interface gtp1 type=gtp option:remote_ip=192.168.56.103 option:key=flow ofport_request=10')
    os.system ('sudo ovs-ofctl add-flows s1 VM1flow.txt') 
    os.system ('sudo ovs-vsctl add-port s1 eth1')
    os.system ('sudo ifconfig eth1 0.0.0.0')
    os.system ('sudo ifconfig s1 192.168.56.101')  	
    
    CLI(net)
    net.stop()

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
run()
