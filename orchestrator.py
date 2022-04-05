from openstack_builder import build_vns, build_vms, build_sec_groups, build_router
from dockerfunctions import docker_file_generate, spin_up_dockers

def openstack():
    build_vns()
    # build_vms()
    # build_sec_groups()
    build_router()
# def docker():
#     if docker_file_generate == True:
#         print("spin up dockers")
#         spin_up_dockers()

if __name__ == "__main__":
    openstack()
    # docker()
