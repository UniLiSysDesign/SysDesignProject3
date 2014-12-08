# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 19:17:58 2014

@author: kevin_000
"""

import json
import pyodbc
import sentiment as s
from TwitterAPI import TwitterAPI

conn = pyodbc.connect("DRIVER={MySQL ODBC 5.3 Unicode Driver}; SERVER=xxx.com; PORT=3306; \
DATABASE=group2; UID=xxx; PASSWORD=xxx;")

cursor = conn.cursor()

consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token_key = 'xxx'
access_token_secret = 'xxx'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('statuses/filter', {'track': 'audi'})
for item in r:
    if item["lang"] == "en":
        try:
            print "English - saved"
            ID = item["id"]
            ID = str(ID)
            tweet = item["text"]
            tweet = str(tweet)
            timestamp = item["created_at"]
            timestamp = str(timestamp)
            print "   "+str(ID)

            scores = s.calc_sentiment_sentence(tweet)

            insert_state = "INSERT INTO tweets (ID, Tweet, Timestamp, ScoreAlgorithm, ScoreControl, Calculated) VALUES ('"+ID+"', '"+tweet+"', '"+timestamp+"', " + str(scores[0]) +" , " + str(scores[1]) + ", TRUE)"
            cursor.execute(insert_state)
            cursor.commit()
        except:
            pass

    else:
        print "Tweet not English"
        
cursor.close()

    