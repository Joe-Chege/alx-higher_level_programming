#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status using urllib
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()

    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")
    print(f"    - utf8 content: {content.decode('utf-8')}")