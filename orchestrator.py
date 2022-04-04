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


def docker():
    dockerfunctions()
    
if __name__ == "__main__":
    # openstack()
    docker()