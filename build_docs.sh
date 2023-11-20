#!/bin/bash


DOCKER_IMAGE_TAG=${1:?"missing arg 1 for DOCKER_IMAGE_TAG"}
PYRAYA_PATH=$HOME/ur_dev/pyraya

VOLUMES=(
    -v $PYRAYA_PATH:/pyraya
    -v $(pwd)/src:/raya_documentation/src:ro
    -v $(pwd)/src/api:/raya_documentation/src/api
    -v $(pwd)/docs:/raya_documentation/docs
)

docker run -it \
    --rm \
    --name raya_documentation \
    -e USER_ID=$(id -u) \
    -e GROUP_ID=$(id -g) \
    "${VOLUMES[@]}" \
    unlimitedrobotics/raya_os.sim_gpu.prod:$DOCKER_IMAGE_TAG \
    bash