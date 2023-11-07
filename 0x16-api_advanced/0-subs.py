#!/usr/bin/python3
"""
Function that queries the Reddit API
and returns the number of subscribers
for a given subreddit.
- Not active users, total subscribers!
- If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'alx'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
