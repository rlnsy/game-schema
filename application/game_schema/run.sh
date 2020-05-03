#!/bin/bash

chmod +x docker_entry.sh
echo "Going up"
docker-compose up
echo "Coming down"
docker-compose down
