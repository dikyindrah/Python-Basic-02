import subprocess
import re

ssid = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output = True).stdout.decode()
nama_ssid = re.findall('All User Profile     : (.*)\r', ssid)
list_wifi = []

for nama in nama_ssid:
    info_ssid =  subprocess.run(['netsh', 'wlan', 'show', 'profile', nama], capture_output = True).stdout.decode()
    dict_wifi = {}

    if re.search('Security key           : Absent', info_ssid):
        continue
    else:
        dict_wifi['ssid'] = nama      
        info_key_ssid =  subprocess.run(['netsh', 'wlan', 'show', 'profile', nama, 'key=clear'], capture_output = True).stdout.decode()
        password_ssid = re.search('Key Content            : (.*)\r', info_key_ssid)
        if password_ssid == None:
            dict_wifi['password'] = None
        else:
            dict_wifi['password'] = password_ssid[1]
    
    list_wifi.append(dict_wifi)

for i in range(len(list_wifi)):
    print(list_wifi[i])
            


