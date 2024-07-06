#!/usr/bin/python3

""" use post request with requests """

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if (r.status_code == 200):
        print(r.text)

    if (r.status_code >= 400):
        print("Error code: {}".format(r.status_code))
