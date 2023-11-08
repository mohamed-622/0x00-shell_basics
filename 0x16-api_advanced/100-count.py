#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
parses the title of all hot articles,
and prints a sorted count of given keywords
case-insensitive, delimited by spaces.
Javascript should count as javascript,
but java should not).
"""
import requests


def count_words(subreddit, word_list, after="", word_dict={}):
    """
    Recurse it!
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            for word in word_list:
                if word.lower() in title.lower():
                    if word.lower() not in word_dict.keys():
                        word_dict[word.lower()] = 1
                    else:
                        word_dict[word.lower()] += 1
        after = req.json().get("data").get("after")

        if after is None:
            if len(word_dict) == 0:
                return
            else:
                for key, value in sorted(word_dict.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print("{}: {}".format(key, value))
                return
        else:
            return count_words(subreddit, word_list, after, word_dict)
    else:
        return
