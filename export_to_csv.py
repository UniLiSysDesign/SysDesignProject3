# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 17:53:13 2014

@author: Raphael
"""
# Pyodbc Import
import pyodbc
import pandas as pd

#DB Export Funktion (YYYY-MM-DD, YYYY-MM-DD)
def exportDaysToCsv(start_date, end_date):
    df_out = pd.DataFrame(columns=['PK', 'ID', 'SCORE_ALGORITHM', 'SCORE_CONTROL', 'DATETIME'])
    
    # DB Connection
    conn = pyodbc.connect("DRIVER={MySQL ODBC 5.3 Unicode Driver}; SERVER=xxx.com; PORT=3306; \
    DATABASE=group2; UID=xxx; PASSWORD=xxx;")
    
    # Cursor wird erstellt
    cursor = conn.cursor()
    
    # Cursor wird ausgeführt
    cursor.execute("SELECT * FROM `TWEETS` WHERE DATETIME >= \""+ start_date +"\"and DATETIME <= \""+ end_date + " 23:59:59\"")
  
    # Cursor Fetch 
    rows = cursor.fetchall()
    
    # Print Command
    for row in rows:
        df_out.loc[len(df_out)+1] = [row[0], row[1], row[3], row[4], row[6]]
                                
    df_out = df_out.set_index(['PK'])
    
    # Schließen des Cursors
    cursor.close()
    
    print df_out
    df_out.to_csv("./sentiment_analysis.csv")

exportDaysToCsv("2014-02-02", "2014-12-09")