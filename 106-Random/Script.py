import random

# Mendapatkan sebuah angka secara acak dari angka 1 sampai 10
angka_acak = random.randint(1, 10)
print('Sebuah angka acak dari 1 sampai 10 adalah {}'.format(angka_acak))

# Mendapatkan sebuah item secara acak dari list
list_string = ['Jeruk', 'Apel', 'Mangga', 'Anggur']
item_acak = random.choice(list_string)
print('Item acak dari {} adalah {}'.format(list_string, item_acak))