#!/bin/sh
. docker/env.sh
docker run \
  -dit \
  -v $PWD:/workspace \
  -p 8888:8888 \
  --name $CONTAINER_NAME\
  --rm \
  $IMAGE_NAME