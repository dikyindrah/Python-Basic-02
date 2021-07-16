import sys

text = 'Hello World!'

try:
    print(text)
except:
    print(sys.exc_info()[0])
else:
    print('tidak ada kesalahan yang terjadi.')