import mysql.connector 
from mysql.connector import Error

select_tbl_movies_query = '''
    SELECT * FROM tbl_movies
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
                cursor.execute(select_tbl_movies_query)
                result = cursor.fetchall()
                # for row in result:
                #     print(row)
                for i in range(len(result)):
                    for j in range(len(result[i])):
                        print(result[i][j], end=' ')
                    print('')

except Error as e:
    print(f"Koneksi gagal, Error: {e}")