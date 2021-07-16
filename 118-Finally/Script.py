import sys

try:
    print('file dibuka.')
    f = open(r'..\file.txt', 'w+')
    f.write('Hello World!')
except:
    print(sys.exc_info()[0])
finally:
    f.close()
    print('file ditutup.')