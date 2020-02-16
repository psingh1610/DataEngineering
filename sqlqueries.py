# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
(songplay_id serial PRIMARY KEY, start_time bigint, user_id int, level varchar(15), song_id int, artist_id int, session_id int, location varchar(50), user_agent varchar(500))
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
user_id int, first_name varchar(20), last_name varchar(20), gender varchar(10), level varchar(10))
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
song_id varchar(255), title varchar(255), artist_id varchar(255), year int, duration float)
""")

artist_table_create = ("""CREATE TABLE  IF NOT EXISTS artists (
artist_id varchar(255), name varchar(255), location varchar(255), latitude float, longitude float)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
start_time bigint, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays(start_time,user_id,level,song_id, artist_id, session_id,location,user_agent)
values(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""insert into users(user_id,first_name,last_name,gender,level)
values(%s,%s,%s,%s,%s)
""")

song_table_insert = ("""insert into songs(song_id,title,artist_id,duration,year)
values(%s,%s,%s,%s,%s)
""")

artist_table_insert = ("""insert into artists(artist_id,name,location,latitude,longitude)
values(%s,%s,%s,%s,%s)
""")


time_table_insert = ("""insert into time(start_time,hour,day,week,month,year,weekday)
values(%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS

song_select = ("""select songs.song_id,artists.artist_id from songs join artists on songs.artist_id=artists.artist_id 
where songs.title=%s and artists.name=%s and songs.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
