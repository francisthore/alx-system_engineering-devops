#!/usr/bin/python3
"""
Makes a GET request to the Reddit API and returns the number
of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Function to make a GET request to the Reddit API"""
    if subreddit is None:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'mamba'
    }

    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    data = resp.json().get('data')
    return data.get('subscribers')
