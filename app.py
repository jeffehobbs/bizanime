#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# bizanime.py // jeffehobbs@gmail.com
# shitpost low-wattage business nonsense and anime GIFs 

# Construct (timeframe) (noun) (verb) (scenario) ala:
# "WHEN THE CLIENT DMs ME ON SLACK"

# TODO:
# X. Create new Twitter account
# X. Get Twitter API keys
# X. Get GIPHY API key
# X. Set up script to randomly assemble sentence
# X. Randomly choose an anime GIF
# X. Download GIF to temporary storage￼
# X. Tweet out sentence coupled with GIF￼￼
# X. Move application to AWS￼

import requests
import json
import configparser
import random

from tweepy import OAuthHandler
from tweepy import API

# set up API keys from external config apikeys.txt file
config = configparser.ConfigParser()
config.read('apikeys.txt')
GIPHY_APIKEY = config.get('apikeys', 'giphy_apikey')
TWITTER_CONSUMER_KEY = config.get('twitter', 'consumer_key')
TWITTER_CONSUMER_SECRET = config.get('twitter', 'consumer_secret')
TWITTER_ACCESS_TOKEN = config.get('twitter', 'access_token')
TWITTER_ACCESS_TOKEN_SECRET = config.get('twitter', 'access_token_secret')


# main loop for AWS lambda
def lambda_handler():
	sentence = generate_sentence()
	print(sentence)
	gif_url = find_GIF("anime")
	download_GIF(gif_url)
	tweet_GIF(sentence)


# generate the sentence via fragments pulled from text files
def generate_sentence():
	#source files
	with open('timeframes.txt', 'r') as f:
		TIMEFRAMES = f.readlines()
	with open('nouns.txt', 'r') as f:
		NOUNS = f.readlines()
	with open('verbs.txt', 'r') as f:
		VERBS = f.readlines()
	with open('scenarios.txt', 'r') as f:
		SCENARIOS = f.readlines()
	timeframe = random.choice(TIMEFRAMES).replace('\n','')
	noun = random.choice(NOUNS).replace('\n','')
	verb = random.choice(VERBS).replace('\n','')
	scenario = random.choice(SCENARIOS).replace('\n','')
	return(timeframe + " " + noun + " " + verb + " " + scenario)


# find a random GIF via GIPHY API
def find_GIF(query):
	# EXAMPLE: https://api.giphy.com/v1/gifs/search?api_key=bLFbgaPdSjuNv3viqR8SAt0AFibC90xc&q=anime&limit=100&offset=0&rating=R&lang=en
	endpoint = "https://api.giphy.com/v1/gifs/search"
	limit = random.randint(1,25)
	offset = random.randint(0,5000)
	params = {"api_key": GIPHY_APIKEY, "q": query, "limit": limit, "offset": offset, "rating": "G", "lang": "en"}
	r = requests.get(endpoint, params=params)
	#print(r.url)
	data = r.json()
	#print(json.dumps(data, indent=4, sort_keys=True))
	gif_index = random.randint(1,limit) - 1
	return(data['data'][gif_index]['images']['original']['url'])


# download the GIF to /tmp directory
def download_GIF(url):
	r = requests.get(url)
	with open('/tmp/anime.gif', 'wb') as f:
		f.write(r.content)


# tweet the sentence and the GIF out to Twitter
def tweet_GIF(sentence):
	auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
	auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
	api = API(auth)
	api.update_with_media('/tmp/anime.gif',status=sentence)
	print('...DONE.')


# main function
if __name__ == '__main__':
	lambda_handler()

# fin