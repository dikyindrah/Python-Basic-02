import mysql.connector 
from mysql.connector import Error

# # Mengisi data pada tbl_movies
# insert_tbl_movies_query = '''
#     INSERT INTO tbl_movies (title, release_year, genre, collection_in_mil)
#     VALUES 
#     ("Forrest Gump", 1994, "Drama", 330.2), 
#     ("3 Idiots", 2009, "Drama", 2.4),
#     ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5)
# '''

# try:
#     with mysql.connector.connect(
#         host = 'localhost',
#         database = 'db_online_movie_rating',
#         username = 'root',
#         password = ''
#     ) as db_online_movie_rating:
#         if db_online_movie_rating.is_connected():
#             print('Koneksi berhasil')
#             with db_online_movie_rating.cursor() as cursor:
#                 cursor.execute(insert_tbl_movies_query)
#                 db_online_movie_rating.commit()
#                 print('Data berhasil ditambahkan')
# except Error as e:
#     print(f"Koneksi gagal, Error: {e}")
#     print('Data tidak berhasil ditambahkan')

# # Mengisi data pada tbl_reviewers
# insert_tbl_reviewers_query = '''
#     INSERT INTO tbl_reviewers (first_name, last_name)
#     VALUE (%s, %s)
# '''

# reviewers_record = [
#     ("Chaitanya", "Baweja"),
#     ("Mary", "Cooper"),
#     ("John", "Wayne"),
#     ("Thomas", "Stoneman"),
#     ("Penny", "Hofstadter"),
#     ("Mitchell", "Marsh"),
#     ("Wyatt", "Skaggs"),
#     ("Andre", "Veiga"),
#     ("Sheldon", "Cooper"),
#     ("Kimbra", "Masters"),
#     ("Kat", "Dennings"),
#     ("Bruce", "Wayne"),
#     ("Domingo", "Cortes")    
# ]

# try:
#     with mysql.connector.connect(
#         host = 'localhost',
#         database = 'db_online_movie_rating',
#         username = 'root',
#         password = ''
#     ) as db_online_movie_rating:
#         if db_online_movie_rating.is_connected():
#             print('Koneksi berhasil')
#             with db_online_movie_rating.cursor() as cursor:
#                 cursor.executemany(insert_tbl_reviewers_query, reviewers_record)
#                 db_online_movie_rating.commit()
#                 print('Data berhasil ditambahkan')
# except Error as e:
#     print(f"Koneksi gagal, Error: {e}")
#     print('Data tidak berhasil ditambahkan')

# # Mengisi data pada tbl_ratings
insert_tbl_ratings_query = '''
    INSERT INTO tbl_ratings (rating, movie_id, reviewer_id)
    VALUE (%s, %s, %s)
'''

ratings_record = [
    (6.4, 1, 5), (5.6, 2, 4), (6.3, 3, 3), (5.1, 1, 2),
    (5.0, 1, 1), (6.5, 2, 6), (8.5, 3, 7), (9.7, 2, 8),
    (8.5, 1, 9), (9.9, 3, 10), (8.7, 1, 11), (9.9, 2, 12),
    (5.1, 3, 13)
]

try:
    with mysql.connector.connect(
        host = 'localhost',
        database = 'db_online_movie_rating',
        username = 'root',
        password = ''
    ) as db_online_movie_rating:
        if db_online_movie_rating.is_connected():
            print('Koneksi berhasil')
            with db_online_movie_rating.cursor() as cursor:
                cursor.executemany(insert_tbl_ratings_query, ratings_record)
                db_online_movie_rating.commit()
                print('Data berhasil ditambahkan')
except Error as e:
    print(f"Koneksi gagal, Error: {e}")
    print('Data tidak berhasil ditambahkan')