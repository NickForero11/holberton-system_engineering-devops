#!/usr/bin/python3
"""Module that contains a handler to interact with the Reddit API.
"""
from requests import get


def count_words(subreddit, word_list, next=None, count_dict=None):
    """Prints a sorted count of given keywords in the title of all hot articles
    of a given subreddit.

    It's case insensitive and results are based on the number of times
    a keyword appears.

    Results are printed in descending order by the count.

    Arguments:
        subreddit (str):    The name of the subreddit that will be processed.
        word_list (list):   The list of keywords that will be checked.

    Keyword Arguments:
        next (str):     The index to get the next page of posts
                        if it exists (default: None)
        count_dict:     The dictionary with the count of every keyword
                        in the post titles (default: {None})
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
        print(end='')
    else:
        json_data = data.json()
        parsed_data = json_data.get('data')
        posts = parsed_data.get('children')
        titles = [post.get('data').get('title') for post in posts]
        normalized_word_list = [word.lower() for word in word_list]
        if not count_dict:
            count_dict = {key: 0 for key in normalized_word_list}
        for title in titles:
            parsed_title = [word.lower() for word in title.split(' ')]
            for key in count_dict.keys():
                count_dict[key] += len(
                    list(
                        filter(
                            lambda word: word == key,
                            parsed_title
                        )
                    )
                )
        next_list = parsed_data.get('after')
        if next_list:
            count_words(subreddit, word_list, next_list, count_dict)
        else:
            sorted_results = dict(
                sorted(
                    ((value, key) for (key, value) in count_dict.items()),
                    reverse=True
                )
            )
            for count, key in sorted_results.items():
                if count > 0:
                    word = word_list[normalized_word_list.index(key)]
                    print('{}: {}'.format(word, count))
