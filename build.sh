#!/usr/bin/env bash
# exit on error
set -o errexit

py manage.py collectstatic --no-input
py manage.py migrate