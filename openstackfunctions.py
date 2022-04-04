def get_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d
    
def createNetwork():
    from neutronclient.v2_0 import client
    from credentials import get_credentials

    network_name = 'sample_network'
    credentials = get_credentials()
    neutron = client.Client(**credentials)
    try:
        body_sample = {'network': {'name': network_name,
                       'admin_state_up': True}}

        netw = neutron.create_network(body=body_sample)
        net_dict = netw['network']
        network_id = net_dict['id']
        print('Network %s created' % network_id)

        body_create_subnet = {'subnets': [{'cidr': '192.168.199.0/24',
                              'ip_version': 4, 'network_id': network_id}]}

        subnet = neutron.create_subnet(body=body_create_subnet)
        print('Created subnet %s' % subnet)
    finally:
        print("Execution completed")

        print("vn deployment")

def createPorts():
    from neutronclient.v2_0 import client
    import novaclient.v1_1.client as nvclient
    from credentials import get_credentials
    from credentials import get_nova_credentials

    credentials = get_nova_credentials()
    nova_client = nvclient.Client(**credentials)

    # Replace with server_id and network_id from your environment

    server_id = '9a52795a-a70d-49a8-a5d0-5b38d78bd12d'
    network_id = 'ce5d204a-93f5-43ef-bd89-3ab99ad09a9a'
    server_detail = nova_client.servers.get(server_id)
    print(server_detail.id)

    if server_detail != None:
        credentials = get_credentials()
        neutron = client.Client(**credentials)

        body_value = {
                         "port": {
                                 "admin_state_up": True,
                                 "device_id": server_id,
                                 "name": "port1",
                                 "network_id": network_id
                          }
                     }
        response = neutron.create_port(body=body_value)
        print(response)

def listNetwork():
    #!/usr/bin/env python
    from neutronclient.v2_0 import client
    from credentials import get_credentials
    from utils import print_values

    credentials = get_credentials()
    neutron = client.Client(**credentials)
    netw = neutron.list_networks()

    print_values(netw, 'networks')
def deployOsSec():
    print("sec group deployment")
