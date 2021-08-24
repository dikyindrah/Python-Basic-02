import csv

# # Cara pertama
# with open('D:/Programming/web/Python/Python-Basic-02/138-Membaca File CSV/myfile.csv', mode='r', newline='\n') as file:
#     read = csv.reader(file)
#     for row in read:
#         print(row)

# # Cara kedua
# with open('D:/Programming/web/Python/Python-Basic-02/138-Membaca File CSV/myfile.csv', mode='r', newline='\n') as file:
#     read = csv.reader(file)
#     data = list(read)

#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             print(data[i][j], end=' ')
#         print('')

# Membaca file csv sebagai dictionary
# Cara pertama
# with open('D:/Programming/web/Python/Python-Basic-02/138-Membaca File CSV/myfile.csv', mode='r', newline='\n') as file:
#     read_dict = csv.DictReader(file)
#     for row in read_dict:
#         print(row)

# Cara kedua
with open('D:/Programming/web/Python/Python-Basic-02/138-Membaca File CSV/myfile.csv', mode='r', newline='\n') as file:
    csv_file = csv.DictReader(file)
    list_csv_file = list(csv_file)
    for i in range(len(list_csv_file)):
        if i == 0:
            for key in list_csv_file[i].keys():
                print(key, end='')
            print('')
        
        for value in list_csv_file[i].values():
            print(value, end='')
        print('')