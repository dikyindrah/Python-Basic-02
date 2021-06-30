import re

# findall()
teks = '27 November 1999'
hasil = re.findall(r'\d+', teks)
print(hasil)


# search()
teks = 'javascript, php, pyhton, 12345, go, r'
hasil = re.search(r'\d\d\d\d\d', teks)
print(len(teks))
print(hasil)


# group()
print(hasil.group())

# start(), end(), dan span()
print(hasil.start())
print(hasil.end())
print(hasil.span())

# re dan string
print(hasil.re)
print(hasil.string)


# split()
teks = 'hari ini hujan lebat'

hasil = re.split(r'\s', teks)
print(hasil)

# Maxsplit = 1
mx_hasil = re.split(r'\s', teks, 1)
print(mx_hasil)

# Maxsplit = 2
mx_hasil = re.split(r'\s', teks, 2)
print(mx_hasil)


# sub()
teks  = 'saya sedang belajar java'
hasil = re.sub('java', 'python', teks)
print(hasil)

teks  = 'java, java, java, java, java, java, java'
hasil = re.sub('java', 'python', teks, 3)
print(hasil)

# subn()
teks  = 'java, go, java, go, java, go, java'
hasil = re.subn('java', 'python', teks)
print(hasil)