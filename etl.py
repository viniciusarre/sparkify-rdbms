import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
        Process a given songfile from a specific pathname, filter and handle the data from the processed file into the appropriate tables. This includes inserting data into the songs and artists tables. 

        Parameters:
            cur: the database cursor which will be used for inserting the data.
            
            filepath: the filepath where the songfile should be extracted from. 

    """
    # open song file
    df = pd.read_json(filepath, orient='index', typ='series')

    # insert song record
    selected_columns = ['song_id', 'title', 'artist_id', 'year', 'duration']
    song_data = df[selected_columns]
    cur.execute(song_table_insert, song_data)

    # insert artist record
    selected_columns = ['artist_id', 'artist_name',
                        'artist_location', 'artist_latitude', 'artist_longitude']
    ideal_indexes = ['artist_id', 'name', 'location', 'latitude', 'longitude']
    artist_data = df[selected_columns]

    artist_data = pd.Series(data=artist_data.values)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
        Process a given log_file from a specific pathname, filter it by NextSong and then filter and handle the data from the processed log_file into the tables. This includes inserting data into time, user and songplay tables. 

        Parameters:
            cur: the database cursor which will be used for inserting the data.
            
            filepath: the filepath where the logfile should be extracted from. 

    """

    # open log file
    df = pd.read_json(filepath, orient='records', lines=True)

    # filter by NextSong action
    df = df[df.page == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'].values, unit='ms')

    # insert time data records
    series = pd.Series(t)
    time_data = {
        'start_time': df['ts'].values,
        'hour': list(series.dt.hour.values),
        'day': list(series.dt.day.values),
        'week': list(series.dt.week),
        'month': list(series.dt.month),
        'year': list(series.dt.year),
        'weekday': list(series.dt.weekday),
    }
    column_labels = ['start_time', 'hour', 'day',
                     'week', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(data=time_data, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName',
                  'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results[0], results[2]
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid,
                         artistid, row.sessionId, row.location)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
        Get all files matching extension from directory then call the callback function for handling and setting the data. 
        Once that is done, the connection commits all the data that was inserted. 
            Parameters:
                cur: The current database cursor
                conn: the current connection object
                filepath: the filepath where the files must be fetched from
                func: The callback function which will be called once the extraction is complete
    '''
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''
        Main function, which handles all the ETL process during the execution. 
        First the song_data goes through the pipeline and then the log_file data
    '''
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
