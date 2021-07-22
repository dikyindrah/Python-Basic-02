myfile = open('D:/Programming/web/Python/Python-Basic-02/125-Membaca File/myfile.txt', 'r')

# # Membaca seluruh isi file
# print(myfile.read())

# # Membaca beberapa karakter pada file
# print(myfile.read(5))


# # Membaca isi file baris demi baris
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())

# # Membaca isi file dengan perulangan 
# for i in myfile:
#     print(i, end='')

# # Memeriksa file apakah bisa dibaca atau tidak
# print(myfile.readable())

# Menyimpan isi file kedalam list
# Menyimpan seluruh baris isi file kedalam list
list_seluruh_isi_file = myfile.readlines()
print(list_seluruh_isi_file)
