#!/usr/bin/python3
"""
Take GitHub credentials (username and personal access token)
and uses the GitHub API to display your user id
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = (username, password)
    response = requests.get(url, auth=auth)

    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        print("None")
