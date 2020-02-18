# DataEngineering
MyAssignment

Sparkify is a music streaming app which has been collecting songs and user activity data.
They want to analyze the user's song listining activity. But in order to analyze it, they want it to only the relevant data for song analysis to be extracted. 
For this we need to create a database schema and break it down to different dimension tables and finally building ETL
pipeline to extract data from the two song and log files to our analytical database for better analysis.



1.Objective of this project is to create a star schema with following fact and dimesnion tables:
 Fact Table: Songplay
 Dimension Table: songs,artists,time,users
 
2.sql_queries.py
This file contains queries to create all the fact and dimension tables.
The script makes sure to drop the table if already exists and then create the tables.

3.create_tables.py
We start by creating database SParkify and then creating all the tables by importing queries from sq_queries.py.

4.etl.py
This helps in extarcting filepath from song and log data.
song_data: Using the filepath from song data we extract 5 song data and artist data columns from these files.
log_data: Using the filepath from log data we extract time and user data.

song_play_analysis: select song_play data from song an artist where song_id ,duration and artist_id is equal to the log data.

Order of executing the py files:
1.Run Create_tables.py to create database tables and song select and song play analysis table.
2.Then run etl.py to read the song and log files and process them to insert data in song play analysis table.
