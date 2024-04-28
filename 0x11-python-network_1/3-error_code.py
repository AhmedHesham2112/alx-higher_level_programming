#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('UTF-8'))
    except urllib.error.URLError as e:
        print('Error code: {}'.format(e.code))
