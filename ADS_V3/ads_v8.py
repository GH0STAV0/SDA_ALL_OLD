import cnf_bvb
import mod_vpn2
import mod_driver
import emoji
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re
from selenium.webdriver import ActionChains
import json
# import pickle


###########global urls_BVB
# urls_BVB=cnf_bvb.random_url
#####################################
# urls_BVB="https://wild-beauty.weebly.com/about.html"
urls_BVB="https://bitcoin-chat-news-and-games.netlify.app/"
# random_display_chose=cnf_bvb.random_display_chose
# width=cnf_bvb.width
# height=cnf_bvb.height
main_url="https://nordcheckout.com/"
user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]


########################################################################################################################################




def clean_up():
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log")
	os.system("rm -rf rm -rf __pycache__/")







	#starting_tasks()
############################################################################################









def lets_play(serv,ops):


	try:
#		print("OPEN DISPLAY  WEB-SITE ...... ",end='',flush=True)
		
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))

	except Exception as error:
		print(str(error))
		exit(0)
	
	print("OPEN AND VISITE WEB-SITE ...... ",end='',flush=True)
	time.sleep(1)
	try:

		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		# driver.set_page_load_timeout(79)
		driver.set_page_load_timeout(79)

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		ads_class(driver)	
	except Exception as error:
		print(str(error))

	print("CHECK THE getLink_button WEB-SITE ...... ",end='')


	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass
	try:
		print("Close Display ...... ",end='')
		display.stop()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass


#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################


def stage_1():
	try:
		#print (urls_BVB)
		os.system("rm -rf /tmp/*") 
		os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		# print(emoji.emojize("Resolution : "+random_display_chose+' :check_mark_button: :alien:'))
		#####TO DO PRINT ONLY THE SYSTEM
		#print(width+"x"+height)
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))




#################################"MAIN STARTING"##############################
def ads_class(driver):
	try:
		driver.get(urls_BVB)
		time.sleep(10)
		driver.get("https://click.a-ads.com/1847449/148128/")
		time.sleep(11)
		print("ok")
		driver.get("https://www.youtube.com/watch?v=q44p18n_C8k")
		time.sleep(11)
		# driver.get(urls_BVB)
		# time.sleep(10)
		driver.execute_script("window.open('');")
		time.sleep(1)
		driver.switch_to.window(driver.window_handles[1])
		time.sleep(1)
		# input('zzzz')
	except Exception as e:
		print(e)
		
def starting_tasks():
	width ,height=cnf_bvb.resolution_func()

	moz_wid="--width="+str(width)
	moz_hig="--height="+str(height)

######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		# os.system("curl -sx socks5://127.0.0.1:9050 ifconfig.co | grep -oP '(?<=Your IP</span>: ).*(?=</span>)'")
		mod_vpn2.fnc_vpn ()
		# mod_vpn.renew_connection()
		display = Display(visible=0, size=(width,height)).start()
		serv,ops=mod_driver.build_driver(width ,height)
		lets_play(serv,ops)
		clean_up()

	except Exception as error:
		print (str(error))





def user_information():
	arry_user_all_info=[]

	arry_usr_info=t00l_.generate_name_add()
	# print(arry_usr_info)
	full_name=arry_usr_info[1].split(" ")
	# print(full_name)
	date_off_birthday=arry_usr_info[2].split("-")


	password =   arry_usr_info[0]
	first_name = full_name[0]
	last_name =  full_name[1]
	dd_birth =   date_off_birthday[0]
	mm_birth =   date_off_birthday[1]
	yy_birth =   date_off_birthday[2]
	post_code = arry_usr_info[3]
	email_usr = arry_usr_info[4]
	arry_user_all_info.extend((email_usr,first_name,last_name,post_code))
	# print(arry_user_all_info)
	# for i in arry_user_all_info:
	# 	print(i)
	return arry_user_all_info #password,first_name,last_name,dd_birth,mm_birth,yy_birth,post_code








def read_the_last_bin():
	# file_bin=open('last_bin' ,'w')
	with open("last_bin") as file_bin:
		lines=file_bin.readlines()
	v_last_bin=lines[0].replace("\n","")
	return v_last_bin

def generate_card_from_bin(bin_number):
	arry_card_bin_info=[]
	# print("GENERATE CARD  OF BIN [ "+bin_number+" ]            ",end='',flush=True)
	print("GENERATE CARD  OF BIN       : ",end='',flush=True)
	time.sleep(1)
	bin_all_card=bin00.generator_bin(bin_number,1)
	# print(bin_all_card)
	arry_bin=bin_all_card[0].split("#")
	card_num=arry_bin[0]
	card_date=arry_bin[1]
	card_date=card_date.replace('|','/')
	card_ccv=arry_bin[2]
	arry_card_bin_info.extend((card_num,card_date,card_ccv))
	print(arry_card_bin_info)
	return arry_card_bin_info





def bin_operation():
	# print("-------------------------------------------------------------------------------------")
	print("GET THE LAST BIN         ",end='',flush=True)
	arry_card_all_info=[]
	the_last_bin=read_the_last_bin()
	time.sleep(1)
	print("   : [  "+the_last_bin+"  ]")
	arry_card_bin_info=generate_card_from_bin(the_last_bin)
	# arry_card_all_info.extend((card_num,card_date,card_ccv))
	# print(card_num,card_date,card_ccv)
	# print(arry_card_bin_info)
	return arry_card_bin_info



def add_to_last_bin():
	l_bin=read_the_last_bin()
	print(l_bin)
	new_bin=int(l_bin)+1
	binani=str(new_bin)
	#################
	with open("last_bin","w") as file_bin:
		file_bin.write(binani)

def save_successed_bin(card_numer):
	# l_bin=read_the_last_bin()
	print(card_numer)
	# new_bin=int(l_bin)+1
	# binani=str(new_bin)
	#################
	with open("succed_bin","a") as file_bin:
		file_bin.write(card_numer+"\n")










os.system("rm -rf /tmp/*")





def main():
	starting_tasks()


if __name__ == '__main__':

	main()


# begaining_loop()