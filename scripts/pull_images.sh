#!/bin/bash


docker pull coolwill92/service_1
docker pull coolwill92/service_2
docker pull coolwill92/service_3
docker pull coolwill92/service_4

# if service exists then docker service update --image 
# coolwill92/services_1 secondapp_service_1