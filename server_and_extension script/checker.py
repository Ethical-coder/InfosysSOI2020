import re,requests,json
from PhishTank import phish_https_checker as phish
from bs4 import BeautifulSoup
import subprocess




class Tester:
	def __init__(self,url):
		self.url=url
	

	def ml(self,url):
		command="python3 ML_response.py -u "+url
		predict=str(subprocess.check_output(command,shell=True))
		if("bad" in predict):
			return(0)
		else:
			return(1)

	#will be invoked when popup button is pressed
	def crawler(self):
		html_data=requests.get(self.url)
		html_data=html_data.text
		links=list()
		soup=BeautifulSoup(html_data, "html.parser")
		for a in soup.findAll("a"):
			try:
				link=a.attrs.get("href")
			except:
				link=[]
				print("exception")

			if(link!= None and "http://"  in link and self.url not in link):
				links.append(link)
		return links,html_data

	def phishTank(self,url):
		tank=phish.phishTank(url)
		if(tank.check()==True):
			return 1
		else:
			return 0

	def check_for_downloadables(self,url):
		slash=url.split("/")
		if ".exe" in  slash[-1].lower() or ".zip" in slash[-1].lower():
			return 1
		elif "exe." in slash[-1].lower():
			return -1
		else:
			return 0

	def scan(self):
		check=self.check_for_downloadables(self.url)
		if(self.phishTank(self.url)==1):
			return "Phishing Website Detected"
		elif check!=0:
			if check==1:
				return "You are downloading files that may be suspiscious be aware"
			elif check==-1:
				return "There may be Left To Right pointer used in naming"
		elif(self.ip_checker(self.url)!="0"):
			return "This website may be malicious as it uses IP address not domain"		

		elif(self.ml(self.url[7:])):
			return "Url looks malicious"
		 
		else:
			return "safe"



	def fullScan(self):
		links,html=self.crawler()
		if_ip=self.ip_checker(html)
		if(len(links)!=0):
			result=0
			check1=0
			check_1=0
			if(self.phishTank(self.url)==1):
				return "Phishing Website Detected"
			for i in links:
				check=self.check_for_downloadables(i)
				if(check==1):
					check1=1
				if(check==-1):
					check_1=1
				if(self.phishTank(i)==1):
					return "Phishing Website Detected"
				if(self.ml(i[7:])==0):
					result+=1
			if(check1==1):
				return "This page contains links for downloadable be aware"
			elif(check_1==1):
				return "Downloadable in this page may be spoofing Left to Right pointer"
			elif(if_ip!="0"):
				return if_ip
			elif(result!=0):
				return "There is "+str(result*100/(len(links)))+"% chances that you will open a Phishing website"
			else:
				return "safe"
		else:
			return "safe"


	def ip_checker(self,html):
		regex ='''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
		reg="(?:http://)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
		ips=re.findall(reg,html)
		ip_address=list()
		for ip in ips:
			if(re.search(regex,ip)):
				ip_address.append(ip)
		if(len(ip_address)!=0):
			return("Browser may be hooked some ip address")
		return "0"




