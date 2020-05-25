#!/bin/bash

DEFAULT_STACK="backend"

dev_frontend () {
    cd frontend
    yarn install && yarn serve
    exit 0
}

STACK=$DEFAULT_STACK
if [[ ! -z "$1" ]]; then 
    STACK=$1 
fi

if      [[ $STACK == "frontend"     ]]; then dev_frontend
elif    [[ $STACK == "backend"      ]]; then CONFIG="docker/backend-dev.yml"
elif    [[ $STACK == "production"   ]]; then CONFIG="docker/full-stack.yml"
else
        echo "ERROR: Invalid stack"
        exit 1
fi

chmod +x app/docker_entry.sh
echo "Going up"
docker-compose -f "$CONFIG" up --build
echo "Coming down"
docker-compose -f "$CONFIG" down

exit 0
