#!/usr/bin/python3
""" 2. Recurse it!
    Write a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    Hint: The Reddit API uses pagination for separating pages of responses.
    """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Recurse it! """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Python/requests'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
