#!/usr/bin/python3
"""
A function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests
from sys import argv


def top_ten(subreddit):
    """Returns the titles of the top 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {
            "User-Agent": "Mozilla/5.0"
            }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            titles = [post['data']['title'] for post in posts]
            for title in titles:
                print(title)
        else:
            print(None)
    except request.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
