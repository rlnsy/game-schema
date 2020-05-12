#!/bin/bash

CONFIG="docker/backend.yml"

if [[ $1 == "--frontend" ]]; then
    cd frontend
    yarn install && yarn serve
else
    if [[ $1 == "--full-deployment" ]]; then
        CONFIG="docker/full-stack.yml"
    fi
    chmod +x app/docker_entry.sh
    echo "Going up"
    docker-compose -f "$CONFIG" up --build
    echo "Coming down"
    docker-compose -f "$CONFIG" down
fi
