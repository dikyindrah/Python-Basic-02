import csv
import os
import platform

my_file_path = 'D:/Programming/web/Python/Python-Basic-02/143-Latihan Membuat Program CRUD Dengan File CSV/myfile.csv'

def show_menu():
    print(f"{'='*5}Buku Telepon{'='*5}")
    print('[1] Lihat Daftar Kontak')
    print('[2] Tambah Kontak')
    print('[3] Ubah Kontak')
    print('[4] Hapus Kontak')
    print('[5] Cari Kontak')
    print('[0] Keluar')

    selected_menu = str(input('\nPilih nomor untuk memilih menu: '))
    if selected_menu == '1':
        show_contact()
    elif selected_menu == '2':
        add_contact()
    elif selected_menu == '3':
        update_contact()
    elif selected_menu == '4':
        delete_contact()
    elif selected_menu == '5':
        search_contact()
    elif selected_menu == '0':
        close_menu()
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

def add_contact_to_temporary():
    contact = []
    with open(my_file_path, mode='r', encoding='UTF-8', newline='\n') as my_csv_file:
        file = csv.DictReader(my_csv_file)
        for data in file:
            contact.append(data)
    
    return contact

def show_contact_from_temporary():
    tmp_contact = add_contact_to_temporary()

    if not tmp_contact:
        print('Belum ada kontak.')
    else:
        field = list(tmp_contact[0].keys())
        print(f"No\t{field[0]}\t\t{field[1]}")
        for i in range(len(tmp_contact)):
            print(f"{i+1}\t{tmp_contact[i]['Nama']}\t{tmp_contact[i]['Kontak']}")

def show_contact():
    clear_screen()

    print(f"{'='*10}Lihat Daftar Kontak{'='*10}")
    tmp_contact = add_contact_to_temporary()
    total_contact = len(tmp_contact)
    print(f"Total kontak : {total_contact}\n")
    show_contact_from_temporary()

    back_to_menu()

def add_contact():
    clear_screen()

    print(f"{'='*10}Tambah Kontak{'='*10}")
    Nama = str(input('Nama \t: '))
    Kontak = str(input('Kontak \t: '))
    
    add = str(input('\nTambahkan ke daftar kontak? [y/t]: '))

    if add.lower() == 'y':
        with open(my_file_path, mode='a', encoding='UTF-8', newline='\n') as my_file_csv:
            fieldnames = ['Nama','Kontak']
            file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
            file.writerow({'Nama':Nama,'Kontak':Kontak})
            print('\nKontak telah ditambahkan.')
        back_to_menu()
    elif add.lower() == 't':
        print('\nKontak tidak ditambahkan.')
        back_to_menu()
    else:
        print('\nPerintah tidak diketahui!')
        back_to_menu()

def update_contact():
    clear_screen()
    tmp_contact = add_contact_to_temporary()
    
    print(f"{'='*5}Ubah Kontak{'='*5}")
    show_contact_from_temporary()

    No = int(input('\nPilih \'No\' untuk mengubah kontak: '))
    data_found = False
    for i in range(len(tmp_contact)):
        if i == No-1:
            data_found = True
            break;
    
    if data_found == True:
        clear_screen()
        print(f"{'='*5}Ubah Kontak{'='*5}")
        field = list(tmp_contact[0].keys())
        print(f"No\t{field[0]}\t\t{field[1]}")
        print(f"{No}\t{tmp_contact[No-1]['Nama']}\t{tmp_contact[No-1]['Kontak']}")

        Nama = str(input('\nNama \t: '))
        Kontak = str(input('Kontak \t: '))
        tmp_contact[No-1]['Nama'] = Nama
        tmp_contact[No-1]['Kontak'] = Kontak

        with open(my_file_path, mode='w', encoding='UTF-8', newline='\n') as my_file_csv:
            fieldnames = ['Nama', 'Kontak']
            file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
            file.writeheader()
            file.writerows(tmp_contact)
    else:
        print('Kontak tidak ditemukan.')

    back_to_menu()

def delete_contact():
    clear_screen()
    tmp_contact = add_contact_to_temporary()

    show_contact_from_temporary()
    No = int(input('\nPilih \'No\' untuk menghapus kontak: '))
    data_found = False
    for i in range(len(tmp_contact)):
        if i == No-1:
            data_found = True
            break;
    
    if data_found == True:
        tmp_contact.remove(tmp_contact[No-1])
        with open(my_file_path, mode='w', encoding='UTF-8', newline='\n') as my_file_csv:
            fieldnames = ['Nama','Kontak']
            file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
            file.writeheader()
            file.writerows(tmp_contact)
        print('Kontak berhasil dihapus.')
    else:
        print('Kontak tidak ditemukan.')
    
    back_to_menu()

def search_contact():
    clear_screen()
    all_contact = add_contact_to_temporary()

    show_contact_from_temporary()

    search_data = str(input('\nCari data : '))
    total_data = 0
    index_data = []
    for i in range(len(all_contact)):
        if (all_contact[i]['No'] == search_data 
        or all_contact[i]['Nama'] == search_data 
        or all_contact[i]['Kontak'] == search_data):
            total_data = total_data + 1
            index_data.append(i)

    clear_screen()
    if total_data != 0:
        print(f"Total data yang ditemukan {total_data}\n")
        field = list(all_contact[0].keys())
        print(f"{field[0]}\t{field[1]}\t\t{field[2]}")
        for i in range(len(index_data)):
            index = int(index_data[i])
            print(f"{all_contact[index]['No']}\t{all_contact[index]['Nama']}\t{all_contact[index]['Kontak']}")
    else:
        print('Data tidak ditemukan!')
    
    back_to_menu()

def close_menu():
    os.system('exit')

if __name__ == '__main__':
    show_menu()