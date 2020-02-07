#!/usr/bin/python3
"""Module that contains a handler to interact with the Reddit API.
"""
from requests import get


def recurse(subreddit, hot_list=[], next=None):
    """Function to get the titles of the top 10 hot posts
    for a given subreddit.

    Arguments:
        subreddit (str) - The name of the subreddit that will be processed.
    """
    URL = 'https://www.reddit.com/r/{}/hot.json'
    query_params = {'limit': 100}
    if next:
        query_params['after'] = next
    data = get(
        URL.format(subreddit),
        allow_redirects=False,
        headers={'User-Agent': 'fake_user_agent'},
        params=query_params)
    if data.status_code != 200:
        return(None)
    else:
        json_data = data.json()
        parsed_data = json_data.get('data')
        posts = parsed_data.get('children')
        hot_list += posts
        next_list = parsed_data.get('after')
        if next_list:
            return(recurse(subreddit, hot_list, next_list))
        else:
            return(hot_list)
