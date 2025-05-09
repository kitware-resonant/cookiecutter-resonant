FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN mv /root/.local/bin/uv /usr/local/bin/uv
RUN mv /root/.local/bin/uvx /usr/local/bin/uvx

USER vscode

RUN mkdir /home/vscode/uv

WORKDIR /home/vscode/django-project
