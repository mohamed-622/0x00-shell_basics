#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recurse it!"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers={"User-Agent": "alx"},
                            params={"after": after},
                            allow_redirects=False,
                            )
    if response.status_code == 200:
        data = response.json()
        child = data.get('data').get('children')
        for title in child:
            hot_list.append(title.get('data').get('title'))
        after = response.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
