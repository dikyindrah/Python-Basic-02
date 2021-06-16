def status_permainan(pilihan, pilihan_komputer, pilihan_user):
    status = ''

    if pilihan_user == 'batu' and pilihan_komputer == 'kertas':
        status = 'Menang'
    elif pilihan_user == 'batu' and pilihan_komputer == 'gunting':
        status = 'Menang'
    elif pilihan_user == 'batu' and pilihan_komputer == 'batu':
        status = 'Seri'
    elif pilihan_user == 'gunting' and pilihan_komputer == 'kertas':
        status = 'Menang'
    elif pilihan_user == 'gunting' and pilihan_komputer == 'batu':
        status = 'Kalah'
    elif pilihan_user == 'gunting' and pilihan_komputer == 'gunting':
        status = 'Seri'
    elif pilihan_user == 'kertas' and pilihan_komputer == 'gunting':
        status = 'Kalah'
    elif pilihan_user == 'kertas' and pilihan_komputer == 'kertas':
        status = 'Seri'
    else:
        status = 'Tidak diketahui.'
        
    return status