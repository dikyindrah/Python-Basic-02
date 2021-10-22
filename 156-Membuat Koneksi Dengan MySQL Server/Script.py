import mysql.connector
from mysql.connector import Error

try:
    with mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = ''
    ) as mysql_server:
        if mysql_server.is_connected():
            print('Koneksi berhasil')
except Error as e:
    print(f"Koneksi gagal, Eror: {e}")
