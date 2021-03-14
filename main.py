import random,requests,string, os
from colorama import init, Fore
init()

def Visa_mass_gen():
	amount = int(input(f"How many you want to generate and check :"))
	count = 0
	while count <= amount:
		gen = ''.join(random.choices(string.digits, k=4))
		unchecked_bin = "42"+gen
		r = requests.get(f"https://lookup.binlist.net/{unchecked_bin}")
		try:
			card_scheme = r.json()["scheme"]
		except:
			card_scheme = "None"
		try:
			card_type = r.json()["type"]
		except:
			card_type = "None"
		try:
			card_prepaid = r.json()["prepaid"]
		except:
			card_prepaid = "None"
		try:
			card_country = r.json()["country"]["name"]
		except:
			card_country = "None"
		try:
			card_country_al = r.json()["country"]["alpha2"]
		except:
			card_country_al = "None"
		try:
			card_currency = r.json()["country"]["currency"]
		except:
			card_currency = "None"
		try:
			bank_name = r.json()["bank"]["name"]
		except:
			bank_name = "None"
		try:
			bank_url = r.json()["bank"]["url"]
		except:
			bank_url = "None"
		try:
			bank_phone = r.json()["bank"]["phone"]
		except:
			bank_phone = "None"
		
		print("Bin:",unchecked_bin)
		print("~~~~~~~~~~~~~~~~~~~~~")
		f = open('MassGenCheckedBin.txt','a')
		f.write(f"Bin:{unchecked_bin}\nBin Scheme:{card_scheme}\nBin Type:{card_type}\nBin Prepaid:{card_prepaid}\nBin Country Code:{card_country_al}\nBin Country:{card_country}\nBin Currency:{card_currency}\nBank Name:{bank_name}\nBank Url:{bank_url}\nBank Phone:{bank_phone}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		f.close()
		count += 1
	os.system("pause >nul")

def Mastercard_mass_gen():
	amount = int(input(f"How many you want to generate and check :"))
	count = 0
	while count <= amount:
		gen = ''.join(random.choices(string.digits, k=4))
		unchecked_bin = "55"+gen
		r = requests.get(f"https://lookup.binlist.net/{unchecked_bin}")
		try:
			card_scheme = r.json()["scheme"]
		except:
			card_scheme = "None"
		try:
			card_type = r.json()["type"]
		except:
			card_type = "None"
		try:
			card_prepaid = r.json()["prepaid"]
		except:
			card_prepaid = "None"
		try:
			card_country = r.json()["country"]["name"]
		except:
			card_country = "None"
		try:
			card_country_al = r.json()["country"]["alpha2"]
		except:
			card_country_al = "None"
		try:
			card_currency = r.json()["country"]["currency"]
		except:
			card_currency = "None"
		try:
			bank_name = r.json()["bank"]["name"]
		except:
			bank_name = "None"
		try:
			bank_url = r.json()["bank"]["url"]
		except:
			bank_url = "None"
		try:
			bank_phone = r.json()["bank"]["phone"]
		except:
			bank_phone = "None"
		
		print("Bin:",unchecked_bin)
		print("~~~~~~~~~~~~~~~~~~~~~")
		f = open('MassGenCheckedBin.txt','a')
		f.write(f"Bin:{unchecked_bin}\nBin Scheme:{card_scheme}\nBin Type:{card_type}\nBin Prepaid:{card_prepaid}\nBin Country Code:{card_country_al}\nBin Country:{card_country}\nBin Currency:{card_currency}\nBank Name:{bank_name}\nBank Url:{bank_url}\nBank Phone:{bank_phone}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		f.close()
		count += 1
	os.system("pause >nul")

def Visa_gen():
	gen = ''.join(random.choices(string.digits, k=4))
	unchecked_bin = "42"+gen
	r = requests.get(f"https://lookup.binlist.net/{unchecked_bin}")
	try:
		card_scheme = r.json()["scheme"]
	except:
		card_scheme = "None"
	try:
		card_type = r.json()["type"]
	except:
		card_type = "None"
	try:
		card_prepaid = r.json()["prepaid"]
	except:
		card_prepaid = "None"
	try:
		card_country = r.json()["country"]["name"]
	except:
		card_country = "None"
	try:
		card_country_al = r.json()["country"]["alpha2"]
	except:
		card_country_al = "None"
	try:
		card_currency = r.json()["country"]["currency"]
	except:
		card_currency = "None"
	try:
		bank_name = r.json()["bank"]["name"]
	except:
		bank_name = "None"
	try:
		bank_url = r.json()["bank"]["url"]
	except:
		bank_url = "None"
	try:
		bank_phone = r.json()["bank"]["phone"]
	except:
		bank_phone = "None"
	
	print("Bin:",unchecked_bin)
	print("Card Sheme:",card_scheme)
	print("Card Type:",card_type)
	print("Card Prepaid:",card_prepaid)
	print("Card Country Code:",card_country_al)
	print("Card Country:",card_country)
	print("Card Currency:",card_currency)
	print("Bank Name:",bank_name)
	print("Bank Url:",bank_url)
	print("Bank Phone:",bank_phone)
	print("Press enter to go back")
	os.system("pause >nul")

def Mastercard_gen():
	gen = ''.join(random.choices(string.digits, k=4))
	unchecked_bin = "55"+gen
	r = requests.get(f"https://lookup.binlist.net/{unchecked_bin}")
	try:
		card_scheme = r.json()["scheme"]
	except:
		card_scheme = "None"
	try:
		card_type = r.json()["type"]
	except:
		card_type = "None"
	try:
		card_prepaid = r.json()["prepaid"]
	except:
		card_prepaid = "None"
	try:
		card_country = r.json()["country"]["name"]
	except:
		card_country = "None"
	try:
		card_country_al = r.json()["country"]["alpha2"]
	except:
		card_country_al = "None"
	try:
		card_currency = r.json()["country"]["currency"]
	except:
		card_currency = "None"
	try:
		bank_name = r.json()["bank"]["name"]
	except:
		bank_name = "None"
	try:
		bank_url = r.json()["bank"]["url"]
	except:
		bank_url = "None"
	try:
		bank_phone = r.json()["bank"]["phone"]
	except:
		bank_phone = "None"
	
	print("Bin:",unchecked_bin)
	print("Card Sheme:",card_scheme)
	print("Card Type:",card_type)
	print("Card Prepaid:",card_prepaid)
	print("Card Country Code:",card_country_al)
	print("Card Country:",card_country)
	print("Card Currency:",card_currency)
	print("Bank Name:",bank_name)
	print("Bank Url:",bank_url)
	print("Bank Phone:",bank_phone)
	print("Press enter to go back")
	os.system("pause >nul")

def menu():
	banner = f"""
						{Fore.YELLOW} __                 __  
						|__) | |\ |  /\  | /  \ 
						|__) | | \| /~~\ | \__/ 
						{Fore.GREEN}[1]Visa   [2]Mastercard{Fore.RESET} 
		"""
	banner_2 = f"""
						{Fore.YELLOW} __                 __  
						|__) | |\ |  /\  | /  \ 
						|__) | | \| /~~\ | \__/ 
						{Fore.GREEN}[1]OnePerOne  [2]MassGen    {Fore.RESET} 
		"""

	while True:
		try:
			os.system("cls")
			print(banner_2)
			choose = int(input("Your Choice :"))
			if choose == 1:
				os.system("cls")
				print(banner)
				choose_2 = int(input("Your Choice :"))
				if choose_2 == 1:
					Visa_gen()
				elif choose_2 == 2:
					Mastercard_gen()
				else:
					print("Error Choose 1 or 2")
			elif choose == 2:
				os.system("cls")
				print(banner)
				choose_3 = int(input("Your Choice :"))
				if choose_3 == 1:
					Visa_mass_gen()
				elif choose_3 == 2:
					Mastercard_mass_gen()
				else:
					print("Error Choose 1 or 2")
		except ValueError:
			print("Error Choose 1 or 2")

menu()