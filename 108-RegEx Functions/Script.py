import re

# findall()
f_teks = '27 November 1999'

f_pola = '\d+'
f_hasil = re.findall(f_pola, f_teks)
print(f_hasil)


# search()
sh_teks_1 = 'python adalah bahasa pemrograman yang mudah untuk digunakan'
sh_teks_2 = 'nomor whatsapp : 082112345678'

sh_pola_1 = 'pemrograman'
sh_pola_2 = '\d\d\d\d\d\d\d\d\d\d\d\d'

sh_hasil_1 = re.search(sh_pola_1, sh_teks_1)
sh_hasil_2 = re.search(sh_pola_2, sh_teks_2)

print(sh_hasil_1)
print(sh_hasil_2)

# group()
print(sh_hasil_2.group())

# start(), end(), dan span()
print('teks = {}'.format(sh_teks_1))
print('panjang teks = {}'.format(len(sh_teks_1)))
print('teks yang dicari = {}'.format(sh_hasil_1.group()))
print('teks {} ditemukan pada rentang indeks {} sampai {}'.format(sh_hasil_1.group(), sh_hasil_1.start(), sh_hasil_1.end()))
print(sh_hasil_1.span())

# re dan string
print(sh_hasil_2.re)
print(sh_hasil_2.string)


# split()
st_teks_1 = 'hari ini hujan'
st_teks_2 = '123-456-789-101'

st_pola_1 = '\s'
st_pola_2 = r'\D'

st_hasil_1 = re.split(st_pola_1, st_teks_1)
st_hasil_2 = re.split(st_pola_2, st_teks_2)


print(st_hasil_1)
print(st_hasil_2)

# Maxsplit = 1
st_hasil_3 = re.split(st_pola_2, st_teks_2, 1)

# Maxsplit = 2 
st_hasil_4 = re.split(st_pola_2, st_teks_2, 2)

print(st_hasil_3)
print(st_hasil_4)