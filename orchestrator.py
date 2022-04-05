from openstack_builder import build_vns, build_vms, build_sec_groups

def openstack():
    build_vns()
    build_vms()
    build_sec_groups()

if __name__ == "__main__":
    openstack()
