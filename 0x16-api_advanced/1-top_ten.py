#!/usr/bin/python3
from requests import get


def top_ten(subreddit):
    """Checks the number of susbscribers in a subreddit"""
    trending = get("https://www.reddit.com/r/{}.json?limit=10"
                   .format(subreddit), headers={'User-agent': 'Kaiser-bot'})
    if trending.status_code == 404:
        print(None)
        return
    trending_json = trending.json()
    data_dict = trending_json['data']
    data_children = data_dict['children']
    for keys in data_children:
        print(keys.get('data').get('title'))
