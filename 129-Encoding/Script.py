import sys

try:
    myfile = open('D:/Programming/web/Python/Python-Basic-02/129-Encoding/myfile.txt', 'a', 1, 'utf-8')
    myfile.write('File berhasil ditulis\n')
except:
    print(sys.exc_info()[0])
finally:
    myfile.close()

# Memeriksa format encoding
print(myfile.encoding)