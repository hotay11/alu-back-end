#!/usr/bin/python3
"""Recursively count keywords in the titles of hot posts of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the keywords found in hot post titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/student)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    try:
        data = response.json().get("data", {})
    except ValueError:
        return
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0) + title.count(key)
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    results = sorted([(w, c) for w, c in counts.items() if c > 0],
                     key=lambda item: (-item[1], item[0]))
    for word, count in results:
        print("{}: {}".format(word, count))
