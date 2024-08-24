#!/bin/bash

# Function to display menu
display_menu() {
    echo "Select the service you want to manage:"
    echo "1) auth_server"
    echo "2) task_server"
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

# Change directory to docker
cd ../docker/ || exit

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
    *) echo "Invalid choice. Please try again." ;;
    esac
done
