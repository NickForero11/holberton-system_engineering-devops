#!/usr/bin/python3
"""Module that contains a handler to interact with the Reddit API.
"""
from requests import get


def recurse(subreddit, hot_list=[], next=None):
    """Fetch a list with all the hot posts of a given subreddit.

    Arguments:
        subreddit (str) - The name of the subreddit that will be processed.

    Keyword Arguments:
        hot_list (list):    The list of hot posts (default: [])
        next (str):         The index to get the next page of posts
                            if it exists (default: None)
        Returns:
        list:    The object of every post containing its data and metadata,
                 If an invalid subreddit is given, return None.
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
