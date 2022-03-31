from unicodedata import name
from dockerfunctions import docker_file_generate, spin_up_containers
from openstackfunctions import *
from dockerfunctions import *
from bgpSetup import *

def openstack():
    #This function call the openstack subfunctions to deploy vm, network and security groups
    deployOsVm()
    deployOsNw()
    deployOsSec()

def bgp():
    ryuConf()
    quaggaConf()

def docker():
    docker_file_generate()
    spin_up_containers()
if __name__ == "__main__":
    openstack()
    docker()
    bgp()