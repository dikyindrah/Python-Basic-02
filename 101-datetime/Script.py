import datetime as dt

# Menampilkan tanggal dan waktu saat ini
tanggal_dan_waktu_saat_ini = dt.datetime.now()
print('Tanggal dan waktu saat ini : {}'.format(tanggal_dan_waktu_saat_ini))


# Kelas date
# Menampilkan tanggal saat ini
tanggal_saat_ini = dt.date.today()
print('Saat ini adalah tanggal {}'.format(tanggal_saat_ini))

# Mengatur urutan pada tanggal saat ini
tgl = tanggal_saat_ini.day
bln = tanggal_saat_ini.month
thn = tanggal_saat_ini.year
print('Saat ini adalah tanggal {}-{}-{}'.format(tgl, bln, thn))

# Menentukan tanggal sesuai dengan keinginan
tanggal_lahir_ucup = dt.date(year=1999, month=11, day=27)
print('Tanggal lahir ucup adalah {}'.format(tanggal_lahir_ucup))


# Kelas time
# Menampilkan waktu saat ini
now = dt.datetime.now()
waktu_saat_ini = dt.time(now.hour, now.minute, now.second)
print('Waktu saat ini {}'.format(waktu_saat_ini))

# Menentukan waktu sesuai dengan keinginan
waktu_makan_siang = dt.time(hour=11, minute=30, second=5)
print('Waktu makan siang adalah {}'.format(waktu_makan_siang))

# Kelas datetime
# Menampilkan tanggal saat ini
tanggal = dt.datetime.now().date()
print('Tanggal saat ini : {}'.format(tanggal))

# Menampilkan waktu saat ini
waktu = dt.datetime.now().time()
print('Waktu saat ini : {}'.format(waktu))

# Mengatur urutan atau memformat tanggal dan waktu
saat_ini = dt.datetime.now()

# Menggunakan cara manual
tgl = saat_ini.day
bln = saat_ini.month
thn = saat_ini.year

jam = saat_ini.hour
mnt = saat_ini.minute
dtk = saat_ini.second

print('Tanggal saat ini {}-{}-{}'.format(tgl, bln, thn))
print('Waktu saat ini {}:{}:{}'.format(jam, mnt, dtk))

# Menggunakan method strftime()
strf_format_tgl_1 = saat_ini.strftime('%d/%m/%Y')
strf_format_tgl_2 = saat_ini.strftime('%d-%m-%Y')
strf_format_wkt_1 = saat_ini.strftime('%H:%M:%S')
strf_format_wkt_2 = saat_ini.strftime('%H.%M.%S')

print('Format tanggal 1 : {}'.format(strf_format_tgl_1))
print('Format tanggal 2 : {}'.format(strf_format_tgl_2))
print('Format waktu 1 : {}'.format(strf_format_wkt_1))
print('Format waktu 2 : {}'.format(strf_format_wkt_2))

# Membuat Objek datetime Dari String Menggunakan Method strptime()
str_tgl = '27 November 1999'
str_wkt = '12:30:12'
str_tgl_wkt = '27 November 1999 12:30:12'

strp_format_tgl = dt.datetime.strptime(str_tgl, '%d %B %Y')
strp_format_wkt = dt.datetime.strptime(str_wkt, '%H:%M:%S')
strp_format_tgl_wkt = dt.datetime.strptime(str_tgl_wkt, '%d %B %Y %H:%M:%S')

print('String tanggal : {}, {}'.format(str_tgl, type(str_tgl)))
print('Objek datetime dari string tanggal : {}, {}'.format(strp_format_tgl, type(strp_format_tgl)))

print('String waktu : {}, {}'.format(str_wkt, type(str_wkt)))
print('Objek datetime dari string waktu : {}, {}'.format(strp_format_wkt, type(strp_format_wkt)))

print('String tanggal dan waktu : {}, {}'.format(str_tgl_wkt, type(str_tgl_wkt)))
print('Objek datetime dari string tanggal dan waktu : {}, {}'.format(strp_format_tgl_wkt, type(strp_format_tgl_wkt)))
