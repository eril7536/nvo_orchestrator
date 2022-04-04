import openstack


# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize connection
conn = openstack.connect(cloud='admin')

# List the servers
for server in conn.compute.servers():
    print(server.to_dict())