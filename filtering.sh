#!/bin/bash

/usr/bin/echo 'Killing gunicorn'
/usr/bin/sleep 1s
pkill gunicorn
/usr/bin/sleep 4s


/usr/bin/echo 'getting latest block'
/usr/bin/sleep 1s
/usr/bin/cat /var/lib/docker/containers/91f325d4f0dc731b7b7e20ed40a8ecbd5ae0e0ca8c65af744233a957e0c29c79/91f325d4f0dc731b7b7e20ed40a8ecbd5ae0e0ca8c65af744233a957e0c29c79-json.log | grep "solved block" | sed 's/^.*\(".*Z\).*$/\1/' | sed 's/[.].*$//' | sed -e 's/^"//' -e 's/"Date//' | sed -e 's/T/ and Time: /g' | sed 's/^/Date: /' > /root//flask_project/get_block.txt


/usr/bin/echo 'starting gunicorn'
/usr/bin/sleep 2s
gunicorn -w 3 --chdir ~ flask_project:app
