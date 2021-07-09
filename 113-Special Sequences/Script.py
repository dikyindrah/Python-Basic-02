import re

teks = '1.jeruk 2.apel 3.mangga 4.anggur 5.semangka'

# \d
hasil = re.findall('\d', teks)
print(hasil)

# \D
hasil = re.findall('\D', teks)
print(hasil)
hasil = re.findall('\D+', teks)
print(hasil)

# \s
hasil = re.findall('\s', teks)
print(hasil)

# \S
hasil = re.findall('\S', teks)
print(hasil)
hasil = re.findall('\S+', teks)
print(hasil)

# \w 
hasil = re.findall('\w', teks)
print(hasil)
hasil = re.findall('\w+', teks)
print(hasil)

# \W 
hasil = re.findall('\W', teks)
print(hasil)

# \A dan \B
teks = 'matahari bersinar terang'

hasil = re.findall('\Amatahari', teks)
print(hasil)
hasil = re.findall('terang\Z', teks)
print(hasil)

# \b
hasil = re.findall(r'\bmatahari', teks)
print(hasil)
hasil = re.findall(r'terang\b', teks)
print(hasil)

# \B
hasil = re.findall(r'bersinar\b', teks)
print(hasil)
