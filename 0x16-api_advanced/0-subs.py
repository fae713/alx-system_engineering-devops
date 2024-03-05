#!/usr/bin/python3
"""
A function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total subscriber for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Setting the header to prevent too many requests errors
    headers = {
            "User-Agent": "Mozilla/5.0"
            }
    # Make a GET request to the reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        # Returns the exact number of subscribers
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
