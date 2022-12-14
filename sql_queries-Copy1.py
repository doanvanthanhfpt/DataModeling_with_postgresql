# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
#user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

# Fact table
# songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay (
  songplay_id INT PRIMARY KEY,
  start_time TIMESTAMP,
  user_id INT,
  level INT,
  song_id INT,
  artist_id INT,
  session_id INT,
  location VARCHAR(50),
  user_agent VARCHAR(50)
  );
""")

# Dimension Tables

# user_id, first_name, last_name, gender, level
user_table_create = ("""
CREATE TABLE IF NOT EXISTS user (
  user_id INT PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR,
  gender VARCHAR,
  level INT
  );
""")

# song_id, title, artist_id, year, duration
song_table_create = ("""
CREATE TABLE IF NOT EXISTS song (
  song_id INT PRIMARY KEY,
  title VARCHAR,
  artist_id INT,
  year INT,
  duration INT
  );
""")

# artist_id, name, location, latitude, longitude
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist (
  artist_id INT PRIMARY KEY,
  name VARCHAR,
  location VARCHAR,
  latitude INT,
  longitude INT
  );
""")

# start_time, hour, day, week, month, year, weekday
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
  start_time TIMESTAMP PRIMARY KEY,
  hour VARCHAR,
  day VARCHAR,
  week INT,
  month INT,
  year INT,
  weekday INT
  );
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]