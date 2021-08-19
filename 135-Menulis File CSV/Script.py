import csv

# Menulis data dalam satu baris menggunakan writerow()
# with open('D:/Programming/web/Python/Python-Basic-02/135-Menulis File CSV/myfile.csv', mode='w', newline='\n') as file:
#     write = csv.writer(file)
#     write.writerow(['No','Nama','Profesi'])
#     write.writerow(['1','Diky Indra H','Programmer'])
#     write.writerow(['2','Ardi Wibowo','IT Support'])
#     write.writerow(['3','Tubagus Bagas','Manager'])

# Menulis data dalam beberapa baris menggunakan writerows()
list_data = [['No','Nama','Profesi'], 
             ['1','Diky Indra H','Programmer'],
             ['2','Ardi Wibowo','IT Support'],
             ['3','Tubagus Bagas','Manager']]

with open('D:/Programming/web/Python/Python-Basic-02/135-Menulis File CSV/myfile.csv', mode='w', newline='\n') as file:
    write = csv.writer(file)
    write.writerows(list_data)
