import docker

print("1")
DCLIENT = docker.APIClient(base_url='unix://var/run/docker.sock',version='auto',timeout=30)
print("2")
DCLIENT.tag('busybox', '10.0.0.10/busybox','test',force=True)
print("3")

