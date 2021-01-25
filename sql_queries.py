# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (
    "CREATE TABLE IF NOT EXISTS songplay (\
        songplay_id INTEGER PRIMARY KEY, \
        start_time TIME, \
        user_id INTEGER, \
        level VARCHAR(10), \
        song_id INTEGER,\
        artist_id INTEGER,\
        session_id INTEGER,\
        location VARCHAR(200),\
        CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES users(user_id),\
        CONSTRAINT fk_song_id FOREIGN KEY(song_id) REFERENCES song(song_id),\
        CONSTRAINT fk_artist_id FOREIGN KEY(artist_id) REFERENCES artist(artist_id)\
        )\
    "
)

user_table_create = (
    "CREATE TABLE IF NOT EXISTS users (\
        user_id INTEGER PRIMARY KEY, \
        first_name VARCHAR(100), \
        last_name VARCHAR(100),\
        gender VARCHAR(1), \
        level VARCHAR(10)\
        )\
    ")

song_table_create = (
    "CREATE TABLE IF NOT EXISTS song (\
        song_id INTEGER PRIMARY KEY, \
        title VARCHAR(200), \
        artist_id INTEGER, \
        year INTEGER, \
        duration NUMERIC (10, 2),\
        CONSTRAINT fk_artist_id FOREIGN KEY(artist_id) REFERENCES artist(artist_id)\
    )"
)

artist_table_create = (
    "CREATE TABLE IF NOT EXISTS artist (\
        artist_id INTEGER PRIMARY KEY, \
        name VARCHAR (200),\
        location VARCHAR(100),\
        latitude VARCHAR(200),\
        longitude VARCHAR(200)\
    )"
)

time_table_create = (
    "CREATE TABLE IF NOT EXISTS time(\
        start_time TIME,\
        hour INTEGER,\
        day INTEGER,\
        week INTEGER,\
        month INTEGER,\
        year INTEGER,\
        weekday VARCHAR(20)\
    )"
)

# INSERT RECORDS

songplay_table_insert = (
    "INSERT INTO songplay (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location) \
    values (%s, %s, %s, %s, %s, %s)    "
)

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

create_table_queries = [user_table_create,
                        artist_table_create, time_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
