import cnf_bvb
import mod_vpn2
import mod_driver2
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

telrgram_text=[]

###########global urls_BVB
# urls_BVB=cnf_bvb.random_url
#####################################
# urls_BVB="https://wild-beauty.weebly.com/about.html"
url_1="https://bitcoin-chat-news-and-games.netlify.app/index.html"
# url_1="https://cryptocurency-space.netlify.app/index.html"

# url_3="https://elated-nobel-943d26.netlify.app/index.html"
# random_display_chose=cnf_bvb.random_display_chose
# width=cnf_bvb.width
# height=cnf_bvb.height
# main_url="https://nordcheckout.com/"
user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]



random_ads=cnf_bvb.random_ads
url_click_ads="https://click.a-ads.com/1852771/"+random_ads+"/"
########################################################################################################################################




def clean_up():
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log && rm ipifo.json > /dev/null 2>&1")
	os.system("rm -rf rm -rf __pycache__/")
	init_fire()







	#starting_tasks()
############################################################################################









def lets_play(driver) :
	
	time.sleep(1)
	try:
		ads_class(driver)	
	except Exception as error:
		print(str(error))

	# print("CHECK THE getLink_button WEB-SITE ...... ",end='')


	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
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
		os.system("rm /var/log/openvpn/openvpn.log > /dev/null 2>&1")
		#
		time.sleep(5)
		print(" OK !!!")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################


def stage_1():
	try:
		#print (url_1)
		init_fire()
		os.system("rm -rf /tmp/*") 
		os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+url_1+' :check_mark_button: :alien:'))
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")
	except Exception as error:
		print (str(error))




#################################"MAIN STARTING"##############################
def ads_class(driver):
	try:
		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)
		# print(driver.execute_script("return navigator.userAgent;"))
		driver.get(url_1)
		print(" [ "+url_1+" ]")
		time.sleep(10)
		print("CLICK  AND VISITE WEB-SITE [ 2 ]...... ",end='',flush=True)
		# driver.execute_script("window.open('');")
		# time.sleep(3)
		# driver.switch_to.window(driver.window_handles[1])
		driver.get(url_click_ads)
		# print(" [ "+url_2+" ]")
		# print("OPEN AND VISITE WEB-SITE [ 3 ]...... ",end='',flush=True)
		# driver.execute_script("window.open('');")
		# time.sleep(3)
		# driver.switch_to.window(driver.window_handles[2])
		# driver.get(url_3)
		# print(" [ "+url_3+" ]")
		# driver.get("https://elated-nobel-943d26.netlify.app/index.html")
		# driver.get("https://click.a-ads.com/1847449/147974/")
		time.sleep(25)
		# time.sleep(10)
		# time.sleep(1)
		# driver.get(url_1)
		# time.sleep(11)
		# driver.get(url_1)
		# input('zzzz')
	except Exception as e:
		print(e)
		
def starting_tasks():
	width ,height=cnf_bvb.resolution_func()


######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		mod_vpn2.fnc_vpn ()
		display = Display(visible=0, size=(width,height)).start()
		driver=mod_driver2.build_driver(width ,height)
		lets_play(driver)
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