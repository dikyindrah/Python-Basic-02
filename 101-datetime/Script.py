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

# Mengatur urutan pada tanggal dan waktu saat ini
saat_ini = dt.datetime.now()

tgl = saat_ini.day
bln = saat_ini.month
thn = saat_ini.year

jam = saat_ini.hour
mnt = saat_ini.minute
dtk = saat_ini.second

print('Tanggal saat ini {}-{}-{}'.format(tgl, bln, thn))
print('Waktu saat ini {}:{}:{}'.format(jam, mnt, dtk))
