# syntax=docker/dockerfile:1.4
FROM --platform=linux/amd64 python:3.8-slim-buster

# Avoid interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    libhdf5-dev \
    git \
    curl \
    wget \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy your project files
COPY . /app

# Upgrade pip & install dependencies
RUN pip install --upgrade pip setuptools wheel

# Install compatible Rasa version
RUN pip install rasa==3.6.2

# Expose port
EXPOSE 5005

# Run Rasa
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]