#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recurse it!"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Python3'}
    params = {'after': after}
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        after = data.get('data').get('after')
        children = data.get('data').get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
