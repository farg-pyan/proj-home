#!/usr/bin/sh

# remember to set environment when running locally
# RNV=dev ./sh/dump.sh

# mkdir -p tmp_data

./manage.py dumpdata --indent 2 --format json --output ../dump-all-$(date +%s).json \
--exclude admin \
--exclude auth \
--exclude contenttypes \
--exclude sessions \
--exclude dpa_aux_users