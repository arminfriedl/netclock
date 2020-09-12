#!/bin/sh

redis-server &

pipenv run flask run --host=0.0.0.0
