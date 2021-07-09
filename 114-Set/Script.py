import re
from typing import List

teks = 'hari ini sangat cerah'

# [arn]
hasil = re.findall('[arn]', teks)
print(hasil)
print('a : {}'.format(hasil.count('a')))
print('r : {}'.format(hasil.count('r')))
print('n : {}'.format(hasil.count('n')))

# [a-n]
hasil = re.findall('[a-n]', teks)
print(hasil)

# [^arn]
hasil = re.findall('[^arn]', teks)
print(hasil)



# [0,1,2,3]
teks = '0.anggur 1.jeruk 2.apel 3.mangga'

hasil = re.findall('[0,1,2,3]', teks)
print(hasil)

# [0-9]
teks = '017175159'

hasil = re.findall('[0-9]', teks)
print(hasil)

# [0-5][0-9]
teks = '017175159'

hasil = re.findall('[0-5][0-9]', teks)
print(hasil)

# [a-zA-Z]
teks = 'Hari Ini'

hasil = re.findall('[a-zA-Z]', teks)
print(hasil)

# [+]
teks = '5 + 5 + 5 = 15'
hasil = re.findall('[+]', teks)
print(hasil)




