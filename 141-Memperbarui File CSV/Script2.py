import csv 

file_path = 'D:/Programming/web/Python/Python-Basic-02/141-Memperbarui File CSV/myfile2.csv'
temp_file = []
fieldnames = ['no','nama','profesi']

# # Mengubah data pada kolom
# Membaca dan menyalin data pada file ke variable list
with open(file_path, mode='r', newline='\n') as my_file_csv:
    file = csv.DictReader(my_file_csv)
    for data in file: temp_file.append(data)

# Menampilkan data dari variable list
print('\nno \t nama \t\t profesi')
for data in temp_file: print(f"{data['no']} \t {data['nama']} \t {data['profesi']}")

# Mengubah data pada variable list
col = 'nama'
no = '1'
nama = 'diky indra h'
profesi = 'manager'
print(f"\nmengubah seluruh data pada kolom {col}")
for i in range(len(temp_file)):
    if temp_file[i][col]: 
        if col == 'no': temp_file[i][col] = no
        elif col == 'nama': temp_file[i][col] = nama
        elif col == 'profesi': temp_file[i][col] = profesi
        else: print('data tidak diketahui.')

# Menulis data dari variable list ke file
with open(file_path, mode='w', newline='\n') as my_file_csv:
    file = csv.DictWriter(my_file_csv, fieldnames)
    file.writeheader()
    file.writerows(temp_file)