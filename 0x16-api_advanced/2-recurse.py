#!/usr/bin/python3
from requests import get


def recurse(subreddit, hot_list=[], next_page=''):
    """Iterate through the array """
    if next_page is None:
        return hot_list

    trending = get("https://www.reddit.com/r/{}/hot.json"
                   .format(subreddit), headers={'User-agent': 'Kaiser-bot'},
                   params={'limit': 100, 'after': next_page})
    if trending.status_code == 404:
        return None

    trending_json = trending.json()
    data_dict = trending_json['data']
    data_children = data_dict['children']

    for keys in data_children:
        hot_list.append(keys.get('data').get('title'))

    next_page = data_dict.get('after')
    return recurse(subreddit, hot_list, next_page)
