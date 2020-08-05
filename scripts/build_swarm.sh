#!/bin/bash

#Takes running services and builds swarm! 

source /var/lib/jenkins/.env


if [[ "$(docker stack services secondapp 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml secondapp
fi