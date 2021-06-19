import time as tm

jam_hidup = True

while jam_hidup == True:
    waktu = tm.localtime()
    format_waktu = tm.strftime('%H:%M:%S', waktu)
    print(format_waktu)
    tm.sleep(1.0)