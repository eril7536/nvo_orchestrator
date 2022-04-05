import openstack
# https://docs.openstack.org/openstacksdk/latest/user/index.html
IMAGE_NAME = "cirros-0.5.2-x86_64-disk"
FLAVOR_NAME = "cirros256"
# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize connection
conn = openstack.connect(cloud='admin')

def list_networks(conn):
    print("List Networks:")

    for network in conn.network.networks():
        print(network)

def list_subnets(conn):
    print("List Subnets:")

    for subnet in conn.network.subnets():
        print(subnet)

def list_ports(conn):
    print("List Ports:")

    for port in conn.network.ports():
        print(port)

def list_security_groups(conn):
    print("List Security Groups:")

    for port in conn.network.security_groups():
        print(port)

def list_routers(conn):
    print("List Routers:")

    for router in conn.network.routers():
        print(router)

def list_images(conn):
    print("List Images:")

    for image in conn.compute.images():
        print(image)

def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        print(server)

def create_network(network_name, subnet_name, cidr_net, gateway):
    print("Create Network:")

    example_network = conn.network.create_network(
        name=network_name)

    print(example_network)

    example_subnet = conn.network.create_subnet(
        name=subnet_name,
        network_id=example_network.id,
        ip_version='4',
        cidr=cidr_net,
        gateway_ip=gateway)

    print(example_subnet)

def open_port(name,data_dir,proto,portMax, portMin):
    print("Open a port:")

    example_sec_group = conn.network.create_security_group(
        name=name)

    print(example_sec_group)

    example_rule = conn.network.create_security_group_rule(
        security_group_id=example_sec_group.id,
        direction=data_dir,
        remote_ip_prefix='0.0.0.0/0',
        protocol=proto,
        port_range_max=portMax,
        port_range_min=portMin,
        ethertype='IPv4')

    print(example_rule)

def create_server(SERVER_NAME, NETWORK_NAME):
    print("Create Server:")
    
    image = conn.compute.find_image(IMAGE_NAME)
    flavor = conn.compute.find_flavor(FLAVOR_NAME)
    network = conn.network.find_network(NETWORK_NAME)

    # keypair = create_keypair(conn)

    server = conn.compute.create_server(
        name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}])#, key_name=keypair.name)

    server = conn.compute.wait_for_server(server)

def create_router():
    conn.network.create_router(name="RouterPy")
    conn.network.add_router_interface({id:"RouterPy"}, subnet_id="NetA")
    conn.network.add_router_interface({id:"RouterPy"}, subnet_id="NetB")
    conn.network.add_router_interface({id:"RouterPy"}, subnet_id="public")