#!usr/bin/env python3.7
import tweepy
import time
from sensor_test import getInput

from tweepy.auth import OAuthHandler

API_KEY='KZ6deQGfupfWNG1Ab8NcNBz9V'
API_SECRET='1gH4yPTIS5RqzQ1Jx9KIcXQ5lupSXNZyTrpDHVyV2nrStiSYz6'
ACCESS_TOKEN='973718052561879041-zDzyVVhgUoGk6kSx67G1okYT1aFGzzW'
ACCESS_TOKEN_SECRET='2L7MGvPx5ztz4AFcY80pj8MD8btCs8u6qogxnbo1LFyBC'

while 1:
	x=getInput()
	temp=float(x[1])
	location="55 St George St, Toronto= St.George"

	auth=tweepy.OAuthHandler(API_KEY,API_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
	api=tweepy.API(auth)

	if(temp>33.0):
		api.update_status(" High Temperature Alert!! Temperature: "+str(round(temp,1))+" degrees Celsius \nLocation: 55 St George St, Toronto\n" + "#torontopolice "+"#firestation "+"#breakingnews "+"#nourishnew ")
		print("Sent!")
	time.sleep(5)
