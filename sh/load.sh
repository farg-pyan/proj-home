#!/usr/bin/sh

# remember to set environment when running locally
# RNV=dev ./sh/load.sh

./manage.py migrate
./manage.py loaddata ../secrets/admin.json