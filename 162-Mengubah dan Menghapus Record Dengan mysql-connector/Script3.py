import mysql.connector 
from mysql.connector import Error

select_query = '''
    SELECT * FROM tbl_ratings
'''

delete_query = '''
    DELETE FROM tbl_ratings WHERE movie_id=%s AND reviewer_id=%s
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
                cursor.execute(select_query)
                result = cursor.fetchall()
                print('tbl_reviewers:\n')
                print('movie_id, reviewer_id, rating')
                for row in result:
                    print(row)

                print('\nDelete record')
                movie_id = str(input('delete movie_id: '))
                reviewer_id = str(input('delete reviewer_id: '))
                val_record = (movie_id, reviewer_id)
                cursor.execute(delete_query, val_record, multi=True)
                db_online_movie_rating.commit()
               
                cursor.execute(select_query)
                result = cursor.fetchall()
                print('\ntbl_reviewers:\n')
                print('movie_id, reviewer_id, rating')
                for row in result:
                    print(row)
except Error as e:
    print(f"Koneksi gagal, Error: {e}")