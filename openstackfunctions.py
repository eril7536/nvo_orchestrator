import openstack


# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize connection
conn = openstack.connect(cloud='admin')

conn.create_server(
    'test1',image= 'a2b43ae8-7ce7-4512-a4f9-994c0fa06ead',flavor='m1.tiny',wait=True,auto_ip=True)

# List the servers
# for server in conn.compute.servers():
#     print(server.to_dict())