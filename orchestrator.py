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

def bgp(local_as_ryu, router_id_ryu, neighbor_id_ryu, remote_as_ryu, local_as_q, router_id_q, neighbor_id_q, remote_as_q):
    ryuConf(local_as_ryu, router_id_ryu, neighbor_id_ryu, remote_as_ryu)
    quaggaConf(local_as_q, router_id_q, neighbor_id_q, remote_as_q)

def docker():
    
if __name__ == "__main__":
    # openstack()
    docker()
    # bgp(local_as_ryu, router_id_ryu, neighbor_id_ryu, remote_as_ryu, local_as_q, router_id_q, neighbor_id_q, remote_as_q)