#!/usr/bin/python3
"""Return the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return total subscribers, or 0 if the subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/student)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    try:
        data = response.json().get("data", {})
    except ValueError:
        return 0
    return data.get("subscribers", 0)
