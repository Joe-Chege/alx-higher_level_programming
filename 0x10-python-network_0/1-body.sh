#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response.

response=$(curl -s -w "%{http_code}" -o /dev/null "$1")

if [ "$response" -eq 200 ]; then
    curl -s "$1"
fi
