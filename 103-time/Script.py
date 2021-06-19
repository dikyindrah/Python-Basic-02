import time as tm

# print('\nProgram mulai...')

# for i in range(5):
#     print(i+1)
#     tm.sleep(2.0)

# print('Program berakhir...')

# time()
detik = tm.time()
print(detik)

# ctime
# Mengetahui tanggal dan waktu saat pertama kali 
# ditentukan
tgl_wkt_pertama = tm.ctime(0.0)
print(tgl_wkt_pertama)

# Mengetahui tanggal dan waktu saat ini
detik = tm.time()
tgl_wkt_saat_ini = tm.ctime(detik)
print(tgl_wkt_saat_ini)

# sleep()
print('Program dimulai...')
# tm.sleep(2.0)
print('Program selesai...')


# locltime
waktu_lokal = tm.localtime(1545925769)

# Struktur waktu dari kelas struct_tim()
print(waktu_lokal)

tgl = waktu_lokal.tm_mday
bln = waktu_lokal.tm_mon
thn = waktu_lokal.tm_year
jam = waktu_lokal.tm_hour
mnt = waktu_lokal.tm_min
dtk = waktu_lokal.tm_sec

print('{}-{}-{} {}:{}:{}'.format(tgl, bln, thn, jam, mnt, dtk))

# gmtime()
waktu_utc = tm.gmtime(1545925769)

# Struktur waktu dari kelas struct_tim()
print(waktu_utc)

tgl = waktu_utc.tm_mday
bln = waktu_utc.tm_mon
thn = waktu_utc.tm_year
jam = waktu_utc.tm_hour
mnt = waktu_utc.tm_min
dtk = waktu_utc.tm_sec

print('{}-{}-{} {}:{}:{}'.format(tgl, bln, thn, jam, mnt, dtk))


# mktime()
t = (1999, 11, 27, 0, 0, 0, 0, 0, 0)
waktu_mk = tm.mktime(t)
print(waktu_mk)


# asctime()
t = (1999, 11, 27, 0, 0, 0, 0, 0, 0)
waktu_asc = tm.asctime(t)
print(waktu_asc)

# strftime()
waktu = tm.localtime()
format_waktu = tm.strftime('%H:%M:%S', waktu)
print(format_waktu)

tanggal = tm.localtime()
format_tanggal = tm.strftime('%d-%m-%Y', tanggal)
print(format_tanggal)

# srtptime
str_waktu = '27 November 1999 12:30:45'
obj_waktu = tm.strptime(str_waktu, '%d %B %Y %H:%M:%S')
print(obj_waktu)

waktu_asc = tm.asctime(obj_waktu)
print(waktu_asc)