#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Function to make a GET request to the Reddit API"""
    if subreddit is None:
        print(None)
        return
    url = 'https://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent': 'mamba'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            data = data['data']['children'][:10]
            for post in data:
                print(post.get('data').get('title', None))
        else:
            print(None)
            return
    except requests.RequestException:
        print(None)
        return
