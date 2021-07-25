import sys
import time

myfile = open('D:/Programming/web/Python/Python-Basic-02/128-Buffering/myfile.txt', 'a', 12)
myfile.write('hari ini adalah hari yang cerah, matahari bersinar terang.')
myfile.close()

# Memeriksa waktu proses dalam hitungan detik
waktu = time.time()
print(f'waktu proses {waktu} detik')