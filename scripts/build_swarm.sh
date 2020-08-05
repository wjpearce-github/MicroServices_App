#!/bin/bash

#Takes running services and builds swarm! 

source /var/lib/jenkins/.env


docker stack deploy --compose-file docker-compose.yml secondapp
