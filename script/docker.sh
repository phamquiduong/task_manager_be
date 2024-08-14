#!/bin/bash

copy_if_not_exists() {
    local src=$1
    local dest=$2
    if [ ! -f "$dest" ]; then
        cp "$src" "$dest"
        echo "Copied $src to $dest"
    else
        echo "$dest already exists, skipping copy"
    fi
}


# Change directory to the project root
cd ..


# Create project enviroment file if it doesn't exist
copy_if_not_exists "auth.env.example" "auth.env"


# Copy alembic.ini.example to alembic.ini if it doesn't exist
cd migration || { echo "Failed to change directory to 'migration'"; exit 1; }
copy_if_not_exists "alembic.ini.example" "alembic.ini"
cd ..


# Change directory to docker
cd docker || { echo "Failed to change directory to 'docker'"; exit 1; }

# Down docker-compose
docker-compose down
echo "The Docker containers are down."

# Create docker-compose enviroment file if it doesn't exist
copy_if_not_exists ".env.example" ".env"

# Create Docker network if it doesn't exist
if ! docker network ls | grep -q "task_manager_be_network"; then
    docker network create task_manager_be_network
    echo "Created Docker network 'task_manager_be_network'"
else
    echo "Docker network 'task_manager_be_network' already exists, skipping"
fi

# Build and run Docker containers
docker-compose up --build -d
echo "Docker containers are up and running. Open http://localhost to view docs"
