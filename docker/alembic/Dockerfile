FROM python:3.11
ENV PYTHONUNBUFFERED 1


# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip


# Install python packet
COPY requirement/migration.requirements.txt /
RUN pip install -r migration.requirements.txt
