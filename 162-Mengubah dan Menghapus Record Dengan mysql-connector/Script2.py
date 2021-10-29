import mysql.connector 
from mysql.connector import Error

select_record_query = '''
    SELECT * FROM tbl_reviewers
'''

update_record_query = '''
    UPDATE tbl_reviewers SET first_name=%s, last_name=%s WHERE reviewer_id=%s
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
                cursor.execute(select_record_query)
                result = cursor.fetchall()
                print('tbl_reviewers\n')
                for row in result:
                    print(row)
                
                print('\nUpdate record from tbl_reviewers\n')
                reviewer_id = str(input('Select reviewer_id: '))
                new_first_name = str(input('new first_name: '))
                new_last_name = str(input('new last_name: '))
                val_record = (new_first_name, new_last_name, reviewer_id)
                cursor.execute(update_record_query, val_record, multi=True)
                db_online_movie_rating.commit()
                
                print('\ntbl_reviewers\n')
                cursor.execute(select_record_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)

except Error as e:
    print(f"Koneksi gagal, Error: {e}")