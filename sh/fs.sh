#!/usr/bin/sh

# https://www.reddit.com/r/linux/comments/mk9wuq/cli_replacement_for_baobab_disk_usage_analyzer/

# e.g.,
# ./sh/du.sh ~/venv/lib/python3.10/site-packages

# see also ncdu

if [ -z "$1" ]; then
    du -hs -- * 2>/dev/null | sort -rh | head -n 25
else
    du -hs --  $1/* 2>/dev/null | sort -rh | head -n 25
fi