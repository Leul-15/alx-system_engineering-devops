#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests
import sys

def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for c in range(10):
                print(children[c].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
