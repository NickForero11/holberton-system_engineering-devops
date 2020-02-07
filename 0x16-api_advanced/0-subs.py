#!/usr/bin/python3
"""Module that contains a handler to interact with the Reddit API.
"""
from requests import get


def number_of_subscribers(subreddit):
    """Checks the number of subscribers (not active users, total subscribers)
    of a given subreddit.


    Arguments:
        subreddit (str):    The name of the subreddit that will be processed.

    Returns:
        int:    The number of total subscribers of the given subreddit,
                If an invalid subreddit is given, return 0.
    """
    URL = 'https://www.reddit.com/r/{}/about.json'
    data = get(
        URL.format(subreddit),
        allow_redirects=False,
        headers={'User-Agent': 'fake_user_agent'})
    if data.status_code != 200:
        return 0
    json_data = data.json()
    parsed_data = json_data.get('data')
    subscribers = parsed_data.get('subscribers')
    return subscribers
