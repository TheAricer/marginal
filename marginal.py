#author:Arice
import argparse
import re
import requests
from concurrent.futures import ThreadPoolExecutor

def para_options():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u",help = "input your domain or ip")
	parser.add_argument("-k",help = "input your Keys！ep：->> inurl:action or action")
	args = parser.parse_args()
	return args

def C(ip_u):
	ipc = []
	for i in range(0,255):
		ipc.append(ip_u[0:ip_u.rfind('.')+1]+str(i))
	return ipc

def regular(url,page):
	headers = {
"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}
	req = requests.get(url, headers = headers, timeout = 4)
	content = req.text
	patt = re.compile('<li class="b_algo"><h2><a target="_blank" href="(.*?)" h=".*?">(.*?)</a></h2>')
	Values = re.findall(patt,content)
	for V in Values:
		site = str(V[0])
		if site not in page:
			print('\t\033[1;36m{} \033[0m----{}'.format(site,V[1]))
			page.append(site)

def site(site):
	page = []
	if para_options().k == None:
		for j in range(0,6):
			url = 'https://www.bing.com/search?q=site:'+site+'&first='+str(j)+'0'
			regular(url,page)
			
	else:	
		for j in range(0,6):
			url = 'https://www.bing.com/search?q=site:'+site+'+'+para_options().k+'&first='+str(j)+'0'
			regular(url,page)
			

def IP(ip):
	page = []
	if para_options().k == None:
		print(ip+':')
		for j in range(0,6):
			url = 'https://www.bing.com/search?q=ip:'+ip+'&first='+str(j)+'0'
			regular(url,page)
	else:
		print(ip+':')
		for j in range(0,6):
			url = 'https://www.bing.com/search?q=ip:'+ip+'+'+para_options().k+'&first='+str(j)+'0'
			regular(url,page)
			
def main():
	if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', para_options().u):
		with ThreadPoolExecutor(5) as executor:
			executor.map(IP, C(para_options().u))
	elif re.match(r'.*?\.\D*$', para_options().u):
		site(para_options().u)
	else:
		print('Input error, please try retyping your instruction!')
def bing(K):
	print('testest')
	print(K)

if __name__ == '__main__':
	if para_options().u:
		main()