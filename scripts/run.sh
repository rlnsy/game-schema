#!/bin/bash

DEFAULT_STACK="backend"

dev_frontend () {
    cd frontend
    yarn install && yarn serve
    exit 0
}

error () {
    echo "ERROR: $1"
    exit 1
}

STACK=$DEFAULT_STACK
if [[ ! -z "$1" ]]; then 
    STACK=$1 
fi

APP_CONFIG=""

if      [[ $STACK == "frontend"     ]]; then dev_frontend
elif    [[ $STACK == "backend"      ]]; then
                                        APP_CONFIG="app/config/dev/config.json"
                                        CONFIG="docker/backend-dev.yml"
elif    [[ $STACK == "production"   ]]; then
                                        APP_CONFIG="app/config/prod/config.json"
                                        CONFIG="docker/full-stack.yml"
else
        error "Invalid stack"
fi

echo "Running stack $STACK"

if [ ! -z "$APP_CONFIG" ] && [ ! -f "$APP_CONFIG" ]; then
        error "Missing backend configuration at $APP_CONFIG"
fi

chmod +x app/docker_entry.sh
echo "Going up"
docker-compose -f "$CONFIG" up --build
echo "Coming down"
docker-compose -f "$CONFIG" down

exit 0
