# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (
    "CREATE TABLE IF NOT EXISTS songplays (\
        songplay_id SERIAL PRIMARY KEY, \
        start_time BIGINT NOT NULL,\
        user_id INTEGER, \
        level VARCHAR(10), \
        song_id VARCHAR(30),\
        artist_id VARCHAR(30),\
        session_id INTEGER,\
        location VARCHAR(200)\
     )\
    "
)

# songplay_table_create FK CONSTRAINTS
# CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES users(user_id),\
# CONSTRAINT fk_song_id FOREIGN KEY(song_id) REFERENCES songs(song_id),\
# CONSTRAINT fk_artist_id FOREIGN KEY(artist_id) REFERENCES artists(artist_id),\
# CONSTRAINT fk_time_id FOREIGN KEY(start_time) REFERENCES time(start_time)\

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
    "CREATE TABLE IF NOT EXISTS songs (\
       song_id VARCHAR(30) PRIMARY KEY, \
        title VARCHAR(200), \
        artist_id  VARCHAR(30), \
        year INTEGER, \
        duration NUMERIC\
     )"
)

artist_table_create = (
    "CREATE TABLE IF NOT EXISTS artists (\
        artist_id VARCHAR(50) PRIMARY KEY, \
        name VARCHAR (300),\
        location VARCHAR(300),\
        latitude VARCHAR(300),\
        longitude VARCHAR(300)\
    )"
)

time_table_create = (
    "CREATE TABLE IF NOT EXISTS time(\
        start_time BIGINT PRIMARY KEY,\
        hour INTEGER,\
        day INTEGER,\
        week INTEGER,\
        month INTEGER,\
        year INTEGER,\
        weekday INTEGER\
    )"
)

# INSERT RECORDS

songplay_table_insert = (
    "INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location) \
    VALUES (%s, %s, %s, %s, %s, %s, %s) \
    ON CONFLICT DO NOTHING"
)

user_table_insert = (
    "INSERT INTO users (user_id, first_name, last_name, gender, level) \
        VALUES (%s, %s, %s, %s, %s)\
        ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level"
)

song_table_insert = (
    "INSERT INTO songs (song_id, title, artist_id, year, duration) \
        VALUES (%s, %s, %s, %s, %s)\
            ON CONFLICT DO NOTHING"
)

artist_table_insert = (
    "INSERT INTO artists (artist_id, name, location, latitude, longitude) \
        VALUES (%s, %s, %s, %s, %s)\
        ON CONFLICT DO NOTHING"
)


time_table_insert = (
    "INSERT INTO time (start_time, hour, day, week, month, year, weekday)\
        VALUES (%s, %s, %s, %s, %s, %s, %s)\
        ON CONFLICT DO NOTHING"
)

# FIND SONGS

song_select = (
    "SELECT * FROM songs s JOIN artists a USING (artist_id) WHERE s.title = %s AND a.name = %s AND s.duration = %s"
)

# QUERY LISTS

create_table_queries = [user_table_create,
                        artist_table_create, time_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
