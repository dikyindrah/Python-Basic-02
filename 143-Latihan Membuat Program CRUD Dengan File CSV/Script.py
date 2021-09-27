import csv
import os
import platform

my_file_path = 'D:/Programming/web/Python/Python-Basic-02/143-Latihan Membuat Program CRUD Dengan File CSV/myfile.csv'

def show_menu():
    print(f"{'='*10}Buku Telepon{'='*10}")
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
        print('\nPerintah tidak diketahui.')
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
    nama = str(input('Nama \t: '))
    Kontak = str(input('Kontak \t: '))
    
    add = str(input('\nTambahkan ke daftar kontak? [y/t]: '))

    if add.lower() == 'y':
        with open(my_file_path, mode='a', encoding='UTF-8', newline='\n') as my_file_csv:
            fieldnames = ['Nama','Kontak']
            file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
            file.writerow({'Nama':nama,'Kontak':Kontak})
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
    
    print(f"{'='*10}Ubah Kontak{'='*10}")
    show_contact_from_temporary()

    try:
        no = int(input('\nPilih \'No\' untuk mengubah kontak: '))
    except:
        no = 0

    data_found = False
    for i in range(len(tmp_contact)):
        if i == no-1:
            data_found = True
            break;
        
    if data_found == True:
        clear_screen()
        print(f"{'='*5}Ubah Kontak{'='*5}")
        field = list(tmp_contact[0].keys())
        print(f"No\t{field[0]}\t\t{field[1]}")
        print(f"{no}\t{tmp_contact[no-1]['Nama']}\t{tmp_contact[no-1]['Kontak']}")

        nama = str(input('\nNama \t: '))
        kontak = str(input('Kontak \t: '))
        tmp_contact[no-1]['Nama'] = nama
        tmp_contact[no-1]['Kontak'] = kontak

        with open(my_file_path, mode='w', encoding='UTF-8', newline='\n') as my_file_csv:
            fieldnames = ['Nama', 'Kontak']
            file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
            file.writeheader()
            file.writerows(tmp_contact)
    else:
        print('\nKontak tidak ditemukan.')

    back_to_menu()

def delete_contact():
    clear_screen()
    tmp_contact = add_contact_to_temporary()
    
    print(f"{'='*10}Hapus Kontak{'='*10}")    
    show_contact_from_temporary()

    try:
        no = int(input('\nPilih \'No\' untuk menghapus kontak: '))
    except:
        no = 0

    data_found = False
    for i in range(len(tmp_contact)):
        if i == no-1:
            data_found = True
            break;

    if data_found == True:
        tmp_contact.remove(tmp_contact[no-1])
        with open(my_file_path, mode='w', encoding='UTF-8', newline='\n') as my_file_csv:
            fieldnames = ['Nama','Kontak']
            file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
            file.writeheader()
            file.writerows(tmp_contact)
        print('\nKontak berhasil dihapus.')
    else:
        print('\nKontak tidak ditemukan.')
    
    back_to_menu()

def search_contact():
    clear_screen()
    tmp_contact = add_contact_to_temporary()

    print(f"{'='*10}Cari Kontak{'='*10}")
    print('[1] No')
    print('[2] Nama')
    print('[3] Kontak')

    selected_menu = str(input('\nPilih \'No\' untuk memilih jenis pencarian: '))
    if selected_menu == '1':
        clear_screen()
        print(f"{'='*10}Cari Kontak{'='*10}")
        show_contact_from_temporary()

        try:
            no = int(input('\nPilih \'No\' untuk mencari kontak: '))
        except:
            no = 0
        
        kontak_found = False
        for i in range(len(tmp_contact)):
            if i == no-1:
                kontak_found = True
                break;
        
        clear_screen()
        print(f"{'='*10}Cari Kontak{'='*10}")
        if kontak_found == True:
            print('Kontak ditemukan.\n')
            field = list(tmp_contact[0].keys())
            print(f"No\t{field[0]}\t\t{field[1]}")
            print(f"{no}\t{tmp_contact[no-1]['Nama']}\t{tmp_contact[no-1]['Kontak']}")
        else:
            print('Kontak tidak ditemukan!')
    elif selected_menu == '2':
        clear_screen()
        print(f"{'='*10}Cari Kontak{'='*10}")
        show_contact_from_temporary()
        nama = str(input('\nPilih \'Nama\' untuk mencari kontak: '))
        kontak_found = False
        index_kontak = []
        for i in range(len(tmp_contact)):
            if nama in tmp_contact[i]['Nama']:
                kontak_found = True
                index_kontak.append(i)
        
        clear_screen()
        print(f"{'='*10}Cari Kontak{'='*10}")
        if kontak_found == True:
            print(f"Total kontak ditemukan {len(index_kontak)}\n")
            field = list(tmp_contact[0].keys())
            print(f"No\t{field[0]}\t\t{field[1]}")
            for i in range(len(index_kontak)):
                print(f"{index_kontak[i]+1}\t{tmp_contact[index_kontak[i]]['Nama']}\t{tmp_contact[index_kontak[i]]['Kontak']}")
        else:
            print('Kontak tidak ditemukan.')
    elif selected_menu == '3':
        clear_screen()
        print(f"{'='*10}Cari Kontak{'='*10}")
        show_contact_from_temporary()
        kontak = str(input('\nPilih \'Kontak\' untuk mencari kontak: '))
        kontak_found = False
        index_kontak = []
        for i in range(len(tmp_contact)):
            if kontak in tmp_contact[i]['Kontak']:
                kontak_found = True
                index_kontak.append(i)
        
        clear_screen()
        print(f"{'='*10}Cari Kontak{'='*10}")
        if kontak_found == True:
            print(f"Total kontak ditemukan {len(index_kontak)}\n")
            field = list(tmp_contact[0].keys())
            print(f"No\t{field[0]}\t\t{field[1]}")
            for i in range(len(index_kontak)):
                print(f"{index_kontak[i]+1}\t{tmp_contact[index_kontak[i]]['Nama']}\t{tmp_contact[index_kontak[i]]['Kontak']}")
        else:
            print('Kontak tidak ditemukan.')
    else:
        print('\nPerintah tidak diketahui!')
    
    back_to_menu()

def close_menu():
    clear_screen()
    os.system('exit')

if __name__ == '__main__':
    show_menu()