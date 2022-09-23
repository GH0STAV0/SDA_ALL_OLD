import random , os ,requests
import json
import socket
import urllib.parse
import emoji , os
import  u_a

os.system("clear && sleep 1") 

print("#######################***  CONFIGURATION ; ) ****############################\n")

vpn_type="V"
hostname_os=socket.getfqdn()
visible_v=0

if "LOOKE3" in hostname_os:
	# print(hostname_os)
	print("HOST    NAME        : [ "+hostname_os+" ]")
	print("VPN     TYPE        : [ "+vpn_type+" ]")
	visible_v=1


total_l0g=[]
vversion="SITE_5.0 io/IMG= xm0uray-site_5 | VANISH +NEW+ renew FIX 1.1S"
telegram_tokens_bot=["0","5036803152:AAGs0ES1OmEdy86MNJDp7mp19BB5IQhcVHU","5099462819:AAEndTxvXaSqBQ6E_EpiCN02a81ROGPMgr0","5001651751:AAGzzbUfJXWHZz-FKJyLSUxzg-JiRMO5v-Q","5041058138:AAFRher-cMwnRI476iW24tT6Kt8lvC0bmLc","5051743922:AAEOHJTRzv2WIxZ8bR-VrVYNA6io6qB1Ltw"]


def ap_2_l0g(gms):
	total_l0g.append(gms)


urls=["https://30m30m.nl.eu.org/"]
# urls=["https://indab0x.nl.eu.org/"]
# 30m30m.nl.eu.org
# 30m30m.nl.eu.org
# urls=["https://disp0s0.nl.eu.org/","https://indab0x.nl.eu.org/"]
# 

url_6="https://www.bit-plazza.nl.eu.org/?m=0"


def set_url():
	random_url=random.choice(urls)
	return random_url

url_1=set_url()

url_site_2="https://www.iblogger.nl.eu.org/index.html"
url_2=url_1.replace("https://","")
url_2=url_2.replace("/index.html","")
# url_site_2
url_site_4=url_site_2.replace("https://","")
url_site_4=url_site_4.replace("/2021/12/bash-you-can-get-hostname-of-node-in-at.html","")
# N= norrd

second_2_visit='https://www.iblogger.nl.eu.org/2022/01/bash-for-loop-examples-what-is-bash-for.html'

parssed_url_1=urllib.parse.urlparse(url_1).netloc
parssed_url_2=urllib.parse.urlparse(url_site_2).netloc
# print(url_1)
print("U R L   TO   VISIT  : [ "+url_1+" ]")




def send_msg_dock(text):
	msg_telegram="[ "+hostname_os +" ]"+text
	token = "5261450305:AAEROP9j6569RV4rKsE_tStXCdnLSX7Gz1Y"
	# chat_id = "-643828126" L0G_NICH
	chat_id = "-615987943"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 
	results = requests.get(url_req)
	print(results.json())
	


def p0st_phase():
	host_id="test"
	send_msg_dock("text")



u_a_count=str(u_a.u_a_count)
# print(str(len(user_agent_list)))
##############################################################################################
print("USER AGENT COUNTING : [ "+u_a_count+" ]")

def hostname_os_val():
	hostname_os=socket.getfqdn()
	# print(hostname_os[-1])
	b_v=hostname_os[-1]
	return b_v



def get_tokens():
	bot_name=hostname_os_val()
	# print(bot_name)
	tokens=telegram_tokens_bot[5]
	if "1" in bot_name:
		tokens=telegram_tokens_bot[1]
	if "2" in bot_name:
		tokens=telegram_tokens_bot[2]
	if "3" in bot_name:
		tokens=telegram_tokens_bot[3]
	if "4" in bot_name:
		tokens=telegram_tokens_bot[4]
	if "5" in bot_name:
		tokens=telegram_tokens_bot[5]
	# print(tokens)
	# print("TELEGRAM   TOKENS   : [ "+tokens+" ]")
	return tokens
# hostname_os_val()
# get_tokens()check_mark_button

def alias_send_msg(text):
	pol=emoji.emojize(""':man_genie:')
	mp=emoji.emojize(" "'  :dizzy:'+"[ "+hostname_os +" ] "':dizzy:'+" \n"''+"  [ "+vversion+" ] "'')
	msg_telegram=mp+" \n"+text+" ] \n "+pol+" [ "+parssed_url_1+" ] \n "+pol+"[ "+parssed_url_2+" ] "
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	token=get_tokens()
	# token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	chat_id = "-615987943"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 

	results = requests.get(url_req)
	# print(results.json())


##############################################################################################
def alias_send_msg_2():
	mmgg.emojize(" "' :ghost: :alien:')
	# mmgg=""
	for x in total_l0g :
		mmgg=mmgg+x+"\n"
		pass

	msg_telegram="[ "+hostname_os +" ] [ "+vversion+" ] [ "+mmgg+" ] [ "+parssed_url_1+" ] [ "+parssed_url_2+" ] [ 000000 OK ]"
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	token=get_tokens()
	# token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	chat_id = "-615987943"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 

	results = requests.get(url_req)
	# print(results.json())


##############################################################################################

mp=emoji.emojize("STARTING Ok "':alien:')
alias_send_msg(mp)
















l05_00='l05_00'
def append_to_l0g(text_add):
	with open(l05_00,'a') as fw:
		fw.write(text_add+"\n")
	# 	# for i in all_vpn_config_file:

##############################################################







#p_vpn_g="/root/install_add/moya/yserverListTCP/"
#
############################# VPN ##################################""



