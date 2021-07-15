try:
    print(x)
except:
    print('error!, variabel x belum didefinisikan.')


import sys

list_item = ['a', 0, 2]

for item in list_item:
    try:
        print('item :', item)
        n = int(item)/int(item)
        break
    except:
        print('Terjadi kesalahan :', sys.exc_info()[0], 'pada kode program')
        print('Selanjutnya..\n')

print(item,'/',item, '=', int(n))


try:
    for i in range(4):
        print(list_item[i])
except Exception as e:
    print(f'Terjadi kesalahan {e.__class__} pada kode program.')


try:
    print(x)
except NameError as ne:
    print(ne)


try:
    print(x)
except ValueError as ve:
    print(ve)
except NameError as ne:
    # Ini adalah penanganan yang sesuai dengan pengecualian
    print(ne)
except IndexError as ie:
    print(ie)


list_angka = [1, 2, 3, 4, 5]
try:
    for item in list_angka:
        print(item, end=' ')
except:
    e = sys.exc_info()[0]
    print(e)
else:
    print('\nTidak ada kesalahan yang terjadi.')