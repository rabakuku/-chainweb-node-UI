#!/bin/bash
cat /var/lib/docker/containers/91f325d4f0dc731b7b7e20ed40a8ecbd5ae0e0ca8c65af744233a957e0c29c79/91f325d4f0dc731b7b7e20ed40a8ecbd5ae0e0ca8c65af744233a957e0c29c79-json.log | grep "solved block" | sed 's/^.*\(".*Z\).*$/\1/' > /root/flask_project/textfile.txt
