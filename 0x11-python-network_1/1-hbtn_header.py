#!/usr/bin/python3

""" Get the X-Request-Id from the response header"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request_id = response.info().get("X-Request-Id")
        print(request_id)
