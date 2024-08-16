import subprocess
def stop():
    ip = "172.18.0.3"

    cmd = "docker network inspect my_network --format='{{range .Containers}}{{.Name}}:{{.IPv4Address}} {{end}}'"
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

    containers = res.stdout.decode().split(" ")
    for i in containers:
        print(i)
    
    # for container in containers:
    #     container_name = container.split(":")[0]
    #     container_ip = container.split(":")[1].split("/")[0]
    #     if container_ip == ip:
    #         print(f"Container Name: {container_name}")
    #         print(f"Container IP: {container_ip}")
    #         # stop and remove container with subprocess
    #         cmd = f"docker stop {container_name} && docker rm {container_name}"
    #         res = subprocess.run(cmd, shell=True)
    #         if res.returncode == 0:
    #             print(f"Container with ip: {ip} stopped and removed!")
    #             return
    #         else:
    #             print("Error:", res.stderr)
    #             return
            
    # print(f"No container found with IP {ip}")


stop()
