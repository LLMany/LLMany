#!/usr/bin/env bash

set -o errexit

cd "$(dirname "$0")"

cd backend

poetry install --with dev

poetry run mypy llmany_backend/ tests/
