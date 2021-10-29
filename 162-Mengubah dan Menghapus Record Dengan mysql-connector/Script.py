import mysql.connector
from mysql.connector import Error

update_record_query = '''
    UPDATE tbl_reviewers SET last_name='Cena' WHERE first_name='John'
'''

select_record_query = '''
    SELECT * FROM tbl_reviewers WHERE first_name='John' 
'''

try:
    with mysql.connector.connect(
        host = 'localhost',
        database = 'db_online_movie_rating',
        username = 'root',
        password = ''
    ) as db_online_movie_rating:
        if db_online_movie_rating.is_connected():
            print('Koneksi berhasil\n')
            with db_online_movie_rating.cursor() as cursor:
                cursor.execute(update_record_query)
                print('Record berhasil diubah')
                cursor.execute(select_record_query)
                result = cursor.fetchall()
                print(result)
                db_online_movie_rating.commit()
except Error as e:
    print(f"Koneksi gagal, Error: {e}")