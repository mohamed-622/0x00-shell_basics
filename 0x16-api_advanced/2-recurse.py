#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of all the hot posts
listed for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[None], after=None):
    """return all the hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    if after:
        url += "?after=" + after

    header = {'User-Agent': 'alx'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            hot_list.append(post["data"]["title"])

        next_after = data["data"]["after"]

        if next_after:
            return recurse(subreddit, hot_list, next_after)
        else:
            return hot_list

    else:
        return None
