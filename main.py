import time
import tweepy
import wiki_page
import auth as authentication

auth = tweepy.OAuthHandler(authentication.consumer_key, authentication.consumer_secret)
auth.set_access_token(authentication.access_token, authentication.access_token_secret)

def __main__():

    api = tweepy.API(auth)
    api.update_status("#wikipedia\n " + wiki_page.random_wikipedia_page)

__main__()