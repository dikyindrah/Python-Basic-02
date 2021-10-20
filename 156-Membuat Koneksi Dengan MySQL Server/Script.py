import mysql.connector
from mysql.connector import Error

try:
    with mysql.connector.connect(
        host = 'localhost',
        database = 'db_profesi',
        username = 'root',
        password = ''
    ) as mydatabase:
        if mydatabase.is_connected():
            print('Koneksi berhasil')
except Error as e:
    print(f"Koneksi gagal, Eror: {e}")
