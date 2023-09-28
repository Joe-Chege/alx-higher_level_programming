#!/bin/bash
# This script sends a POST request to a URL with specified parameters and displays the response body.

# Define the URL
url="$1"

# Define the POST parameters
email="email=test@gmail.com"
subject="subject=I%20will%20always%20be%20here%20for%20PLD"  # URL-encoded

# Use curl to send a POST request with parameters and display the response body
curl -s -X POST -d "$email" -d "$subject" "$url"
