#!/usr/bin/python3
"""
Take a letter, sends a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter. If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name
Otherwise, display appropriate messages for invalid JSON or empty response
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=data)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
