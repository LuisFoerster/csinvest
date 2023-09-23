#!/bin/bash
# Install the dependencies in the project using Poetry
poetry install
# Upgrade the database
./.venv/bin/python -m alembic upgrade head
# install frontend dependecies
npm install --prefix ./static