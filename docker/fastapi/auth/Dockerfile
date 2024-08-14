FROM python:3
ENV PYTHONUNBUFFERED 1


# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip


# Install python packet
COPY auth.requirements.txt /
RUN pip install -r auth.requirements.txt
