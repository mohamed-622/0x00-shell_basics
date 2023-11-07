#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """return the top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {'User-Agent': 'alx'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
