import mysql.connector 
from mysql.connector import Error

try:
    with mysql.connector.connect(
        host = 'localhost',
        database = 'db_online_movie_rating',
        username = 'root',
        password = ''
    ) as db_online_movie_rating:
        # Mendefinisikan query untuk membuat tbl_movies.
        create_tbl_movies = """
        CREATE TABLE tbl_movies (
            movie_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR (100),
            collection_in_mil INT
        )
        """

        # Mendefinisikan query untuk membuat tbl_reviewers.
        create_tbl_reviewers = """
        CREATE TABLE tbl_reviewers (
            reviewer_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
            )
        """

        # Mendefinisikan query untuk membuat tbl_ratings 
        create_tbl_ratings = """
        CREATE TABLE tbl_ratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES tbl_movies(movie_id),
            FOREIGN KEY(reviewer_id) REFERENCES tbl_reviewers(reviewer_id)
        )
        """

        # Mendefinisikan query untuk menampilkan struktur tabel
        show_tbl_movies = 'DESCRIBE tbl_movies'
        show_tbl_reviewers = 'DESCRIBE tbl_reviewers'
        show_tbl_ratings = 'DESCRIBE tbl_ratings'

        if db_online_movie_rating.is_connected():
            print('Koneksi berhasil')

            # Mengeksekusi query yang telah dibuat
            with db_online_movie_rating.cursor() as cursor:
                cursor.execute(create_tbl_movies)
                cursor.execute(create_tbl_reviewers)
                cursor.execute(create_tbl_ratings)
                db_online_movie_rating.commit()
        
        # Menampilkan tabel yang berhasil dibuat
        print('Tabel berhasil dibuat\n')
        with db_online_movie_rating.cursor() as cursor:
            print('tbl_movies:')
            cursor.execute(show_tbl_movies)
            tbl_movies = cursor.fetchall()
            for row in tbl_movies:
                print(row)
            
            print('\ntbl_reviewers:')
            cursor.execute(show_tbl_reviewers)
            tbl_reviewers = cursor.fetchall()
            for row in tbl_reviewers:
                print(row)

            print('\ntbl_ratings:')
            cursor.execute(show_tbl_ratings)
            tbl_ratings = cursor.fetchall()
            for row in tbl_ratings:
                print(row)
except Error as e:
    print(f"Koneksi gagal, Error: {e}")
    print('Gagal membuat tabel')