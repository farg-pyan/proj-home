#!/usr/bin/sh

python -m venv ../venv/
source ../venv/bin/activate

pip install -r reqs.pip

echo 'NOTE: you may still have to source the venv in future consoles'
echo 'Be sure to now MANUALLY upload REQUIRED secrets'