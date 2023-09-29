#!/usr/bin/python3
"""
Python script that takes a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an exception if the request returned an unsuccessful status code

        print("Your email is: {}".format(response.text))

    except requests.exceptions.HTTPError as errh:
        print(f'HTTP Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        print(f'Error Connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        print(f'Timeout Error: {errt}')
    except requests.exceptions.RequestException as err:
        print(f'Request Exception: {err}')
