# Task manager BE

-   A website that manage tasks

<br>

## Development by

-   [Python3](https://www.python.org/)
-   [FastAPI](https://fastapi.tiangolo.com/)
-   [PostgreSQL](https://www.postgresql.org/)
-   [Docker & Docker compose](https://www.docker.com/)

<br>

## Build and run server

-   Install [docker & docker-compose](https://www.docker.com/)

-   Change directory to `script` folder

    ```bash
    cd script/
    ```

-   Change access permission for `docker.sh`

    ```bash
    chmod +x docker.sh
    ```

-   Run script build and start server by docker-compose
    ```bash
    ./docker.sh
    ```

<br>

## Project structure

```bash
task_manager_be
├─ docker
│  ├─ docker-compose.yml         # Docker compose file
│  ├─ alembic
│  │  └─ Dockerfile
│  ├─ fastapi
│  │  ├─ auth
│  │  │  └─ Dockerfile
│  │  └─ task
│  │     └─ Dockerfile
│  ├─ nginx
│  │  ├─ Dockerfile
│  │  ├─ config
│  │  │  ├─ fastcgi_params
│  │  │  ├─ mime.types
│  │  ├─ log
│  │  ├─ nginx-crontab
│  │  ├─ nginx.conf.template     # Nginx config file
│  │  └─ run_nginx.sh
│  └─ postgresql
│     ├─ Dockerfile
│     └─ data
├─ environment
│  └─ auth.env.example           # Auth server environment
├─ migration
│  ├─ alembic
│  │  ├─ README
│  │  ├─ env.py
│  │  ├─ script.py.mako
│  │  └─ versions
│  └─ alembic.ini.example        # Alembic config file
├─ requirement
│  ├─ auth.requirements.txt
│  ├─ migration.requirements.txt
│  └─ task.requirements.txt
├─ script
│  ├─ alembic.sh                 # Alembic migrate script
│  └─ docker.sh                  # Build and start server by docker-compose script
└─ src
   ├─ auth
   │  ├─ main.py                 # Authentication application
   │  ├─ constants
   │  ├─ databases
   │  ├─ models
   │  └─ router
   └─ task
      └─ main.py                 # Task application

```
