#!/bin/bash

cd /home/appuser/app/grenseed/

python manage.py migrate

exec "$@"