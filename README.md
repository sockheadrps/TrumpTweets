# TrumpTweets
This project by default processes language used by trump in his most recent tweets. 

It can be suited to other twitter users by changing the username in the Twitter API calls. 

Fill in your API information in theDonNLTK.py and run it. 
This will create two files in the same directory as thedonNLTK.py: 
  1. NaturalTweets.txt
  2. TrumpTweetIDs.txt 

After creating these files run vrbnTT.py to view most used proper nouns by default. 

Change pos_type to a valid NLTK POS identifier  

Change most_common_to_search to desired range (Most used to least used range is determined by this variable)  

### Requirements ###
Python 3.5

nltk

collections

pumpy

matplotlib

tweepy

os

json

unidecode

