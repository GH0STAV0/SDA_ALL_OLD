import cnf_bvb
import mod_vpn2
import mod_driver
import drive_md
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
# urls_BVB="https://bitcoin-chat-news-and-games.netlify.app/"
urls_BVB="https://indab0x.nl.eu.org/"
# random_display_chose=cnf_bvb.random_display_chose
# width=cnf_bvb.width
# height=cnf_bvb.height
main_url="https://nordcheckout.com/"
user_agent = cnf_bvb.user_agent
try:
	sys_use_agent=re.findall('\(.*?\)',user_agent)[0]
	
except Exception as e:
	sys_use_agent="eereee"

file_list_1='succes_2'
########################################################################################################################################


# print(file_list_1)
# input("")
def clean_up():
	try:
		os.system("rm -rf /tmp/*")
		os.system("rm -rf rm -rf __pycache__/")
		# os.system("rm geckodriver.log")

	except:
		pass






	#starting_tasks()
############################################################################################



###############################################################################################
def save_succed(logg):
	with open("Wsucced_nord_xxxx",'a') as fw:
		fw.write(logg[0]+":"+logg[1]+"\n")

def save_succed_final(logg):
	with open("ready_Wsucced_nord_xxxx",'a') as fw:
		fw.write(logg+"\n")






def lets_play(l0g):
	# input("lets play")
	# print(l0g)


	try:
		width ,height=cnf_bvb.resolution_func()
#		print("OPEN DISPLAY  WEB-SITE ...... ",end='',flush=True)
# size=(width,height)
		display = Display(visible=0,size=(width,height)).start()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))

	except Exception as error:
		print(str(error))
		exit(0)
	
	print("OPEN AND VISITE WEB-SITE ...... ",end='',flush=True)
	time.sleep(1)
	try:
		sz=height+","+width
		# print(sz)

		driver = drive_md.build_driver(sz)
		driver.maximize_window()
		# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		# driver.set_page_load_timeout(79)
		# driver.set_page_load_timeout(79)
		ads_class(driver,l0g)
		
	except Exception as error:
		print(str(error))
		# input('')

	# print("CHECK THE getLink_button WEB-SITE ...... ",end='')


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
		os.system("ps aux | grep -i chrome | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
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
		# os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		# print(emoji.emojize("Resolution : "+random_display_chose+' :check_mark_button: :alien:'))
		#####TO DO PRINT ONLY THE SYSTEM
		#print(width+"x"+height)
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))

###############################################################################################


	



#################################"MAIN STARTING"##############################
def ads_class(driver,l0g):
	action = ActionChains(driver)

	# /html/body/div/div[2]/div
	try:
		driver.get(urls_BVB)
		# print(l0g[0])
		# driver.get("https://webglreport.com/")
		time.sleep(3)
		# driver.get("https://indab0x.nl.eu.org/")
		# driver.get("https://nordaccount.com/")
		# # time.sleep(8)
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/div[3]/div/iframe')))
		# SUCCESS_MSG_BUTTON.send_keys(l0g[0],Keys.ENTER)
		action.move_to_element(SUCCESS_MSG_BUTTON)
		action.perform()
		print("peform")
		time.sleep(7)
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="address-box-normal"]/div[3]/button')))
		# SUCCESS_MSG_BUTTON.send_keys(l0g[0],Keys.ENTER)
		action.move_to_element(SUCCESS_MSG_BUTTON)
		action.perform()
		time.sleep(5)
		try:

			iframes = driver.find_elements_by_xpath("//iframe")
			# print(str(iframes))
			driver.switch_to.frame(0)
			time.sleep(2)
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/span')))
			print("peform2 : "+SUCCESS_MSG_BUTTON.text)
			cnf_bvb.alias_send_msg(SUCCESS_MSG_BUTTON.text)
			time.sleep(7)
			driver.switch_to.parent_frame()
		except:
			print("noooo")
			time.sleep(7)
			pass
		# SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="address-box-normal"]/div[3]/button')))
		# SUCCESS_MSG_BUTTON.click()
		time.sleep(7)
		driver.refresh()
		time.sleep(7)

		# //*[@id="address-box-normal"]/div[3]/button
		# # time.sleep(8)
		# # input("")
		# SUCCESS_MSG_BUTTON.send_keys(l0g[1],Keys.ENTER)
		# # # driver.get(urls_BVB)
		# # # time.sleep(10)
		# # driver.execute_script("window.open('');")
		# # time.sleep(1)
		# # driver.switch_to.window(driver.window_handles[1])
		# # time.sleep(1)
		# check_login(driver,l0g)
		# # input('zzzz')
	except Exception as e:
		print(e)
		
def starting_tasks(l0g):
	width ,height=cnf_bvb.resolution_func()
	moz_wid="--width="+str(width)
	moz_hig="--height="+str(height)

######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		# print(l0g)
		# os.system("curl -sx socks5://127.0.0.1:9050 ifconfig.co | grep -oP '(?<=Your IP</span>: ).*(?=</span>)'")
		mod_vpn2.fnc_vpn ()
		# mod_vpn.renew_connection()
		# serv,ops=mod_driver.build_driver(width ,height)
		lets_play(l0g)
		clean_up()
		

	except Exception as error:
		print (str(error))


def read_current_list_vpn():
	with open(file_list_1,'r') as file:
		lines = file.readlines()
	return lines







def save_successed_bin(card_numer):
	# l_bin=read_the_last_bin()
	print(card_numer)
	# new_bin=int(l_bin)+1
	# binani=str(new_bin)
	#################
	with open("succed_bin","a") as file_bin:
		file_bin.write(card_numer+"\n")
















def main():
	os.system("rm -rf /tmp/.*")
	# login_arry=read_current_list_vpn()
	starting_tasks("l0g:l0g")
	# print(login_arry)
	# # input("")
	# for i in login_arry:
	# 	logg0=i.replace("\n","")
	# 	logg0=logg0.replace(" ","")
	# 	print(i)
	# 	logg=logg0.split("|")
	# 	logg2=logg[0].split(":")
	# 	print(logg2)
	# 	# input("")
	# 	starting_tasks(logg2)


if __name__ == '__main__':

	main()


# begaining_loop()