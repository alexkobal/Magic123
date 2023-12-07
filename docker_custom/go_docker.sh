#!/usr/bin/env bash

# Check if container exists
if [ "$(docker ps -q -a -f name=magic123)" ]; then
    if [ "$(docker ps -q -f name=magic123)" ]; then
        echo "Container exists and is running, no op"
    else
        echo "Container exists but is not running, start it"
        docker start magic123
    fi
    echo "Container exists and running, exec it"
    docker exec -it magic123 bash
else
    # Container does not exist, run it
    echo "Container does not exist, run it"
    docker run -it \
        --runtime=nvidia \
        --gpus all \
        --name magic123 \
        -w /workdir/Magic123 \
        -v "$1":/data \
        magic123:local
fi
