import csv

my_file_path = 'D:/Programming/web/Python/Python-Basic-02/142-Menghapus Data Pada File CSV/myfile.csv'
tmp_file = []
fieldnames = ['no','nama','profesi']

with open(my_file_path, mode='r', newline='\n') as my_file_csv:
    file = csv.DictReader(my_file_csv)
    for data in file: tmp_file.append(data)

print(f"{'nomor'},{'nama'},{'profesi'}")
for data in tmp_file:
    print(f"{data['no']},{data['nama']},{data['profesi']}")

# # Menghapus satu data
# i = 0
# for data in tmp_file:
#     if data['no'] == '2':
#         tmp_file.remove(tmp_file[i])
#     i = i + 1

# Menghapus beberapa data
delete_data = 'manager'
total_data = 0
index = 0

for data in tmp_file:
    if data['profesi'] == delete_data:
        total_data = total_data + 1

for i in range(total_data+1):
    for data in tmp_file:
        if data['profesi'] == delete_data:
            tmp_file.remove(tmp_file[index])
        index = index + 1
    index = 0

print(f"{'nomor'},{'nama'},{'profesi'}")
for data in tmp_file:
    print(f"{data['no']},{data['nama']},{data['profesi']}")

with open(my_file_path, mode='w', newline='\n') as my_file_csv:
    file = csv.DictWriter(my_file_csv, fieldnames)
    file.writeheader()
    file.writerows(tmp_file)