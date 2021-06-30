# Mencetak \n tanpa raw string
print('hello \nworld')

# Mencetak \n dengan raw string
print(r'hello \nworld')
print(R'hello \nworld')

import re

teks = 'ini \n adalah \t 10'
hasil = re.findall(r'[\n\t]', teks)
print(hasil)