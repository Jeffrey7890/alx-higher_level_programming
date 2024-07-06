#!/usr/bin/python3

""" Show how to use post request with urllib """

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'email': email}
    headers = {'User-Agent': user_agent}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode())
