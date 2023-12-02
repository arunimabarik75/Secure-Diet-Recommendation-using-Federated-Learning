#!/bin/bash

# Server
echo "Starting server...."
python server.py &
sleep 3  

# 2 Clients
for i in `seq 0 1`; do
    echo "Starting client $i...."
    python client.py &
done

# Use CTRL + C to stop all background processes
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM
wait
