# ALX Python Network Projects

This repository contains Python scripts developed for the ALX Higher Level Programming curriculum, specifically for network-related tasks. The projects cover various aspects of network programming in Python, including HTTP requests, fetching internet resources, handling response headers, working with APIs, and error handling.

## Project Details

### 0. What's my status? #0
- File: `0-hbtn_status.py`
- Description: This script fetches the status of https://alx-intranet.hbtn.io/status using the urllib package and displays the body response.

### 1. Response header value #0
- File: `1-hbtn_header.py`
- Description: This script takes a URL as input, sends a request to the URL using urllib, and displays the value of the X-Request-Id variable found in the header of the response.

### 2. POST an email #0
- File: `2-post_email.py`
- Description: This script takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response (decoded in utf-8). Implemented using urllib package.

### 3. Error code #0
- File: `3-error_code.py`
- Description: This script takes a URL as input, sends a request to the URL using urllib, and displays the body of the response. It handles urllib.error.HTTPError exceptions and prints the HTTP status code in case of an error.

### 4. What's my status? #1
- File: `4-hbtn_status.py`
- Description: This script fetches the status of https://alx-intranet.hbtn.io/status using the requests package and displays the body response.

### 5. Response header value #1
- File: `5-hbtn_header.py`
- Description: This script takes a URL as input, sends a request to the URL using requests, and displays the value of the variable X-Request-Id in the response header.

### 6. POST an email #1
- File: `6-post_email.py`
- Description: This script takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response. Implemented using requests package.

### 7. Error code #1
- File: `7-error_code.py`
- Description: This script takes a URL as input, sends a request to the URL using requests, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message with the HTTP status code.

### 8. Search API
- File: `8-json_api.py`
- Description: This script takes a letter as input, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter, and displays the JSON response. It handles different cases and prints specific messages based on the response.

### 9. My GitHub!
- File: `10-my_github.py`
- Description: This script takes GitHub credentials (username and personal access token) as input and uses the GitHub API to display the user's id. It utilizes Basic Authentication with a personal access token to access the user's information.

## General Requirements
- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Code should use pycodestyle (version 2.8.*) for style checks
- All modules should have documentation explaining their purpose
- Code should not be executed when imported (by using `if __name__ == "__main__":`)
- Use of `get` to access dictionary values by key
- No plagiarism or copying of code is allowed
- Detailed requirements for each script are specified in the project description


- **Guillaume, CTO at Holberton School**
- **Weight: 1**
- **Project Start Date: Sep 29, 2023 6:00 AM**
- **Project End Date: Sep 30, 2023 6:00 AM**
- **Checker Released: Sep 29, 2023 12:00 PM**
