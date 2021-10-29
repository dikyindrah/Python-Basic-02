import mysql.connector 
from mysql.connector import Error

# # Mengubah sekema tabel
# try:
#     with mysql.connector.connect(
#         host = 'localhost',
#         database = 'db_online_movie_rating',
#         username = 'root',
#         password = ''
#     ) as db_online_movie_rating:
#         # Mendefinisikan query untuk mengubah skema tabel
#         alter_tbl_movies_query = """
#             ALTER TABLE tbl_movies MODIFY COLUMN collection_in_mil DECIMAL(4,1)
#         """

#         # Mendefinisikan query untuk menampilkan tbl_movies
#         show_tbl_movies_query = """
#             DESCRIBE tbl_movies
#         """
        
#         if db_online_movie_rating.is_connected():
#             print('Koneksi berhasil')
#             with db_online_movie_rating.cursor() as cursor:
#                 cursor.execute(alter_tbl_movies_query)
#                 cursor.execute(show_tbl_movies_query)
#                 result = cursor.fetchall()
#                 print('Skema tabel berhasil diubah')
#                 print('\ntbl_movies')
#                 for row in result:
#                     print(row)
# except Error as e:
#     print(f"Koneksi gagal, Error: {e}")

# # Menghapus tabel
try:
    with mysql.connector.connect(
        host = 'localhost',
        database = 'db_online_movie_rating',
        username = 'root',
        password = ''
    ) as db_online_movie_rating:
        # Mendefinisikan query untuk menghapus tabel
        drop_tbl_ratings_query = """
            ALTER TABLE tbl_movies MODIFY COLUMN collection_in_mil DECIMAL(4,1)
        """

        if db_online_movie_rating.is_connected():
            print('Koneksi berhasil')
            with db_online_movie_rating.cursor() as cursor:
                cursor.execute(drop_tbl_ratings_query)
                print('Tabel berhasil dihapus')
except Error as e:
    print(f"Koneksi gagal, Error: {e}")