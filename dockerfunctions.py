import os

def docker_file_generate(filenames):
    for file in filenames:
        os.system(f"docker build -t {file} ./{file}/. ")
    print('make docker file')
def spin_up_containers():
    print("docker call to spin container")

