#!/bin/bash

# Step 1: Copy alembic.ini.example to alembic.ini if it doesn't exist
if [ ! -f alembic.ini ]; then
    cp alembic.ini.example alembic.ini
    echo "Copied alembic.ini.example to alembic.ini"
else
    echo "alembic.ini already exists, skipping copy"
fi

# Step 2: Change directory to docker
cd docker || { echo "Failed to change directory to 'docker'"; exit 1; }
echo "Changed directory to 'docker'"

# Step 3: Copy .env.example to .env if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Copied .env.example to .env"
else
    echo ".env already exists, skipping copy"
fi

# Step 4: Create Docker network if it doesn't exist
if ! docker network ls | grep -q "task_manager_be_network"; then
    docker network create task_manager_be_network
    echo "Created Docker network 'task_manager_be_network'"
else
    echo "Docker network 'task_manager_be_network' already exists, skipping"
fi

# Step 5: Build and run Docker containers
docker-compose up --build -d
echo "Docker containers are up and running"
