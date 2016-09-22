#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from TwitterSearch import *

argfile = str(sys.argv[1])

CONSUMER_KEY = 'VX4rE3pnhuXxgHR0xJHmX8Dyn'
CONSUMER_SECRET = '8RKXuTh6iqt23EwXjQ3wiaESmxyMthBdCydDcnLVDdbMu8pn0v'
ACCESS_KEY = '779026531184095232-2Eqnm83uuhY3sN3G2689j69esq5jJDb'
ACCESS_SECRET = 'uvN5IDCBf4PweiddUq8G7E8hnGeGalzEjmwfXuonK46xE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for game in f:
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords([game])
        tso.set_language('en')
        tso.set_include_entities(False)

        ts = TwitterSearch(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

        pos=0
        neg=0
        for tweet in ts.search_tweets_iterable(tso):
            lowtweet = tweet['text'].lower
            if 'good' or 'great' or 'amazing' or 'fantastic' or 'excellent' or 'best' in lowtween:
                pos += 1
            if 'bad' or 'awful' or 'terrible' or 'worst' in lowtween:
                neg += 1

        if (pos + neg) == 0:
            mytweet = 'Nobody has tweeted an opinion about ' + game
        else:
            score = (pos - neg) / (pos + neg) 

            if score == 0:
                rating = 'neither loved or hated'
            elif score < 0 and score >= -1/3:
                rating = 'did not like'
            elif score < -1/3:
                rating = 'hated'
            elif score <= 1/3:
                rating = 'liked'
            else:
                rating = 'loved'

            mytweet= 'Gamers ' + rating + ' ' + game + str(pos) + ' players enjoyed the game, while ' + str(neg) + ' did not'

        api.update_status(mytweet)
        sleep(86400)

    except TwitterSearchException as e:
        print(e)


