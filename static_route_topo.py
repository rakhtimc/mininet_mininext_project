import inspect
import os
from mininext.topo import Topo
from mininext.services.quagga import QuaggaService
from mininet.node import Node

from collections import namedtuple

QuaggaHost = namedtuple("QuaggaHost", "name ip loIP")
net = None

class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class QuaggaTopo(Topo):
    "Creates a topology of Quagga routers"

    def __init__(self):
        """Initialize a Quagga topology with 5 routers, configure their IP
           addresses, loop back interfaces, and paths to their private
           configuration directories."""
        Topo.__init__(self)

        # Directory where this file / script is located"
        selfPath = os.path.dirname(os.path.abspath(
            inspect.getfile(inspect.currentframe())))  # script directory

        # Initialize a service helper for Quagga with default options
        quaggaSvc = QuaggaService(autoStop=False)

        # Path configurations for mounts
        quaggaBaseConfigPath = selfPath + '/configs/'

        # List of Quagga host configs
        # quaggaHosts = []
        # quaggaHosts.append(QuaggaHost(name='h1', ip='172.0.0.1/24'))
        # quaggaHosts.append(QuaggaHost(name='r1', ip='172.0.2.1/24'))
        # quaggaHosts.append(QuaggaHost(name='r2', ip='172.0.3.2/24'))
        # quaggaHosts.append(QuaggaHost(name='r3', ip='172.0.3.1/24'))
        # quaggaHosts.append(QuaggaHost(name='r4', ip='172.0.4.1/24'))
        # quaggaHosts.append(QuaggaHost(name='h2', ip='172.0.5.1/24'))

        # Create an instance of a host, called a quaggaContainer
        h1 = self.addHost(name='h1',
                          ip='172.0.0.1/24',
                          hostname = 'h1',
                          privateLogDir = True,
                          privateRunDir = True,
                          inMountNamespace = True,
                          inPIDNamespace = True,
                          inUTSNamespace = True)
                                            



        # Configure and setup the Quagga service for this node
        quaggaSvcConfig = \
            {'quaggaConfigPath': quaggaBaseConfigPath + h1}
        self.addNodeService(node='h1', service=quaggaSvc,
                            nodeConfig=quaggaSvcConfig)

    # Create an instance of a host, called a quaggaContainer
        
                          
        #r1 = self.addNode( 'r1', cls=LinuxRouter, ip='172.0.0.2/24' )
        
        r1 = self.addHost(name='r1',
                          ip='172.0.0.2/24',
                          hostname = 'r1',
                          privateLogDir = True,
                          privateRunDir = True,
                          inMountNamespace = True,
                          inPIDNamespace = True,
                          inUTSNamespace = True)

        # Configure and setup the Quagga service for this node
        quaggaSvcConfig = \
            {'quaggaConfigPath': quaggaBaseConfigPath + r1}
        self.addNodeService(node='r1', service=quaggaSvc,
                            nodeConfig=quaggaSvcConfig)
                            
        # Create an instance of a host, called a quaggaContainer
        r2 = self.addHost(name='r2',
                          ip='172.0.3.1/24',
                          hostname = 'r2',
                          privateLogDir = True,
                          privateRunDir = True,
                          inMountNamespace = True,
                          inPIDNamespace = True,
                          inUTSNamespace = True)



        # Configure and setup the Quagga service for this node
        quaggaSvcConfig = \
            {'quaggaConfigPath': quaggaBaseConfigPath + r2}
        self.addNodeService(node='r2', service=quaggaSvc,
                            nodeConfig=quaggaSvcConfig)

        # Create an instance of a host, called a quaggaContainer
        r3 = self.addHost(name='r3',
                          ip='172.0.4.1/24',
                          hostname = 'r3',
                          privateLogDir = True,
                          privateRunDir = True,
                          inMountNamespace = True,
                          inPIDNamespace = True,
                          inUTSNamespace = True)



        # Configure and setup the Quagga service for this node
        quaggaSvcConfig = \
            {'quaggaConfigPath': quaggaBaseConfigPath + r3}
        self.addNodeService(node='r3', service=quaggaSvc,
                            nodeConfig=quaggaSvcConfig)

        # Create an instance of a host, called a quaggaContainer
        r4 = self.addHost(name='r4',
                          ip='172.0.5.1/24',
                          hostname = 'r4',
                          privateLogDir = True,
                          privateRunDir = True,
                          inMountNamespace = True,
                          inPIDNamespace = True,
                          inUTSNamespace = True)
                          



        # Configure and setup the Quagga service for this node
        quaggaSvcConfig = \
            {'quaggaConfigPath': quaggaBaseConfigPath + r4}
        self.addNodeService(node='r4', service=quaggaSvc,
                            nodeConfig=quaggaSvcConfig)

        # Create an instance of a host, called a quaggaContainer
        h2 = self.addHost(name='h2',
                          ip='172.0.7.1/24',
                          hostname = 'h2',
                          privateLogDir = True,
                          privateRunDir = True,
                          inMountNamespace = True,
                          inPIDNamespace = True,
                          inUTSNamespace = True)



        # Configure and setup the Quagga service for this node
        quaggaSvcConfig = \
            {'quaggaConfigPath': quaggaBaseConfigPath + h2}
        self.addNodeService(node='h2', service=quaggaSvc,
                            nodeConfig=quaggaSvcConfig)

        # Attach the quaggaContainer to the IXP Fabric Switch
        self.addLink(h1, r1, params1={'ip':'172.0.0.1/24'},params2={'ip':'172.0.0.2/24'},intfName1='h1-eth0',intfName2='r1-eth0')
        self.addLink(r1, r2, params1={'ip':'172.0.3.2/24'},params2={'ip':'172.0.3.1/24'},intfName1='r1-eth1',intfName2='r2-eth0')
        self.addLink(r1, r3, params1={'ip':'172.0.4.2/24'},params2={'ip':'172.0.4.1/24'},intfName1='r1-eth2',intfName2='r3-eth0')
        self.addLink(r2, r4, params1={'ip':'172.0.5.2/24'},params2={'ip':'172.0.5.1/24'},intfName1='r2-eth1',intfName2='r4-eth0')
        self.addLink(r3, r4, params1={'ip':'172.0.6.2/24'},params2={'ip':'172.0.6.1/24'},intfName1='r3-eth1',intfName2='r4-eth1')
        self.addLink(h2, r4, params1={'ip':'172.0.7.1/24'},params2={'ip':'172.0.7.2/24'},intfName1='h2-eth0',intfName2='r4-eth2')
        