#!/bin/bash

cp frontend/.env.production frontend/.env.production.local
"$EDITOR" frontend/.env.production.local

cp frontend/nginx.conf frontend/nginx.local.conf
"$EDITOR"  frontend/nginx.local.conf

cp server/nginx.conf server/nginx.local.conf
"$EDITOR"  server/nginx.local.conf

cp app/deployment.json app/deployment.local.json
"$EDITOR"  app/deployment.local.json

echo "Put SSL cert and key in ssl directory and everything should be good"
