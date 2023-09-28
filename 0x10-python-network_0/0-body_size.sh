#!/bin/bash

# Get the URL from the command line argument
URL=$1

# Send a request to the URL and save the response body to a file
curl -s -o response $URL

# Get the size of the response body in bytes
SIZE=$(wc -c response)

# Display the size of the response body
echo $SIZE
