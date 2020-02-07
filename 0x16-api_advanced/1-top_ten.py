#!/usr/bin/python3
"""Module that contains a handler to interact with the Reddit API.
"""
from requests import get


def top_ten(subreddit):
    """Function to get the titles of the top 10 hot posts
    for a given subreddit.

    Arguments:
        subreddit (str) - The name of the subreddit that will be processed.
    """
    URL = 'https://www.reddit.com/r/{}/hot.json'
    data = get(
        URL.format(subreddit),
        allow_redirects=False,
        headers={'User-Agent': 'fake_user_agent'},
        params={'limit': 10})
    if data.status_code != 200:
        print(None)
    else:
        json_data = data.json()
        parsed_data = json_data.get('data')
        posts = parsed_data.get('children')
        for post in posts:
            post_data = post.get('data')
            title = post_data.get('title')
            print(title)
