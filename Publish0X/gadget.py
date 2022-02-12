import random,datetime,string , os ,time ,subprocess 
from selenium import webdriver
from faker_e164.providers import E164Provider
from faker import Faker
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display
import requests
import io
from pydub import AudioSegment
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from stem import Signal
from stem.control import Controller


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
######################################################
#RT2
######################################################
def pinto (TEXT_,f):
	if f == "GREEN12" :
		print(bcolors.BOLD + bcolors.OKGREEN + TEXT_+"" ,end="\n"+ bcolors.ENDC)
	if f == "GREEN11" :
		print(bcolors.BOLD + bcolors.OKGREEN + TEXT_+"" ,end=""+ bcolors.ENDC,flush=True)
	if f == "BLUE_BLOOD_END":
		print(bcolors.BOLD + bcolors.OKBLUE + TEXT_+"" ,end="\n"+ bcolors.ENDC)
	if f== "ERROR12":
		print(bcolors.BOLD + bcolors.FAIL + TEXT_+"" ,end="\n"+bcolors.ENDC)
	if f== "ERROR11":
		print(bcolors.BOLD + bcolors.FAIL + TEXT_+"" ,end=""+bcolors.ENDC)
	if f == "NTX":
		print(TEXT_+"" ,end="\n"+ bcolors.ENDC)
	if f== "BR":
		print(bcolors.BOLD + bcolors.OKBLUE + TEXT_+"" ,end="\n"+bcolors.ENDC)
	if f == "RT2" :
		print(bcolors.BOLD + bcolors.FAIL + TEXT_+"" ,end="\n"+ bcolors.ENDC)




############################################################################################################
############################################################################################################

Binarry="/root/firefox-sdk/bin/firefox-bin"
#path_profile="/root/.mozilla/firefox/iwuytxe6.shit"
gecko_path="/usr/bin/geckodriver13"
global arr_info
arr_info=[]
############################################################################################################
############################################################################################################




def sstart():
	#new_prof()
	#input()
	#proxy ="98.172.253.135"#98.172.253.135
	#port=1080
	capabilities = webdriver.DesiredCapabilities().FIREFOX
	capabilities["marionette"] = True
	#profile = webdriver.FirefoxProfile(path_profile)
	binary = FirefoxBinary(Binarry)
	driver = webdriver.Firefox(firefox_binary=binary , capabilities=capabilities , executable_path=gecko_path)
	#driver = webdriver.Firefox(firefox_binary=binary , capabilities=capabilities , firefox_profile=profile , executable_path=gecko_path)

	return driver


reasonableCharacters = (string.digits + string.ascii_letters )
def password0(minimum=5, maximum=6):
    return ''.join(
        random.choice(reasonableCharacters) for x in range(
            random.randint(minimum, maximum)
        )
    )

def beep():
    print ("\a");print ("\a")
    print ("\a")

def generated():
	try:
		fake = Faker('en_US')
		fake.add_provider(E164Provider)
		nna=fake.name()
		first_name=fake.first_name()
		last_name=fake.last_name()
		phon_number =fake.e164(region_code="US", valid=True, possible=True)
		company_name=fake.bs() 
		#street_address=fake.street_address()
		address_=fake.address()
		tt=address_.split(",")
		street_address=tt[0].replace("\n"," ")
		street_address=street_address
		a_address_= address_.split()
		zip_code=a_address_[-1]
		city_0=tt[0].split("\n")
		city_1=city_0[1]
		city_=""
		add=city_1
		for i in add.split() :
			if i.isalpha() :
				city_+=i+" "

		street0_=city_0[0]
		dom=random.randint(1,len(domains))
		timestamp = datetime.datetime.now()
		vary=password0(4,4)
		t =  str(timestamp.second)+vary
		email_ja=nna.replace(" ",t)  
		email_do="g3intaya+"+email_ja+domains[dom-1]
		email_do=email_do.lower()
		if ".@" in email_do:
			email_do=email_do.replace(".@","@")
		#arr_info.append(first_name)
		arr_info.extend([first_name,last_name,phon_number,company_name,email_do ,street_address,zip_code,city_,street0_ ])
		print(arr_info)
		#return first_name,last_name,phon_number,company_name,email_do ,street_address,zip_code,city_,street0_
		return arr_info
	except:
		generated()

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath('//*[@id="companyName"]')
    except :
        return False
    return True






def save_it(mail):
	with open('email__','a') as f:
	        f.write(mail+"\n")
	        f.close()
def save_it2(mail):
	with open('email__2','a') as f:
	        f.write(mail+"\n")
	        f.close()


def new_prof():
	#os.system("pkill openvpn && pkill xterm  && pkill firefox")
	#lines = open('tccp').read().splitlines()
	#myline =random.choice(lines)
	#config_vpn='openvpn /root/pn/ovpn_tcp/'+myline
	#print(config_vpn)
	#os.system("xterm -e "+config_vpn+" &")


	print("C R E A T I N G    P R O F I L E  : " ,end="",flush=True)
	remove_prof="rm -rf /root/.mozilla/firefox/iwuytxe6.shit"
	extract_prof="tar xf iwuytxe6.shit.tar.gz -C /root/.mozilla/firefox"
	empty_tmp="rm -rf /tmp/*"

	try:
		subprocess.Popen(remove_prof, shell=True)
		time.sleep(1)
		subprocess.Popen(empty_tmp, shell=True)
	except:
		pass
	try:
		subprocess.Popen(extract_prof, shell=True)
		time.sleep(1)
		print("  O  K  ")
	except:
		pass

