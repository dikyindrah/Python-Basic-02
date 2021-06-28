import math

# Faktorial dengan modul math
nilai = 5
nilai_faktorial = math.factorial(nilai)
print('Nilai faktorial {} adalah {}'.format(nilai, nilai_faktorial))

# Faktorial dengan cara manual
tmp2 = 1
for i in range(1, nilai+1):
    tmp1 = i
    tmp2 = tmp2 * tmp1

print('Nilai faktorial {} adalah {}'.format(nilai, tmp2))
    
# Mendapatkan nilai pada bilangan berpangkat
pangkat = 2
nilai_pangkat = int(math.pow(nilai, pangkat))
print('{} pangkat {} sama dengan {}'.format(nilai, pangkat, nilai_pangkat))

# Mendapatkan nilai pada bilangan akar kuadrat
nilai_akar = int(math.sqrt(400))
print('Akar kuadrat dari {} adalah {}'.format(400, nilai_akar))

# Mendapatkan jumlah nilai pada sebuah iterable (list, tuple, dll)
list_integer = [10, 20, 30, 40, 50]
jumlah = int(math.fsum(list_integer))
print('Jumlah nilai {} adalah {}'.format(list_integer, jumlah)) 