#!/usr/bin/python3

"""
Write a recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """the recurse funtion queries the reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"user-agent": "custom-agent"}
    params = {"limits": 100, "after": after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            children = data.get('data', {}).get('children', [])

            for post in children:
                hot_list.append(post['data']['title'])

            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except request.RequestException as e:
        return None
