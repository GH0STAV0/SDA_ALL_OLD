import smtplib
import time
import imaplib
import email
import bs4
import re
from bs4 import BeautifulSoup
from faker import Faker
import datetime
import random
import string
import subprocess as sp
from urllib.parse import quote
imaplib._MAXLINE = 80000
def save_it(finall):
	with open('shift_url2','a') as f:
	        f.write(finall+"\n")
	        f.close()

activation=[]
	# conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	# gmail_user = 'king00binz@gmail.com'
	# gmail_pwd = 'agoon007'
def connection_imap():

	conn = imaplib.IMAP4_SSL("outlook.office365.com", 993)
	gmail_user = 'disp0s0@outlook.com'
	gmail_pwd = 'baba123A*'
	conn.login(gmail_user, gmail_pwd)
	return conn



def gather_acces(emmail):
	print("search for email")
	magic_formul='(TO "xxxxx" SUBJECT "Verify Email Address")'
	magic_formul=magic_formul.replace("xxxxx",emmail)
	mail=connection_imap()
	mail.select('INBOX')
	status, data = mail.search(None, magic_formul)
	ids = data[0]
	unread_msg_nums = data[0].split()
	print (" [ ",len(unread_msg_nums)," ]",flush=True,end= " ")
	if len(unread_msg_nums) == 0 :
		print("NOTHING FOUND")
		mail.close()
		
		time.sleep(8)
		gather_acces(emmail)


	for emailid in unread_msg_nums:
		resp3, data3 = mail.uid("fetch", emailid,"(RFC822)" )#mail.uid('search', None, "ALL")
		result, data = mail.fetch(emailid, "(RFC822)")
		email_body = data[0][1].decode("utf-8")
		za_body_mail = email.message_from_string(email_body)
		iii=za_body_mail.get_content_type()
		ohh=za_body_mail.get_payload()
		#charset = za_body_mail.get_content_charset()
		html0 = za_body_mail.get_payload()#, str(charset), "ignore"#.encode('utf8', 'replace')
		# print(iii)
		# input("")
		if za_body_mail.is_multipart():
			for part in za_body_mail.get_payload():
				# print(part.get_content_type())
				if part.get_content_type() == 'text/plain' :
					# print(part.get_content_type())
					# html0=part.get_payload()
					payload=part.get_payload(decode=True).decode(part.get_content_charset('utf-8'))
					# print(payload)
		else:
			print(za_body_mail.get_payload())
		# print(za_body_mail.get_payload()[0])
		# print(payload)
		# input("")
		# linkess=re.findall(u'"(https:.*?)"' , payload)
		urls = re.findall(r'https://www.publish0x.com/email/verify.*', payload)
		# print(', '.join(urls))


		# input("")
		activation=urls[0]
		print(activation)
		# input("")

		# soup = BeautifulSoup(html0, 'lxml')
		# # print(soup)
		# jo=soup.find_all('a')
		# input("")
		# print(jo)
		# for h2 in soup.find_all('a'):
		# 	shit=h2.get('href')
		# 	print(h2)
		# 	print(shit)
		# 	all_links=shit.split('\n')
		# 	print(all_links)
		# 	shit_valid=all_links[0]
		# 	print(shit_valid)
		# 	if "https://www.publish0x.com/email=" in shit_valid :
		# 		activation.append(shit)
		# 		print(shit)
		mail.close()
	return activation

#gather_acces("alicia20epxlgoodman@biglose3.ml")
#print(link.get('href'))

#read_uniq()
#gather_acces("john21peolg6brown@multi-service-seller.tk")
# emmail="aaron387ifowler@dark-market-crypto.tk"
# gather_acces(emmail)