FROM mcr.microsoft.com/devcontainers/python:2-3.14-trixie

# Install system Tk package for tkinter (Debian/Ubuntu 'python3-tk')
RUN apt-get update \
    && apt-get install -y python3-tk \
    && rm -rf /var/lib/apt/lists/*
