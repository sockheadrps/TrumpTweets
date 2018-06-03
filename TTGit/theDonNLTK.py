import tweepy
from tweepy import OAuthHandler
from collections import *
import os
import json
from unidecode import unidecode

ckey = 'xxxx'
csecret = 'xxxx'
atoken = 'xxxx'
asecret = 'xxxx'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
tweet_list = api.user_timeline("realDonaldTrump", count=350, tweet_mode="extended")

#Unused, still working on this
def send_to_json(aDict):
	with open("TTJSON.txt", "w") as f:
		json_dict = json.dumps(list(aDict))
		f.write(json_dict)
		print('dumped')

#checks tweets we have seen
def get_saved_tweets(): 
	if not os.path.isfile("TrumpTweetIDs.txt"):
		trumpTweets = []
	else:
		with open("TrumpTweetIDs.txt", "r") as f:
			trumpTweets = f.read()                           
			trumpTweets = trumpTweets.split() 		
	return trumpTweets

#Gathers tweets with the ID that we have not already processed
def gather_tweets(saved_tweets):	#function gathers full tweets and saves in a .txt
	for tweet in tweet_list: 	#For each tweet specified in set up of tweet_list	
		if str(tweet.id) not in saved_tweets and not tweet.retweeted and ('RT @' not in tweet.full_text): 	#if tweet ID has not been saved, and tweet is not a RT
			print(tweet.id)
			with open ("NaturalTweets.txt", "a", encoding='utf-8') as f:	#add the full unaltered tweet.full_text to a text file
				f.write(str(tweet.full_text) + '\n')
			with open ("TrumpTweetIDs.txt", "a") as f: #add ID to save file
				f.write(str(tweet.id) + '\n')

#Gather tweets (but not ones we've already got)
gather_tweets(get_saved_tweets())