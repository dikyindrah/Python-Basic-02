# input -1
n = int(input('input nilai: '))

if n <= 0:
    # Menentukan pengecualian & teks yang akan di tampilkan
    raise ValueError('nilai n harus bilangan positif')

try:
    n = int(input('input nilai: '))
    if n <= 0:
        # Menentukan pengecualian & teks yang akan di tampilkan
        raise ValueError('nilai n harus bilangan positif')
except ValueError as ve:
    # Menampilkan teks dari pengecualian yang terjadi
    print(ve)