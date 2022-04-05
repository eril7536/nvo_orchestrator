import openstack

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

def create_network(conn):
    print("Create Network:")

    example_network = conn.network.create_network(
        name='openstacksdk-example-project-network')

    print(example_network)

    example_subnet = conn.network.create_subnet(
        name='openstacksdk-example-project-subnet',
        network_id=example_network.id,
        ip_version='4',
        cidr='10.0.2.0/24',
        gateway_ip='10.0.2.1')

    print(example_subnet)

def open_port(conn):
    print("Open a port:")

    example_sec_group = conn.network.create_security_group(
        name='openstacksdk-example-security-group')

    print(example_sec_group)

    example_rule = conn.network.create_security_group_rule(
        security_group_id=example_sec_group.id,
        direction='ingress',
        remote_ip_prefix='0.0.0.0/0',
        protocol='HTTPS',
        port_range_max='443',
        port_range_min='443',
        ethertype='IPv4')

    print(example_rule)

def create_server():
    print("Create Server:")

    image = conn.compute.find_image(IMAGE_NAME)
    flavor = conn.compute.find_flavor(FLAVOR_NAME)
    network = conn.network.find_network(NETWORK_NAME)
    keypair = create_keypair(conn)

    server = conn.compute.create_server(
        name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name=keypair.name)

    server = conn.compute.wait_for_server(server)

    # print("ssh -i {key} root@{ip}".format(
    #     key=PRIVATE_KEYPAIR_FILE,
    #     ip=server.access_ipv4))

list_networks(conn)