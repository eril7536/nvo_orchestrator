from openstack_builder import build_vns, build_vms, build_sec_groups
import dockerfunctions
# from bgpSetup import *

def openstack():
    build_vns()
    build_vms()
    # build_sec_groups()

# def docker():
#     dockerfunctions()
    
if __name__ == "__main__":
    openstack()
