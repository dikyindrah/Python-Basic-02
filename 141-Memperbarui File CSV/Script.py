import csv

file_path = 'D:/Programming/web/Python/Python-Basic-02/141-Memperbarui File CSV/myfile.csv'
tmp_file = []
fieldnames = ['no','nama','profesi']

# # Mengubah data pada baris
# Membaca dan menyalin data pada file ke variable list
with open(file_path, mode='r', newline='\n') as my_file_csv:
    file = csv.DictReader(my_file_csv)
    for data in file: tmp_file.append(data)

# Menampilkan data dari variable list
print('\nno \t nama \t\t profesi')
for data in tmp_file: print(f"{data['no']} \t {data['nama']} \t {data['profesi']}")

# Mengubah data pada variable list
no = '2'
print(f"\nmengubah data no.{no}")
for i in range(len(tmp_file)):
    if tmp_file[i]['no'] == '2':
        nama = str(input('nama \t: '))
        profesi = str(input('profesi : '))
        tmp_file[i]['nama'], tmp_file[i]['profesi'] = nama, profesi

# Menulis data dari variable list ke file
with open(file_path, mode='w', newline='\n') as my_file_csv:
    file = csv.DictWriter(my_file_csv, fieldnames)
    file.writeheader()
    file.writerows(tmp_file)

        

