import csv

# # Menulis data dalam satu baris menggunakan writerow()
# with open('D:/Programming/web/Python/Python-Basic-02/135-Menulis File CSV/myfile.csv', mode='w', newline='\n') as file:
#     write = csv.writer(file)
#     write.writerow(['No','Nama','Profesi'])
#     write.writerow(['1','Diky Indra H','Programmer'])
#     write.writerow(['2','Ardi Wibowo','IT Support'])
#     write.writerow(['3','Tubagus Bagas','Manager'])

# # Menulis data dalam beberapa baris menggunakan writerows()
# fields = ['No','Nama','Profesi']
# records = [['1','Diky Indra H','Programmer'],
#            ['2','Ardi Wibowo','IT Support'],
#            ['3','Tubagus Bagas','Manager']]

# with open('D:/Programming/web/Python/Python-Basic-02/135-Menulis File CSV/myfile.csv', mode='w', newline='\n') as file:
#     write = csv.writer(file)
#     # Menulis fields
#     write.writerow(fields)
#     # Menulis records
#     write.writerows(records)

# menulis file csv dari dictionary
with open('D:/Programming/web/Python/Python-Basic-02/135-Menulis File CSV/myfile.csv', mode='w', newline='\n') as file:
    fieldnames = ['id','nama','alamat']
    write = csv.DictWriter(file, fieldnames=fieldnames)

    write.writeheader()
    write.writerow({'id':'id001','nama':'diky indra h','alamat':'kedaton'})
    write.writerow({'id':'id002','nama':'dian budi p','alamat':'way kandis'})