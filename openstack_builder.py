from openstackfunctions import *

def build_vns():
    create_network("NetA","subnet1","11.0.0.0/24",'11.0.0.254')
    print("Made net A")
    create_network("NetB","subnet1","12.0.0.0/24",'12.0.0.254')
    print("Made net B")


def build_vms():
    create_server("VM1","NETA")
    create_server("VM2_A","NETA")
    create_server("VM2_B","NETB")
    print("vms")


def build_sec_groups():
    print("security")