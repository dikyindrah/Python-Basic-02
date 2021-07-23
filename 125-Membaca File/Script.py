myfile = open('D:/Programming/web/Python/Python-Basic-02/125-Membaca File/myfile.txt', 'r')

# # Membaca seluruh data file
# print(myfile.read())

# # Membaca beberapa karakter pada file
# print(myfile.read(5))


# # Membaca data file baris demi baris
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())

# # Membaca data file dengan perulangan 
# for i in myfile:
#     print(i, end='')

# # Memeriksa file apakah bisa dibaca atau tidak
# print(myfile.readable())

# Menyimpan data file kedalam list
# Menyimpan seluruh baris data file kedalam list
# list_data = myfile.readlines()
# print(list_data)

# Mengubah posisi kursor
myfile.seek(50)

# Mengetahui posisi kursor
print(myfile.tell())

print('')
print(myfile.read())