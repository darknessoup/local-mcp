#!/bin/bash

ROOT_DIR_PATH=$(git rev-parse --show-toplevel)

# ensure user and Ids are correct
USER=$(whoami)

DEV_CONTAINER_FOLDER="${ROOT_DIR_PATH}/.devcontainer"
export DOCKER_IMAGE_NAME="local_mcp_${USER}"
docker build -f ${DEV_CONTAINER_FOLDER}/Dockerfile \
    --build-arg DOCKER_IMAGE="${DOCKER_IMAGE}" \
    --build-arg USERNAME="${USER}" \
    --build-arg USER_UID="$(id -u)" \
    --build-arg USER_GID="$(id -g)" \
    --build-arg HOME="${HOME}" \
    -t ${DOCKER_IMAGE_NAME} .

