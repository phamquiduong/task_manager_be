FROM python:3.11
ENV PYTHONUNBUFFERED 1


# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip


# Install python packet
COPY requirement/auth.requirements.txt /
RUN pip install -r auth.requirements.txt
