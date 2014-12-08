# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 14:20:57 2014

@author: Reinhard
"""
import pyodbc
import pandas.io.sql as psql

conn = pyodbc.connect("DRIVER={MySQL ODBC 5.3 Unicode Driver}; SERVER=xxx.com; PORT=3306; \
DATABASE=group2; UID=xxx; PASSWORD=xxx;")


df_tweets = psql.read_sql('select ID, ScoreAlgorithm, DateTime from tweets WHERE Calculated = TRUE', con=conn)    
df_tweets = df_tweets.set_index(['ID'])

df_tweets["DAY"] = df_tweets["DateTime"].map(lambda x: x.date())
df_tweets["WEEK"] = df_tweets["DateTime"].map(lambda x: str(x.isocalendar()[1]) + "/" + str(x.isocalendar()[0]))
df_tweets["YEAR"] = df_tweets["DateTime"].map(lambda x: x.date().year)

print "########################################################################"
print "Mean score total: "
print df_tweets["ScoreAlgorithm"].mean()
print ""
print "Mean score per day: "
print df_tweets.groupby(df_tweets["DAY"]).mean()["ScoreAlgorithm"]
print ""
print "Mean score per week: "
print df_tweets.groupby(df_tweets["WEEK"]).mean()["ScoreAlgorithm"]
print ""
print "Mean score per year: "
print df_tweets.groupby(df_tweets["YEAR"]).mean()["ScoreAlgorithm"]
print ""
print "########################################################################"


conn.close()