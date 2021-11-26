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
	init_fire()







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
		os.system("ps aux | grep -i geckodriver22 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*")
		os.system("rm /var/log/openvpn/openvpn.log")
		#
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
		init_fire()
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
		driver.get("https://click.a-ads.com/1847449/147974/")
		time.sleep(11)
		print("ok")
		# driver.get("https://www.youtube.com/watch?v=q44p18n_C8k")
		# time.sleep(11)
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
		display = Display(visible=1, size=(width,height)).start()
		serv,ops=mod_driver.build_driver(width ,height)
		lets_play(serv,ops)
		display.stop()
		clean_up()

	except Exception as error:
		print (str(error))



os.system("rm -rf /tmp/*")





def main():
	starting_tasks()


if __name__ == '__main__':

	main()


# begaining_loop()