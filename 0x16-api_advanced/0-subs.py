#!/usr/bin/python3
"""
Makes a GET request to the redit api and returns the number
of subscribers for a given subredit
"""
import requests


def number_of_subscribers(subreddiit):
    """Function to make a GET request to the reditapi"""
    if subreddiit is None:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddiit)

    with requests.get(url, allow_redirects=False) as res:
        res = res.json()

    if 'subscribers' not in res.get('data'):
        return 0
    else:
        return res.get('data').get('subscribers')
