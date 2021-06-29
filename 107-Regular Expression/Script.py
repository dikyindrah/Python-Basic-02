import re

pesan = 'ini adalah nomor teleponku 082181177026, tolong disimpan ya!'

# Mencari nomor telepon dengan cara manual
nomor_telepon = ''
for i in range(len(pesan)):
    teks = pesan[i:i+12]
    if teks.isdigit():
        if len(teks) == 12:
            nomor_telepon = teks

print('Nomor telepon ditemukan : {}'.format(nomor_telepon))

# Mencari nomor telepon dengan regex
pola = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d')
nomor_telepon = pola.search(pesan)
print('Nomor telepon ditemukan : {}'.format(nomor_telepon))