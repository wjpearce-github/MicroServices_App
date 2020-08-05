#!/bin/bash

#Sript to build images if non exist locally to save time!

docker build -t coolwill92/service_1 ./Service_1
docker push coolwill92/service_1

docker build -t coolwill92/service_2 ./Service_2
docker push coolwill92/service_2


docker build -t coolwill92/service_3 ./Service_3
docker push coolwill92/service_3


docker build -t coolwill92/service_4 ./Service_4
docker push coolwill92/service_4

docker build -t coolwill92/nginx ./NGINX
docker push coolwill92/nginx