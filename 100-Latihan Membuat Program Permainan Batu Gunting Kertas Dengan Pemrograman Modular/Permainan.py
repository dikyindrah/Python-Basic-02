import Komputer
import Periksa
import Status

pilihan = ['batu', 'gunting', 'kertas',]

print('====={}=====\n'.format('Permainan Batu Gunting Kertas'))
user = str(input('Pilih salah satu (batu, gunting, kertas) : ')) 
pilihan_user = str.lower(user)

pilihan_komputer = Komputer.komputer(pilihan)

pilihan_user_ada = Periksa.periksa_pilihan_user(pilihan, pilihan_user)

if pilihan_user_ada == True:
    status = Status.status_permainan(pilihan, pilihan_komputer, pilihan_user)
    print('\n==========================')
    print('Kamu memilih     = {}'.format(pilihan_user))
    print('Komputer memilih = {}'.format(pilihan_komputer))
    print('====={}====='.format('Status Permainan'))
    print(status)
    print('==========================\n')
else:
    print('Kamu tidak boleh memilih selain batu, guntung, dan kertas.') 