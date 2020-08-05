#!/bin/bash

#Takes running services and builds swarm! 

source /home/William/Second_App.bashrc

if [[ "$(docker stack services secondapp 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml secondapp
fi