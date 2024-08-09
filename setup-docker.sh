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

# Step 1: Copy alembic.ini.example to alembic.ini if it doesn't exist
copy_if_not_exists "alembic.ini.example" "alembic.ini"

# Step 2: Copy .env.example to .env if it doesn't exist
copy_if_not_exists ".env.example" ".env"

# Step 3: Change directory to docker
cd docker || { echo "Failed to change directory to 'docker'"; exit 1; }
echo "Changed directory to 'docker'"

# Step 4: Down docker-compose
docker-compose down
echo "The Docker containers are down."

# Step 5: Copy .env.example to .env if it doesn't exist (inside docker directory)
copy_if_not_exists ".env.example" ".env"

# Step 6: Create Docker network if it doesn't exist
if ! docker network ls | grep -q "task_manager_be_network"; then
    docker network create task_manager_be_network
    echo "Created Docker network 'task_manager_be_network'"
else
    echo "Docker network 'task_manager_be_network' already exists, skipping"
fi

# Step 7: Build and run Docker containers
docker-compose up --build -d
echo "Docker containers are up and running"

# Step 8: Run migrate
docker-compose exec alembic alembic upgrade head
echo "All migrations have been applied."
