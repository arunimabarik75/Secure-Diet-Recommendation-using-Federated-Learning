#!/bin/bash

# Server
echo "Starting server...."
python server.py &
sleep 3  

# 2 Clients
echo "Starting client 1...."
python client.py 1 &
    
echo "Starting client 2...."
python client.py 2 &

# Use CTRL + C to stop all background processes
trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM
wait
