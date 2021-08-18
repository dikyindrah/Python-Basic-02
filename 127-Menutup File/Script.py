# # Menutup file dengan cara manual
# myfile = open('D:/Programming/web/Python/Python-Basic-02/127-Menutup File/myfile.txt', 'r')
# print(myfile.read())
# myfile.close()
# print('file berhasil ditutup...')

# # Menutup file dengan penanganan pengecualian 
# # (exception handling)
# import sys

# try:
#     myfile = open('D:/Programming/web/Python/Python-Basic-02/127-Menutup File/myfile.txt', 'r')
#     print(myfile.read())
# except:
#     print(sys.exc_info()[0])
# finally:
#     try:
#         myfile.close()
#         print('file berhasil ditutup...')
#     except:
#         print(sys.exc_info()[0])

# Menutup file dengan keyword with
with open('D:/Programming/web/Python/Python-Basic-02/127-Menutup File/myfile.txt', 'a') as f:
    f.write('hello world\n')
    print('file berhasil ditulis.')