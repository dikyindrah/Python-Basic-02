import csv

fields = ['no','nama','kontribusi']
records = [['1','guido van rossum','python'],
           ['2','tim barners-lee','world wide web'],
           ['3','linus torvalds','linux kernel']]

# # Menulis file csv dengan delimiter tanda pipa (|)
# with open('D:/Programming/web/Python/Python-Basic-02/136-Menulis File CSV Dengan Delimiter Khusus/myfile.csv', mode='w', newline='\n') as file:
#     write = csv.writer(file, delimiter='|')
#     write.writerow(fields)
#     write.writerows(records)

# # Menulis file csv menggunakan tanda kutip
# with open('D:/Programming/web/Python/Python-Basic-02/136-Menulis File CSV Dengan Delimiter Khusus/myfile.csv', mode='w', newline='\n') as file:
#     write = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
#     write.writerow(fields)
#     write.writerows(records)

# Menulis file csv menggunakan tanda kutip dengan karakter khusus
with open('D:/Programming/web/Python/Python-Basic-02/136-Menulis File CSV Dengan Delimiter Khusus/myfile.csv', mode='w', newline='\n') as file:
    write = csv.writer(file, delimiter=';', quoting=csv.QUOTE_ALL, quotechar='*')
    write.writerow(fields)
    write.writerows(records)