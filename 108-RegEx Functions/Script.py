import re

# findall()
teks = '27 November 1999'

pola = '\d+'
hasil = re.findall(pola, teks)
print(hasil)


# search()
teks_1 = 'python adalah bahasa pemrograman yang mudah untuk digunakan'
teks_2 = 'nomor whatsapp : 082112345678'

pola_1 = 'pemrograman'
pola_2 = '\d\d\d\d\d\d\d\d\d\d\d\d'

hasil_1 = re.search(pola_1, teks_1)
hasil_2 = re.search(pola_2, teks_2)

print(hasil_1)
print(hasil_2)

# group()
print(hasil_2.group())

# start(), end(), dan span()
print('teks = {}'.format(teks_1))
print('panjang teks = {}'.format(len(teks_1)))
print('teks yang dicari = {}'.format(hasil_1.group()))
print('teks {} ditemukan pada rentang indeks {} sampai {}'.format(hasil_1.group(), hasil_1.start(), hasil_1.end()))
print(hasil_1.span())

# re dan string
print(hasil_2.re)
print(hasil_2.string)