import re

teks = 'wa : 082123456789, ini adalah nomor telepon saya.'

# Mencari nomor telepon dengan cara manual
nomor_telepon = ''
for i in range(len(teks)):
    tmp = teks[i:i+12]
    if tmp.isdigit():
        if len(tmp) == 12:
            nomor_telepon = tmp

print(nomor_telepon)

# Mencari nomor telepon dengan regex
nomor_telepon = re.search(r'\d\d\d\d\d\d\d\d\d\d\d\d', teks)
print(nomor_telepon.group())