# ads=['148554','148477','148709','143423','146817','147629','147257','148786','146991','148787','148066','148643','148283','144375','148279','144442','148555','148264','148804','148556','147277','147415','146209','148523','148680','144002','148540','147710','144323','144498','148758','144525','148263','146622','142824','146831','147535','148510','148600','145992','148482','139001','148628','148784','148685','147791','148059','144604','147966','146160','139480','148498','148760','148657','148721','148577','146708','148761','148762','139705','146145','143247','148717','148677','148539','148749','145585','148476','148522','147370','139134','148471','148759','148061','147081','145096','148242']

# random_ads=random.choice(ads)



def send_msg(text):

	msg_telegram="[ "+hostname_os +" ]"+text+" [ "+url_2+" ]"
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	chat_id = "-609247805"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 

	results = requests.get(url_req)
	# print(results.json())



def testt():
	print("this is imported def")


def iip ():
	try:
		# pass
		#sourceee="ipecho.net"
		os.system("curl -s ipinfo.io > ipifo.json")
		f = open ('ipifo.json', "r")
		data = json.loads(f.read())
		#r = requests.get(sourceee)
		ip=data['ip']
		tz=data['timezone']
		loc=data['loc']
		country=data['country']
		# print(" [ "+ip + " ] ["+tz+" ] [ "+loc+" ]")
	except Exception as e:
		ip=""
		tz="OKEurope/Paris"
		loc=""
	return ip,tz ,loc
########################################################################################################################################


# pwd = os.path.dirname(os.path.realpath( __file__ ))
pwd="/root/VPN"
p_vpn_g=pwd+"/CHEAP_VPN/"
file_vpn_dead=pwd+"/DEAD_CONFIG_TCP/"
# 	p_vpn_g=pwd+"/N0RD/WORKING_CONFIG/"
p_vpn_dead=pwd+"/N0RD/DEAD_CONFIG_TCP/"
#CHEAP_VPN

def randomm():
	random_vpn=random.choice(os.listdir(p_vpn_g))
	final_vpn=p_vpn_g+random_vpn
	return final_vpn,random_vpn


#final_vpn,random_vpn=randomm()


extension_path=pwd+"/src/canvasblocker44b.xpi"
# extension_path_ublock=pwd+"/src/uBlock0_1.36.2.firefox.xpi"
#uBlock0.firefox
extension_path_ublock=pwd+"/src/uBlock0.firefox.xpi"

#######################  DISPLAY ##############################
def resolution_func():

	display_aary=['1366x768','2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x1024','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','2160x4096','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x1024','1920x1080','1920x1080','1366x768','1920x1080' ,'1280x720','2560x1440','1080x1920','1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1440x2560','1440x2560' ,'1080x1920','1080x1920','1080x1920' ,'1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920' ,'1080x1920','1080x1920','1080x1920' ,'1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','1920x1080','1920x1080','1280x768','1440x1440','1280x720','1280x720',  '1080x1920', '1080x1920','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x1024','1280x1024','2048x1536' ,'1200x1920','1280x720' ,'1200x1920','1200x1920','1280x1024','1920x1080','1920x1080'  ,'2048x1536','1280x1024' ,'1280x1024','1280x1024','1280x1024' ,'1536x2048' ,'1080x1920','1080x1920','1280x1024','1280x1024','1280x1024','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x1024','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','1080x1920','1125x2436','1125x2436','1242x2688','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']

	random_display_chose=random.choice(display_aary)

	display=random_display_chose.split(sep="x")
	width=display[0]
	height=display[1]
	return width ,height


#########      URLS     ######################

main_domain_BVB="http://bc.vc/"
urls_GH=['MsO5TcT','nrfXdb6','fl5a8H','JvPIhd6','wt0nn5','lwF59F','32NMGr','dfa2gk','UN5Mr5','GycAq7a','movOJG','ec49nF','FuqOZ0','4AFNi6','u6dgi3','xR8ieVb','zYieggh','2jqR5zo','z2UCLn','V1iocU']

urls_BVB=['Uu2MbdT','Uu2MbdT','Uu2MbdT']
#http://bc.vc/Uu2MbdT http://bc.vc/Uu2MbdT
# urls_BVB=['a1yUjT4','9d7ionu','k9bRz5y']
# random_url=main_domain_BVB+random.choice(urls_BVB)
# user_agent = random.choice(user_agent_list)
user_agent = u_a.u_a_count



##URLS 
#firefox_options_binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox"
# new_driver_path = '/usr/bin/geckodriver_15'
# new_driver_path = '/usr/bin/geckodriver13'
new_driver_path = '/usr/bin/geckodriver22'
# new_binary_path = '/root/EXTRA/firefox-53.0b9/firefox/firefox'

########################
#new_binary_path = '/root/EXTRAT/firefox/firefox'
#new_binary_path = '/root/EXTRA/firefox-53.0b9/firefox/firefox'
# new_driver_path = '/usr/bin/geckodriver222'

# new_binary_path = '/root/EXTRA/firefox-53.0b8/firefox/firefox'
# new_binary_path = '/root/EXTRA/firefox-49.0b9/firefox/firefox'

# new_binary_path = '/root/EXTRA/firefox-56.0.1/firefox/firefox'
# new_binary_path = '/root/EXTRA/firefox-57.0.1/firefox/firefox'
# new_binary_path = '/root/EXTRA/firefox-58.0.1/firefox/firefox'
# new_binary_path = '/root/EXTRA/firefox-59.0b9/firefox/firefox'

def random_fir():
	# firefox_version=['49.0b9']
	firefox_version=['57.0.1','58.0.1','59.0.1','60.0.1esr']
	random_firefox_version=random.choice(firefox_version)
	text_add="[ "+random_firefox_version +" ]"
	print(text_add)
	# append_to_l0g(text_add)
	new_binary_path="/root/EXTRAT/firefox-"+random_firefox_version+"/firefox/firefox"
	return new_binary_path ,text_add






# send_msg("text")
print("\n###############################################################################")
