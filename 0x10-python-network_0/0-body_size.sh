#!/bin/bash
# Sends a GET request to a URL and displays the size of the body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
