#!/bin/bash

python -m venv ../venv/
source ../venv/bin/activate

pip install -r rex.pip

echo 'NOTE: you may still have to source the venv in future consoles'
echo 'Be sure to now MANUALLY upload REQUIRED secrets'