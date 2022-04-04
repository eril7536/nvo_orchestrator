import os


def ryuConf():
    bgp_conf = """
from __future__ import absolute_import

import os

from ryu.services.protocols.bgp.bgpspeaker import RF_VPN_V4
from ryu.services.protocols.bgp.bgpspeaker import RF_VPN_V6
from ryu.services.protocols.bgp.bgpspeaker import RF_L2_EVPN
from ryu.services.protocols.bgp.bgpspeaker import RF_VPNV4_FLOWSPEC
from ryu.services.protocols.bgp.bgpspeaker import RF_VPNV6_FLOWSPEC
from ryu.services.protocols.bgp.bgpspeaker import RF_L2VPN_FLOWSPEC
from ryu.services.protocols.bgp.bgpspeaker import EVPN_MAX_ET
from ryu.services.protocols.bgp.bgpspeaker import ESI_TYPE_LACP
from ryu.services.protocols.bgp.bgpspeaker import ESI_TYPE_MAC_BASED
from ryu.services.protocols.bgp.bgpspeaker import EVPN_ETH_AUTO_DISCOVERY
from ryu.services.protocols.bgp.bgpspeaker import EVPN_MAC_IP_ADV_ROUTE
from ryu.services.protocols.bgp.bgpspeaker import TUNNEL_TYPE_VXLAN
from ryu.services.protocols.bgp.bgpspeaker import EVPN_MULTICAST_ETAG_ROUTE
from ryu.services.protocols.bgp.bgpspeaker import EVPN_ETH_SEGMENT
from ryu.services.protocols.bgp.bgpspeaker import EVPN_IP_PREFIX_ROUTE
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_IPV4
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_IPV6
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_VPNV4
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_VPNV6
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_L2VPN
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_TA_SAMPLE
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_TA_TERMINAL
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_POP
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_PUSH
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_SWAP
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_RW_INNER
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_RW_OUTER
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_TPID_TI
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_TPID_TO
from ryu.services.protocols.bgp.bgpspeaker import REDUNDANCY_MODE_SINGLE_ACTIVE

# =============================================================================
# BGP configuration.
# =============================================================================
BGP = {

    # AS number for this BGP instance.
    'local_as': '1',

    # BGP Router ID.
    'router_id': '172.17.0.1',

    # Default local preference
    'local_pref': 100,

    # List of TCP listen host addresses.
    'bgp_server_hosts': ['0.0.0.0', '::'],

    # List of BGP neighbors.
    # The parameters for each neighbor are the same as the arguments of
    # BGPSpeaker.neighbor_add() method.
    'neighbors': [
        {
            'address': '172.17.0.2',
            'remote_as': 2,
            'enable_ipv4': True,
        },
    ],
    # List of BGP routes.
    # The parameters for each route are the same as the arguments of
    # the following methods:
    # - BGPSpeaker.prefix_add()
    # - BGPSpeaker.evpn_prefix_add()
    # - BGPSpeaker.flowspec_prefix_add()
    'routes': [
        # Example of IPv4 prefix
        {
            'prefix': '10.10.1.0/24',
        },
    ],
}


# =============================================================================
# SSH server configuration.
# =============================================================================
SSH = {
    'ssh_port': 4990,
    'ssh_host': 'localhost',
    # 'ssh_host_key': '/etc/ssh_host_rsa_key',
    # 'ssh_username': 'ryu',
    # 'ssh_password': 'ryu',
}


"""
    with open("./ryuBgp/bgp_conf.py","w") as file:
            file.write(bgp_conf)
    print("build ryu bgp conf file")


def quaggaConf(local_as,neighbor_id,remote_as):
    daemons = """
# This file tells the frr package which daemons to start.
#
# Sample configurations for these daemons can be found in
# /usr/share/doc/frr/examples/.
#
# ATTENTION:
#
# When activating a daemon for the first time, a config file, even if it is
# empty, has to be present *and* be owned by the user and group "frr", else
# the daemon will not be started by /etc/init.d/frr. The permissions should
# be u=rw,g=r,o=.
# When using "vtysh" such a config file is also needed. It should be owned by
# group "frrvty" and set to ug=rw,o= though. Check /etc/pam.d/frr, too.
#
# The watchfrr, zebra and staticd daemons are always started.
#
bgpd=yes
ospfd=no
ospf6d=no
ripd=no
ripngd=no
isisd=no
pimd=no
ldpd=no
nhrpd=no
eigrpd=no
babeld=no
sharpd=no
pbrd=no
bfdd=no
fabricd=no
vrrpd=no
pathd=no

#
# If this option is set the /etc/init.d/frr script automatically loads
# the config via "vtysh -b" when the servers are started.
# Check /etc/pam.d/frr if you intend to use "vtysh"!
#
vtysh_enable=yes
zebra_options="  -A 127.0.0.1 -s 90000000"
bgpd_options="   -A 127.0.0.1"
ospfd_options="  -A 127.0.0.1"
ospf6d_options=" -A ::1"
ripd_options="   -A 127.0.0.1"
ripngd_options=" -A ::1"
isisd_options="  -A 127.0.0.1"
pimd_options="   -A 127.0.0.1"
ldpd_options="   -A 127.0.0.1"
nhrpd_options="  -A 127.0.0.1"
eigrpd_options=" -A 127.0.0.1"
babeld_options=" -A 127.0.0.1"
sharpd_options=" -A 127.0.0.1"
pbrd_options="   -A 127.0.0.1"
staticd_options="-A 127.0.0.1"
bfdd_options="   -A 127.0.0.1"
fabricd_options="-A 127.0.0.1"
vrrpd_options="  -A 127.0.0.1"
pathd_options="  -A 127.0.0.1"

# configuration profile
#
#frr_profile="traditional"
#frr_profile="datacenter"

#
# This is the maximum number of FD's that will be available.
# Upon startup this is read by the control files and ulimit
# is called.  Uncomment and use a reasonable value for your
# setup if you are expecting a large number of peers in
# say BGP.
#MAX_FDS=1024

# The list of daemons to watch is automatically generated by the init script.
#watchfrr_options=""

# To make watchfrr create/join the specified netns, use the following option:
#watchfrr_options="--netns"
# This only has an effect in /etc/frr/<somename>/daemons, and you need to
# start FRR with "/usr/lib/frr/frrinit.sh start <somename>".

# for debugging purposes, you can specify a "wrap" command to start instead
# of starting the daemon directly, e.g. to use valgrind on ospfd:
#   ospfd_wrap="/usr/bin/valgrind"
# or you can use "all_wrap" for all daemons, e.g. to use perf record:
#   all_wrap="/usr/bin/perf record --call-graph -"
# the normal daemon command is added to this at the end.

    """
    bgpd_conf = f"""
    router bgp {local_as}
    address-family ipv4 unicast
     network 99.99.99.0/24
    exit-address-family
    neighbor {neighbor_id} remote-as {remote_as}
    """
    with open("./frrBgp/daemons","w") as file:
            file.write(daemons)
    with open("./frrBgp/bgpd.conf","w") as file:
            file.write(bgpd_conf)
            
    print("build frr conf files")