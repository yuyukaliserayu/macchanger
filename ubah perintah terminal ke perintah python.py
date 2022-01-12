#1. Mengubah perintah di terminal menjadi perintah di python
#root@kali: ~ # ifconfig eth0 down	1. nonaktifkan device target
#root@kali: ~ # ifconfig eth0 hw ether 08:00:27:0e:34:8d	2. ubah mac address
#root@kali: ~ # ifconfig eth0 up	3. aktifkan device target

#ubah ke perintah python
import subprocess
subprocess.call('ifconfig ' + interface + ' down', shell=True)	#1. nonaktifkan device target
subprocess.call('ifconfig ' + eth0 + ' hw ether '+ 08:00:27:0e:34:8d, shell=True) 	#2. ubah mac address
subprocess.call('ifconfig ' + interface + ' up', shell=True)	#3. aktifkan device target



