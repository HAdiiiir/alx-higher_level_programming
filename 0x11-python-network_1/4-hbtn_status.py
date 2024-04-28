#!/usr/bin/python3

"""
get https://alx-intranet.hbtn.io/status using
requests and print the response to stdout
"""

from requests import get


def get_alx_intranet(url='https://alx-intranet.hbtn.io/status'):
    """
    Send a GET request to the url
    and print the response
    """
    res = get(url)
    print("Body response:")
    print("\t- type:", type(res))
    print("\t- content:", res.text)


if __name__ == "__main__":
    get_alx_intranet()
