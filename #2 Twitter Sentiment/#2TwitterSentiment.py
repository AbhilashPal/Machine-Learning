import tweepy 
from textblob import TextBlob 
import csv

# Setting up the API
consumer_key = '3ZSHsozYDrE0dr9YzGjiNpNaL'
consumer_secret = 'B2e7vk6NfuhxU0k5GC1br8X6o4W17idQnFj8Tjc8SI6BPo2ish'

access_token = '921391316574945280-4uCpUK9zsyAlcmWKSns2lcciBRgBEs0'
access_token_secret = 'xvoOJitWZcauaDXln8pPlYOXuNA9iS6gU2tFWXgpDm2vB'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


# Searching using the API 
#sr = str(input("Enter An Item to try Sentiment Analysis:"))
sr = "trump"
public_tweets = api.search(sr, count=100)

# Opening a new CSV file
path = "Tweet_Sentiment.csv"
file = open(path,'w')
writer = csv.writer(file)
writer.writerow(["RECORD NUMBER","TWEET","SENTIMENT","SENTIMENT RATING(-1 to +1)"],)		# Column Headers writter.

c= 0
for tweet in public_tweets:		# Iterate Through.
	c+=1
	analysis = TextBlob(tweet.text)
	if float(analysis.sentiment[0]) > 0:
		senti = "Positive"
	elif float(analysis.sentiment[0]) < 0:
		senti = "Negative"
	else:
		senti = "Neutral"
	try:
		writer.writerow([c,tweet.text.encode("utf-8").decode("utf-8",'ignore'),senti,analysis.sentiment[0]])
	except UnicodeEncodeError:
		pass
print("Files written to Tweet_Sentiment.csv alongside the Sentiment Generated.")