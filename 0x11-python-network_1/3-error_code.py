#!/usr/bin/python3
"""
Python script that takes a URL, sends a request, and displays the body of the
response. It handles urllib.error.HTTPError exceptions and prints the HTTP
status code in case of an error.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
