#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'linux User Agent 1.0'}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print("Error:", e)
        return 0
