import csv

# Mendefinisikan dialek dengan fungsi register_dialek()
csv.register_dialect('my_dialect', delimiter='|', skipinitialspace=True, quoting=csv.QUOTE_ALL)

with open('D:/Programming/web/Python/Python-Basic-02/140-Membaca File CSV Dengan Dialect/myfile.csv', mode='r', newline='\n') as file:
    # Menggunakan nama dialek sebagai nilai argumen pada 
    # parameter fungsi reader()
    read = csv.reader(file, dialect='my_dialect')
    for r in read:
        print(r)
    