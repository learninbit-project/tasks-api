#!/bin/bash

# build.sh
pip install -r requirements.txt

# make migrations
python3.11 manage.py migrate
python3.11 manage.py collectstatic --noinput
