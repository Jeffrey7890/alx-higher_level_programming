#!/usr/bin/python3

""" send json data to siite """

import sys
import requests

if __name__ == "__main__":
    argv = sys.argv

    if (len(argv) < 2):
        print("No result")
        exit()

    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1]

    payload = {'q': q}
    r = requests.post(url, data=payload)
    try:
        data = r.json()
    except Exception:
        print('Not a valid JSON')
        exit()

    if (len(data) == 0):
        print('No result')
    print(f"[{data.get('id')}] {data.get('name')}")
