#!/usr/bin/env python3
import requests
import twitter

from generate_title import *
import keys

api =  twitter.Api(consumer_key=keys.apikeys["consumer_key"], consumer_secret=keys.apikeys["consumer_secret"], access_token_key=keys.apikeys["access_token_key"], access_token_secret= keys.apikeys["access_token_secret"])

tweet_content = generate_title()
tweet = api.PostUpdate(tweet_content)
