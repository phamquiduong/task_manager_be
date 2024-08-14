#!/bin/bash

echo "Choose an option:"
echo "1. Create Alembic migration"
echo "2. Upgrade migration"
echo "3. Downgrade migration"
read -p "Enter your choice (1/2/3): " choice

cd ../docker/

case $choice in
    1)
        read -p "Enter migration message: " message
        docker-compose exec alembic alembic revision -m "$message"
        ;;
    2)
        docker-compose exec alembic alembic upgrade head
        ;;
    3)
        docker-compose exec alembic alembic downgrade -1
        ;;
    *)
        echo "Invalid option. Please choose 1, 2, or 3."
        ;;
esac
