#!/bin/bash
# This script takes in a URL as an argument, sends a GET request with a custom header, and displays the body of the response.

# Define the URL and header variable
url="$1"
header="X-School-User-Id: 98"

# Use curl to send a GET request with the custom header and display the response body
curl -s -H "$header" "$url"
