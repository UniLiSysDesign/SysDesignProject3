# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 19:10:05 2014

@author: Reinhard
"""

import pyodbc
import pandas.io.sql as psql
from scipy.stats.stats import pearsonr

conn = pyodbc.connect("DRIVER={MySQL ODBC 5.3 Unicode Driver}; SERVER=xxx.com; PORT=3306; \
DATABASE=group2; UID=xxx; PASSWORD=xxx;")

df_tweets = psql.read_sql('select ScoreAlgorithm, ScoreControl from tweets WHERE Calculated = TRUE', con=conn)    

print 'correlation coefficient: ', pearsonr(df_tweets['ScoreAlgorithm'], df_tweets['ScoreControl'])[0]

conn.close()