#2. program mendapatkan input dari user
				
import subprocess								#0. Modul yang dapat digunakan untuk menjalankan perintah shell yang dapat dieksekusi dengan Python

#program tambahan untuk mendapatkan input dari user
nama_interface = input('interface > ')						#1. buat variabel nama_interface untuk menampung nama interface yang dimasukkan user
mac_baru = input('mac baru > ')							#2. buat variabel mac_baru untuk menampung mac pengganti yang dimasukkan user

#program untuk mengubah mac address yang nama dan mac penggantinya telah didapat dari program diatas
subprocess.call('ifconfig ' + interface + ' down', shell=True)			#3. jalankan fungsi call yang ada di modul subprocess untuk menonaktifkan eth0
subprocess.call('ifconfig ' + interface + ' hw ether '+ mac_baru, shell=True)	#4. jalankan fungsi call yang ada di modul subprocess untuk mengubah mac address menjadi 08:00:27:0e:34:8d 
subprocess.call('ifconfig ' + interface + ' up', shell=True)			#5. jalankan fungsi call yang ada di modul subprocess untuk mengaktifkan eth0
		
print ('[+] Mengubah MAC address' + interface + 'ke' + mac_baru)		#6. tampilkan di layar keterangan bahwa mac address telah dirubah ke alamat mac baru



