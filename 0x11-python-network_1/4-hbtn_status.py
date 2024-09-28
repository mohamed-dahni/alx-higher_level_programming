#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
using the requests package
and displays the body of the response.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
