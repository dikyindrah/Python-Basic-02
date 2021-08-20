import csv

fields = ['id', 'produk', 'harga']
records = [['p001', 'kipas angin', '150000'],
           ['p002', 'tv', '2500000'],
           ['p003', 'lampu', '15000']]

with open('D:/Programming/web/Python/Python-Basic-02/137-Menulis File CSV Dengan Dialect/myfile.csv', mode='w', newline='\n') as file:
    # Mendefinisikan dialek dengan fungsi register_dialek()
    csv.register_dialect('my_dialect', delimiter='|', quoting=csv.QUOTE_ALL)
    
    # Menggunakan nama dialek sebagai nilai argumen pada 
    # parameter fungsi writer()
    write = csv.writer(file, dialect='my_dialect')
    
    write.writerow(fields)
    write.writerows(records)