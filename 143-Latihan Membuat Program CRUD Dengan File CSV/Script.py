import csv
import os
import platform

my_file_path = 'D:/Programming/web/Python/Python-Basic-02/143-Latihan Membuat Program CRUD Dengan File CSV/myfile.csv'

def show_menu():
    print(f"{'='*5}Buku Telepon{'='*5}")
    print('[1] Lihat Daftar Kontak')
    print('[2] Tambah Kontak')
    print('[3] Ubah Kontak')
    print('[5] Hapus Kontak')
    print('[6] Cari Kontak')
    print('[0] Keluar')

    selected_menu = str(input('\nPilih menu : '))
    if selected_menu == '1':
        show_contact()
    elif selected_menu == '2':
        add_contact()
    elif selected_menu == '3':
        pass
    elif selected_menu == '4':
        pass
    elif selected_menu == '5':
        pass
    elif selected_menu == '6':
        pass
    elif selected_menu == '0':
        pass
    else:
        print('\nMenu yang anda pilih tidak diketahui.')
        back_to_menu()

def clear_screen():
    if platform.system() == 'Windows': 
        os.system('cls')
    else: 
        os.system('clear')

def back_to_menu():
    input('\nTekan enter untuk kembali...')
    clear_screen()
    show_menu()

def show_contact():
    clear_screen()
    contact = []
    with open(my_file_path, mode='r', encoding='UTF-8', newline='\n') as my_file_csv:
        file = csv.DictReader(my_file_csv)
        for data in file:
            contact.append(data)
    
    print(f"{'='*5}Lihat Daftar Kontak{'='*5}")
    field = list(contact[0].keys())
    print(f"{field[0]}\t{field[1]}\t\t{field[2]}")
    for data in contact:
        print(f"{data['No']}\t{data['Nama']}\t{data['Kontak']}")
    
    back_to_menu()

def add_contact():
    clear_screen()
    with open(my_file_path, mode='a', encoding='UTF-8', newline='\n') as my_file_csv:
        fieldnames = ['No','Nama','Kontak']
        file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
        
        No = str(input('No : '))
        Nama = str(input('Nama : '))
        Kontak = str(input('Kontak : '))

        file.writerow({'No':No,'Nama':Nama,'Kontak':Kontak})
        print('\nKontak berhasil ditambahkan.')
    
    back_to_menu()



show_menu()