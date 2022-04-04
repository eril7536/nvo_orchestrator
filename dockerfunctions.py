import os
from bgpSetup import ryuConf,quaggaConf
def docker_file_generate():
    if os.path.isdir("./ryuBgp/") == True:
        os.system(f"docker build -t ryu ./ryuBgp/. ")
        dockerfile_ryu = """
        FROM ubuntu:latest
        RUN apt-get update && apt-get install -y net-tools traceroute inetutils-ping git python3 python3-pip
        RUN git clone https://github.com/faucetsdn/ryu.git
        RUN cd ryu; pip install .
        RUN pip install netmiko

        ADD ryuBgpConf.py ryu/ryu/services/protocols/bgp/

        EXPOSE 6633
        EXPOSE 6653

        CMD ["ryu-manager", "--bgp-app-config", "ryu/ryu/services/protocols/bgp/ryuBgpConf.py","ryu/ryu/services/protocols/bgp/application.py"]
        """
        
        with open("./ryuBgp/Dockerfile","w") as file:
            file.write(dockerfile_ryu)
        ryuConf()
    else:
        os.mkdir("./ryuBgp",0o777)
        docker_file_generate()

    if os.path.isdir("./frrBgp/") == True:
        os.system(f"docker build -t frr ./frrBgp/. ")
        dockerfile_frr = """
        FROM frrouting/frr-debian
        EXPOSE  179
        ADD bgpd.conf /etc/frr/
        ADD daemons /etc/frr/
        CMD ['chmod 640 bgpd.conf && systemctl restart ']
        """
        with open("./frrBgp/Dockerfile","w") as file:
            file.write(dockerfile_frr)
        quaggaConf("1","172.17.0.1","2")
    else:
        os.mkdir("./frrBgp",0o777)
        docker_file_generate()  

    print('made docker files')
    return True

def spin_up_dockers():
    os.system("docker run -itd ryu")
    print("docker call to spin up ryu container")
    os.system("docker run -itd frr")
    print("docker call to spin up frr container")


if docker_file_generate() == True:
    print("docker spin") #
    spin_up_dockers()