import tweepy
import csv

#important API info
consumer_key = 'this is proprietary'
consumer_secret = 'this is proprietary'
access_token = 'this is proprietary'
access_token_secret = 'this is proprietary'

#grab the first batch of tweets
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
statuses = (api.user_timeline(id='otasayim',screen_name='Evan Miyasato',count=150,tweet_mode='extended'))
tweets = []
for idx,tweet in enumerate(statuses):
	if(statuses[idx].full_text[0:2]!='RT'):
		tweets.append(statuses[idx].full_text)

#grab the rest of the tweets
for i in range(1,25):
	statuses = (api.user_timeline(id='otasayim',screen_name='Evan Miyasato',max_id=statuses[-1].id_str,count=150,tweet_mode='extended'))
	for idx,tweet in enumerate(statuses):
		if(statuses[idx].full_text[0:2]!='RT'):
			tweets.append(statuses[idx].full_text)

#saving the tweets
csvfile = 'EvansTweets.csv'
with open(csvfile, "w", newline='') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["Evan's tweets"])
    for t in tweets:
    	try:
    		writer.writerow([t])
    	except UnicodeEncodeError:
    		print("nah")
