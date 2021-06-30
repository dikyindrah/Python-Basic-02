import re

teks = '1.python 2.golang 3.php'

# Membuat pola dengan langsung menulisnya 
# sebagai argumen method
hasil = re.findall('golang', teks)
print(hasil)

# Membuat pola dengan menulis dan 
# menyimpannya kedalam variabel
pola = '\d'
hasil = re.findall(pola, teks)
print(hasil)

# Membuat objek pola dengan method
# compile()
pola = re.compile('\d')
hasil = re.findall(pola, teks)
print(hasil)
