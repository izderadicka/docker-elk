#!/usr/bin/env bash

set -eux
set -o pipefail

VERSION="8.11.1"
SUDO="sudo"
LOGS="/mnt/data/test"
echo Testing instance of filebeat, send *.log from $LOGS
echo staring filebeat v${VERSION}


$SUDO podman run --rm --name filebeat --net host \
    -v "./filebeat/filebeat.yml:/usr/share/filebeat/filebeat.yml:ro,Z" \
    -v "$LOGS:/logs:ro,z" \
    -v "filebeat-registry:/usr/share/filebeat/data:rw" \
    docker.elastic.co/beats/filebeat-oss:${VERSION} \
    -e \
    "${@}"

#------------------------------------------------------------------------------------
    