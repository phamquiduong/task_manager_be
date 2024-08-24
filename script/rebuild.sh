#!/bin/bash

# Function to display menu
display_menu() {
    echo "Select the service you want to manage:"
    echo "1) auth_server"
    echo "2) task_server"
    echo "0) All services"
}

# Function to manage the selected service
manage_service() {
    service=$1

    # Down the selected service
    echo "Stopping $service..."
    docker-compose down "$service"

    # Rebuild and start the selected service
    echo "Rebuilding and starting $service..."
    docker-compose up --build "$service" -d
}

# Function to manage all services
manage_all_services() {
    echo "Stopping all services..."
    docker-compose down

    echo "Rebuilding and starting all services..."
    docker-compose up --build -d
}

# Change directory to docker
cd ../docker/

# Main loop
while true; do
    display_menu
    read -rp "Enter your choice: " choice

    case $choice in
    1)
        manage_service "auth_server"
        break
        ;;
    2)
        manage_service "task_server"
        break
        ;;
    0)
        manage_all_services
        break
        ;;
    *) echo "Invalid choice. Please try again." ;;
    esac
done
