#!/bin/sh

redis-server &

pipenv run flask run
