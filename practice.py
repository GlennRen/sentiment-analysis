from textblob import TextBlob
import tweepy

def userSentiment (username):
	sentiments = []
	tweets = api.user_timeline(username, count="15")
	for i in tweets:
		sentiments.append(TextBlob(i.text).sentiment.polarity)
	return (sum(sentiments))

auth = tweepy.OAuthHandler("5mjmNCtr7nHyYMh1zRfoF09uz","hVWcuAp6Tb2J5XqhTcAbE0f7jA0F6O26nWqaPX68UjbMQrud6q")
auth.set_access_token("368675631-zCLQoo8dNzFFqdvfjt4pGz9nXhKDc4rwMtm0Wnfy", "oXL9QyRUYUkY2BP1DTpeVxd0B4vAkf4w2Cjrf1eikKUP2")

api = tweepy.API(auth)

following = []

print (userSentiment("glennren"))

# for user in tweepy.Cursor(api.followers, screen_name="glennren").items():
# 	following.append(user.screen_name)