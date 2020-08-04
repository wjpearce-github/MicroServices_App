#!/bin/bash

#Takes running services and builds swarm! 

if [[ "$(docker stack services secondapp 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml secondapp
fi