#!/usr/bin/env bash

set -o errexit

cd "$(dirname "$0")"

poetry install --with dev

poetry run mypy
