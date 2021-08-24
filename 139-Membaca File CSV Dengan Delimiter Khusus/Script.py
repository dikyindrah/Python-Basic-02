import csv

# # with open('D:/Programming/web/Python/Python-Basic-02/139-Membaca File CSV Dengan Delimiter Khusus/myfile.csv', mode='r', newline='\n') as file:
#     read = csv.reader(file, delimiter='|')
#     for r in read:
#         print(r)

# # Melewatkan spasi pada awal data 
# with open('D:/Programming/web/Python/Python-Basic-02/139-Membaca File CSV Dengan Delimiter Khusus/myfile.csv', mode='r', newline='\n') as file:
#     read = csv.reader(file, delimiter='|', skipinitialspace=True)
#     for r in read:
#         print(r)

# Memberikan tanda kutip pada data yang dibaca
with open('D:/Programming/web/Python/Python-Basic-02/139-Membaca File CSV Dengan Delimiter Khusus/myfile.csv', mode='r', newline='\n') as file:
    read = csv.reader(file, delimiter='|', skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
    for r in read:
        print(r)

