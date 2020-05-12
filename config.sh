#!/bin/bash

cp frontend/.env.production frontend/.env.production.local
"$EDITOR" frontend/.env.production.local

cp app/deployment.json app/deployment.local.json
"$EDITOR"  app/deployment.local.json
