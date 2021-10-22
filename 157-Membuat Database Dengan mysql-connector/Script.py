import mysql.connector
from mysql.connector import Error

try:
    with mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = ''
    ) as koneksi:
        create_db_query = 'CREATE DATABASE db_online_movie_rating'
        show_db_query = 'SHOW DATABASES'
        with koneksi.cursor() as cursor:
            cursor.execute(create_db_query)
            print('Database berhasil dibuat\n')
            print('Daftar database:\n')
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
except Error as e:
    print(f"Database gagal dibuat, Error: {e}")
