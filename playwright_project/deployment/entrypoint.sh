#!/bin/sh
set -ex

envsubst < env/.env.template > .env

exec "$@"
