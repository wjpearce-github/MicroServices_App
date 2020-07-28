#!/bin/bash

#Sript to build images if non exist locally to save time!

if [[ "$(docker images -q coolwill92/service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t coolwill92/service_1 ./Service_1
    docker push coolwill92/service_1
else
    docker pull coolwill92/service_1
fi

if [[ "$(docker images -q coolwill92/service_2:latest 2> /dev/null)" == "" ]]; then
    docker build -t coolwill92/service_2 ./Service_2
    docker push coolwill92/service_2
else
    docker pull coolwill92/service_2
fi

if [[ "$(docker images -q coolwill92/service_3:latest 2> /dev/null)" == "" ]]; then
    docker build -t coolwill92/service_3 ./Service_3
    docker push coolwill92/service_3
else
    docker pull coolwill92/service_3
fi

if [[ "$(docker images -q coolwill92/service_4:latest 2> /dev/null)" == "" ]]; then
    docker build -t coolwill92/service_4 ./Service_4
    docker push forcoolwill92row/service_4
else
    docker pull coolwill92/service_4
fi