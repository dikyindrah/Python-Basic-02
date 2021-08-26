import csv

# # Mendefinisikan dialek dengan fungsi register_dialek()
# csv.register_dialect('my_dialect', delimiter='|', skipinitialspace=True, quoting=csv.QUOTE_ALL)

# with open('D:/Programming/web/Python/Python-Basic-02/140-Membaca File CSV Dengan Dialect/myfile.csv', mode='r', newline='\n') as file:
#     # Menggunakan nama dialek sebagai nilai argumen pada 
#     # parameter fungsi reader()
#     read = csv.reader(file, dialect='my_dialect')
#     for r in read:
#         print(r)

# Mengetahui pemformatan yang digunakan pada file
# .csv dengan csv.sniffer() 
with open('D:/Programming/web/Python/Python-Basic-02/140-Membaca File CSV Dengan Dialect/myfile.csv', mode='r', newline='\n') as file:
    # Mengubah objek file ke string sebanyak 64 karakter
    sample = file.read(64)

    # Mendefinisikan header atau field dari file .csv
    has_header = csv.Sniffer().has_header(sample)
    print(has_header)

    # Mengetahui pemformatan yang digunakan pada file .csv
    deduced_dialect = csv.Sniffer().sniff(sample)

with open('D:/Programming/web/Python/Python-Basic-02/140-Membaca File CSV Dengan Dialect/myfile.csv', mode='r', newline='\n') as file:
    read = csv.reader(file, dialect=deduced_dialect)
    for row in read:
        print(row)