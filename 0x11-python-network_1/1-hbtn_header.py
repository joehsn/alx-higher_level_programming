#!/usr/bin/python3

import urllib.request
import sys


def fetch_request_id(url):
    """Fetches the X-Request-Id from the given URL's response header.

    Args:
        url: The URL to fetch the header from.

    Returns:
        The value of the X-Request-Id header, or None if not found.
    """
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        return headers.get("X-Request-Id")


if __name__ == "__main__":
    url = sys.argv[1]  # Retrieve the URL from the first command-line argument
    request_id = fetch_request_id(url)

    if request_id:
        print(request_id)
    else:
        print("X-Request-Id not found in the response header.")
