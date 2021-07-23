# Mode 'w'
# myfile = open('D:/Programming/web/Python/Python-Basic-02/126-Menulis File/myfile.txt', 'w')

# # write()
# myfile.write('ini adalah hari yang cerah')

# # writelines()
# list_string = ['ini ', 'adalah ', 'hari ', 'yang ', 'cerah ']
# myfile.writelines(list_string)

# # writeable()
# print(myfile.writable())


# Mode 'a'
# myfile = open('D:/Programming/web/Python/Python-Basic-02/126-Menulis File/myfile.txt', 'a')

# # write()
# myfile.write('ini adalah hari yang cerah\n')
# myfile.write('saatnya aku pergi ke sekolah\n')

# # writelines()
# list_string = ['ini ', 'adalah ', 'hari ', 'yang ', 'cerah \n']
# # myfile.writelines(list_string)
# myfile.writelines(list_string)

# # writeable()
# print(myfile.writable())


# Mode 'x'
# myfile = open('D:/Programming/web/Python/Python-Basic-02/126-Menulis File/myfile2.txt', 'x')

# # write()
# myfile.write('ini adalah hari yang cerah')

# # writelines()
# list_string = ['ini ', 'adalah ', 'hari ', 'yang ', 'cerah \n']
# myfile.writelines(list_string)

# # writeable()
# print(myfile.writable())


# Mode '+'
myfile = open('D:/Programming/web/Python/Python-Basic-02/126-Menulis File/myfile.txt', 'w+')

# Memeriksa apakah data bisa ditulis
print(myfile.writable()) 

# Memeriksa apakah data bisa dibaca
print(myfile.readable())
