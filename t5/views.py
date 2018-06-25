from django.shortcuts import render
import tweepy
from tweepy import OAuthHandler

def weather(request):
	return render(request, 't5/weather.html')

def twitter(request):
	consumer_key = "uJyWhkflmQZGmB3loD3s0TIHT"
	consumer_secret ="7nBdbmwg7gNqzVYrrShwewSenfT1eFXvxv5STZ0HOX3vL8pcJn"
	access_token = "19166515-phNfJrQTJZEAktX4GbDKT8eTy4HrBDCAW8KZCqMgY"
	access_token_secret = "yE79IYKhiu2IX2lbHI14dfRcqELKUCvHJe5BM7WBeZMiH"
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	all_public_tweets = api.user_timeline("weatherchannel")
	severe_public_tweets = [k for k in all_public_tweets if "severe" in k.text.lower()]

	return render(request, 't5/twitter.html', {'public_tweets': severe_public_tweets})

def index(request): 
	return render(request, "t5/index.html")
