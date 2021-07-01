import re
from sys import hash_info

teks = 'hari ini adalah hari ulang tahunku ke 21'

# [] Kurung siku
hasil = re.findall('[a-d]', teks)
print(hasil)

hasil = re.findall('[1-2]', teks)
print(hasil)

# . Tanda titik
hasil = re.findall('har..', teks)
print(hasil)

# ^ Tanda caret
hasil = re.search('^hari', teks)
print(hasil)

hasil = re.search('^ini', teks)
print(hasil)

# $ Tanda dolar
hasil = re.search('21$', teks)
print(hasil)

hasil = re.search('tahun$', teks)
print(hasil)

# * Tanda bintang 
hasil = re.findall('hari*', teks)
print(hasil)

# + Tanda tambah
hasil = re.findall('hari ulang..+', teks)
print(hasil)

hasil = re.search('\d+', teks)
print(hasil.group())

# {} Tanda kurung kurawal
# teks = '123456789'
# hasil = re.search('\d{9}', teks)
# print(hasil.group())

# | Tanda vertical bar
hasil = re.findall('a|b', teks)
print(hasil)

# () Tanda kurung
# teks = 'pukul 07:30 wib saya berangkat ke sekolah'
# pola = re.compile(r'(\d+:\d+ \w+) saya (\w..+)')
# hasil = re.search(pola, teks)
# print(hasil)

# \ Tanda garis miring terbalik
teks = 'umur saya adalah 21 tahun'
hasil = re.search('\d+', teks)
print(hasil.group())