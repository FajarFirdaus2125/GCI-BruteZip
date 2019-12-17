#Copyright 2019 By FajarTheGGman
import zipfile as zp

def banner():
	print("[---- Bruteforce Zip By FajarTheGGman ----]\n")

def main():
	user = raw_input("[?] Input Zip File >_ ")
	pw = raw_input("[?] Input Wordlist >_ ")

	p = open(pw, "r")
	
	file = zp.ZipFile(user)
	for data in p:
		data = data.strip("\n").strip("\r")
		try:
			file.extractall(pwd=data)
			print("[+] Unlock : " + data)
		except:
			print("[!] Error : " + data)


banner()
main()