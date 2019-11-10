#!/usr/bin/python

"""
Example network of Quagga routers
(QuaggaTopo + QuaggaService)
"""

import sys
import atexit

# patch isShellBuiltin
import mininet.util
import mininext.util
mininet.util.isShellBuiltin = mininext.util.isShellBuiltin
sys.modules['mininet.util'] = mininet.util

from mininet.util import dumpNodeConnections
from mininet.node import OVSController
from mininet.log import setLogLevel, info

from mininext.cli import CLI
from mininext.net import MiniNExT

from topo import QuaggaTopo

net = None


def startNetwork():
    "instantiates a topo, then starts the network and prints debug information"

    info('** Creating Quagga network topology\n')
    topo = QuaggaTopo()

    info('** Starting the network\n')
    global net
    net = MiniNExT(topo, controller=OVSController)
    net.start()
    
    h1 = net.get('h1')
    h2 = net.get('h2')
    
    r1 = net.get('r1')
    r1.cmd( 'sysctl net.ipv4.ip_forward=1' )
    
    r2 = net.get('r2')
    r2.cmd( 'sysctl net.ipv4.ip_forward=1' )
    
    r3 = net.get('r3')
    r3.cmd( 'sysctl net.ipv4.ip_forward=1' )

    r4 = net.get('r4')
    r4.cmd( 'sysctl net.ipv4.ip_forward=1' )
    
  
    h1.cmd('route add default gw 172.0.0.2 h1-eth0')
    h2.cmd('route add default gw 172.0.7.2 h2-eth0')
# #     
#     r1.cmd('route add -net 172.0.5.0 netmask 255.255.255.0 gw 172.0.3.1 r1-eth1') #r1-r4
#     r1.cmd('route add -net 172.0.7.0 netmask 255.255.255.0 gw 172.0.3.1 r1-eth1') #r1-h2
#  
#     r2.cmd('route add -net 172.0.0.0 netmask 255.255.255.0 gw 172.0.3.2 r2-eth0') #r2-h1
#     r2.cmd('route add -net 172.0.7.0 netmask 255.255.255.0 gw 172.0.5.1 r2-eth1') #r2-h2
#     r2.cmd('route add -net 172.0.4.0 netmask 255.255.255.0 gw 172.0.3.2 r2-eth0') #r2-r3
# #     r2.cmd('route add -net 172.0.5.0 netmask 255.255.255.0 gw 172.0.5.1 r2-eth1') #r2-r4
# #     
#     r3.cmd('route add -net 172.0.0.0 netmask 255.255.255.0 gw 172.0.4.2 r3-eth0') #r3-h1
#     r3.cmd('route add -net 172.0.7.0 netmask 255.255.255.0 gw 172.0.6.1 r3-eth1') #r3-h2
#     r3.cmd('route add -net 172.0.3.0 netmask 255.255.255.0 gw 172.0.4.2 r3-eth0') #r3-r2
#     r3.cmd('route add -net 172.0.5.0 netmask 255.255.255.0 gw 172.0.6.1 r3-eth1') #r3-r4
# #     
#     r4.cmd('route add -net 172.0.3.0 netmask 255.255.255.0 gw 172.0.5.2 r4-eth0') #r4-r1
#     r4.cmd('route add -net 172.0.0.0 netmask 255.255.255.0 gw 172.0.5.2 r4-eth0') #r4-h1
#     r4.cmd('route add -net 172.0.5.0 netmask 255.255.255.0 gw 172.0.5.2 r4-eth0') #r4-r2
#     r4.cmd('route add -net 172.0.4.0 netmask 255.255.255.0 gw 172.0.6.2 r4-eth1') #r4-r3
    
    info('** Dumping host connections\n')
    dumpNodeConnections(net.hosts)

    info('** Testing network connectivity\n')
    net.ping(net.hosts)

    info('** Dumping host processes\n')
    for host in net.hosts:
        host.cmdPrint("ps aux")

    info('** Running CLI\n')
    CLI(net)


def stopNetwork():
    "stops a network (only called on a forced cleanup)"

    if net is not None:
        info('** Tearing down Quagga network\n')
        net.stop()

if __name__ == '__main__':
    # Force cleanup on exit by registering a cleanup function
    atexit.register(stopNetwork)

    # Tell mininet to print useful information
    setLogLevel('info')
    #setLogLevel('debug')
    startNetwork()
