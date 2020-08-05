#!/bin/bash

#updates images

docker service update --image coolwill92/service_1:latest secondapp_service_1
sleep 5

docker service update --image coolwill92/service_2:latest secondapp_service_2
sleep 5

docker service update --image coolwill92/service_3:latest secondapp_service_3
sleep 5

docker service update --image coolwill92/service_4:latest secondapp_service_4
sleep 5

docker system prune -f