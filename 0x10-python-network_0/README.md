# Project: Python - Network #0

## Table of Contents
1. [Introduction](#introduction)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Copyright and Plagiarism](#copyright-and-plagiarism)
5. [Requirements](#requirements)
6. [Tasks](#tasks)

## Introduction
Welcome to the Python - Network #0 project! This project is designed to help you understand and work with various aspects of network protocols, HTTP, and web development. You will complete a series of tasks and quizzes to enhance your knowledge in these areas.

## Resources
Before starting the tasks, it is recommended to read or watch the following resources:
- [HTTP (HyperText Transfer Protocol)](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) (except: "TRACE" Request Method, "CONNECT" Request Method, Language Negotiation and "Options MultiView" and Character Set Negotiation)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

## Learning Objectives
By the end of this project, you are expected to be able to explain the following concepts to anyone, without the help of Google:

### General
- What a URL is
- What HTTP is
- How to read a URL
- The scheme for an HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type "google.com" in your browser (Application level)

## Copyright and Plagiarism
- You are tasked with coming up with solutions for the tasks independently to meet the learning objectives.
- Copying and pasting someone else's work is strictly prohibited.
- You are not allowed to publish any content from this project.
- Any form of plagiarism will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- A README.md file, at the root of the folder of the project, is mandatory.
- All your scripts will be tested on Ubuntu 20.04 LTS.
- All your Bash scripts should be exactly 3 lines long (`wc -l file` should print 3).
- All your files should end with a new line.
- All your files must be executable.
- The first line of all your bash files should be exactly `#!/bin/bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.
- All curl commands must have the option `-s` (silent mode).
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- The first line of all your Python files should be exactly `#!/usr/bin/python3`.
- Your code should use the pycodestyle (version 2.8.*).
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`.
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`.
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`.
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).

## Tasks
### Task 0: cURL Body Size
- Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
- The size must be displayed in bytes.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

### Task 1: cURL to the End
- Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
- Display only the body of a 200 status code response.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

### Task 2: cURL Method
- Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

### Task 3: cURL Only Methods
- Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

### Task 4: cURL Headers
- Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
- A header variable X-School-User-Id must be sent with the value 98.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

### Task 5: cURL POST Parameters
- Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.
- A variable email must be sent with the value test@gmail.com.
- A variable subject must be sent with the value I will always be here for PLD.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

### Task 6: Find a Peak
- Write a function that finds a peak in a list of unsorted integers.
- Prototype: def find_peak(list_of_integers)
- You are not allowed to import any module.
- Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak).
- Note: there may be more than one peak in the list.

