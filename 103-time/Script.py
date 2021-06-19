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
tm.sleep(2.0)
print('Program selesai...')
