import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '',
    database = 'dbtest'
)

if mydb.is_connected():
    print('berhasil terhubung ke database')