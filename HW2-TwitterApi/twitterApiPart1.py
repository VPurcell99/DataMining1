import json

import tweepy # conda friendly. Most starts of any tweeter API project on Github
from IPython.core.display import HTML
from IPython.display import display
import config

consumer_key = config.apiKey
consumer_secret = config.apiSecretKey
access_token = config.accessToken
access_token_secret = config.accessTokenSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets_from_twitterhandle(api, twitter_handle, number_of_tweets=100):
    for count, tweet in enumerate(tweepy.Cursor(api.user_timeline, screen_name=twitter_handle, tweet_mode='extended').items(number_of_tweets), 1):
        display(HTML('{}. ({}) {}'.format(count, tweet.created_at, tweet.full_text)))

def get_tweets_from_search_term(api, query, number_of_tweets=100):
    for count, tweet in enumerate(tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended').items(number_of_tweets), 1):
        display(HTML('{}. ({} by {}) {}'.format(count, tweet.created_at, tweet.author.screen_name, tweet.full_text)))

get_tweets_from_twitterhandle(api, 'Eagles', 10)