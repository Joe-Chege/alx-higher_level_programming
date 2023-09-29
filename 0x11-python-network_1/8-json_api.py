#!/usr/bin/python3
"""
Python script that takes a letter, sends a POST request with the letter as a
parameter, and displays the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
