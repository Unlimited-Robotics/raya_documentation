#!/bin/bash

PYRAYA_PATH=$HOME/ur_dev/pyraya

VOLUMES=(
    -v $PYRAYA_PATH:/pyraya
    -v $(pwd)/src:/raya_documentation/src:ro
    -v $(pwd)/docs:/raya_documentation/docs
)

#    -u $(id -u):$(id -g) \
docker run -it \
    --rm \
    --name raya_documentation \
    -e USER_ID=$(id -u) \
    -e GROUP_ID=$(id -g) \
    "${VOLUMES[@]}" \
    ros:galactic \
    bash