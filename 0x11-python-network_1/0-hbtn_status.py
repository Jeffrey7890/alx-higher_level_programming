#!/usr/bin/python3

""" How to use th urllib module in python """

if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        string = f"""Body response:
    - type: {type(html)}
    - content: {html}
    - utf8 content: {html.decode()}"""
        print(string)
