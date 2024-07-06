#!/usr/bin/python3

""" Handling HTTP status code """

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode())
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
