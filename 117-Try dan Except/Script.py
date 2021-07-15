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

