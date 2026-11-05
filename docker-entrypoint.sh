#!/bin/bash
set -o errexit

uv run metron migrate

uv run metron collectstatic --no-input

exec "$@"