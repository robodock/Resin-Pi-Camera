#!/bin/bash
export PASSWD=${PASSWD:=root}
echo "root:$PASSWD" | chpasswd
dropbear -E -F &

python /app/timelapse2.py