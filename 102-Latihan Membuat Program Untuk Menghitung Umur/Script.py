import datetime as dt

tanggal_saat_ini = dt.date.today()

hari = int(input('hari  : '))
bulan = int(input('bulan : '))
tahun = int(input('tahun : '))

tanggal_saya_lahir = dt.date(year=tahun, month=bulan, day=hari)

umur_saya = (tanggal_saat_ini - tanggal_saya_lahir)/365.25
print('umur kamu adalah {} tahun'.format(umur_saya.days))