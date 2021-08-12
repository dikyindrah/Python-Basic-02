import os
from os import path
import sys

myfile_path = 'D:/Programming/web/Python/Python-Basic-02/132-Menghapus File/myfile.txt'

# Cara pertama
# os.remove(myfile_path)
# print('file berhasil dihapus')


# Cara kedua
try:
    if os.path.exists(myfile_path):
        os.remove(myfile_path)
        print('file berhasil di hapus')
    else:
        print('file tidak tersedia')
except:
    print(sys.exc_info()[0])
