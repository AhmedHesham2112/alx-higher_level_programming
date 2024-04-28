#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
