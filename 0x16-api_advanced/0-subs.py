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

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
