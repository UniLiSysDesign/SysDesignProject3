SysDesignProject3
=================
The given code collects tweets from twitter, calculates the sentiment score, writes the tweets into a MySQL database and evaluates the results.

All the files (except the file sentiment.py) can be executed directly in python. 

Note: Connection-strings for the MySQL database have to be adopted! 

<b>twitter_to_DB.py:</b><br>
This is the script which collects the tweets and stores them into the MySQL database. 
The keyword for which the according tweets are collected can be changed in line 25 (Default: audi)

<b>export_to_csv.py:</b><br>
This script contains a function exportDaysToCsv which takes a time span as parameters and exports the calculated sentiment scores to a .csv file.

<b>calc_correlation _coefficient.py:</b><br>
Calculates and shows the correlation coefficient of the different calculated sentiment scores.

<b>aggregate_scores.py:</b><br>
Calculates and shows mean sentiment scores for different time periods.

<b>sentiment.py:</b><br>
Contains the calculation of the different sentiment analysis.
