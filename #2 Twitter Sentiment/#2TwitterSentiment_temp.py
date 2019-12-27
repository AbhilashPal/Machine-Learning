import tweepy 
from textblob import TextBlob 

consumer_key = '3ZSHsozYDrE0dr9YzGjiNpNaL'
consumer_secret = 'B2e7vk6NfuhxU0k5GC1br8X6o4W17idQnFj8Tjc8SI6BPo2ish'

access_token = '921391316574945280-4uCpUK9zsyAlcmWKSns2lcciBRgBEs0'
access_token_secret = 'xvoOJitWZcauaDXln8pPlYOXuNA9iS6gU2tFWXgpDm2vB'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')
c = 0
for tweet in public_tweets:
	print("==============TWEET NUMBER : {}".format(c),"================")
	c+=1
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
