#!/usr/bin/python3

""" How to use th urllib module in python """

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    string = f"""Body response:
    - type: {type(html)}
    - content: {html}
    - utf8 content: {html.decode()}"""
    print(string)
