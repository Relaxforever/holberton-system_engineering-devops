#!/usr/bin/python3
from requests import get


def number_of_subscribers(subreddit):
    """Checks the number of susbscribers in a subreddit"""
    trending = get("https://www.reddit.com/r/{}/about.json"
                   .format(subreddit), headers={'User-agent': 'Kaiser-bot'})
    if trending.status_code == 404:
        return 0
    trending_json = trending.json()
    data_dict = trending_json['data']
    return data_dict['subscribers']
