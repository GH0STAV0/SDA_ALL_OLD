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
#url_1="https://bitcoin-chat-news-and-games.netlify.app/index.html"
# url_1="https://cryptocurency-space.netlify.app/index.html"
# url_1="https://brave-brown-e09c81.netlify.app/"
# url_1="https://serene-keller-a6f116.netlify.app/index.html"
# https://elated-nobel-943d26.netlify.app/index.html"
# url_1="https://jovial-villani-44d38c.netlify.app/index.html"
# url_1="https://dark-market-crypto.tk/index.html"
# url_1="http://free-coin.nichesite.org/index.html"
# url_1="http://romanian.ueuo.com/index.html"
# url_1="http://crypto-world.is-great.org/index.html"
url_1=cnf_bvb.url_1
print (url_1)
url_site_2=cnf_bvb.url_site_4
second_2_visit=cnf_bvb.second_2_visit

# url_3="https://elated-nobel-943d26.netlify.app/index.html"
# random_display_chose=cnf_bvb.random_display_chose
# width=cnf_bvb.width
# height=cnf_bvb.height
# main_url="https://nordcheckout.com/"
user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]

random_ads=""

# random_ads=cnf_bvb.random_ads
url_click_ads="https://click.a-ads.com/1859747/"+random_ads+"/"
########################################################################################################################################
##############################################################
l05_00='l05_00'
def append_to_l0g(text_add):
	with open(l05_00,'a') as fw:
		fw.write(text_add+"\n")
	# 	# for i in all_vpn_config_file:

##############################################################


def read_current_l0g():
	final_msg=''
	with open(l05_00,'r') as file:
		lines = file.readlines()
		for i in lines:
			final_msg=final_msg + i
	return final_msg
############################################################################




def clean_up():
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log && rm ipifo.json > /dev/null 2>&1")
	os.system("rm -rf rm -rf __pycache__/ && echo -e 'nameserver 8.8.8.8\nnameserver 8.8.4.4' >  /etc/resolv.conf")
	os.system("service openvpn restart")

	init_fire()


def stage_1():
	try:
		#print (url_1)
		init_fire()
		os.system("rm -rf /tmp/* && rm l05_00") 
		os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+url_1+' :check_mark_button: :alien:'))
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("service openvpn restart")
		time.sleep(5)
	except Exception as error:
		print (str(error))









	#starting_tasks()
############################################################################################

#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver_15 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver22 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*")
		os.system("rm /var/log/openvpn/openvpn.log > /dev/null 2>&1")
		#
		time.sleep(5)
		print(" OK !!!")
	except:
		print(" NO  some_Error init_fire")

def lets_play(driver) :
	time.sleep(1)
	try:
		ads_class(driver)
	except Exception as error:
		print(str(error))



###################################################################################################

	lines=read_current_l0g()
	cnf_bvb.send_msg(str(lines))
	# print("CHECK THE getLink_button WEB-SITE ...... ",end='')

###################################################################################################

	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass


###################################################################################################



#################################"MAIN STARTING"##############################
def ads_class(driver):
	try:
		###############################################################################################
		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)
		# print(driver.execute_script("return navigator.userAgent;"))
		# cnf_bvb.send_msg("oooooooooooooooooooo")
		driver.get(url_1)
		# input("pa")
		print(" [ "+url_1+" ]")
		# cnf_bvb.send_msg(meddas)
		append_to_l0g("CLICK  AND VISITE WEB-SITE   [ "+url_1+" ] OK")
		# time.sleep(20)
		# driver.refresh()
		time.sleep(15)
		print("CLICK  AND VISITE WEB-SITE [ 2 ]...... ",end='',flush=True)
		# getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'rightbox')))
		# print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		# action = ActionChains(driver)
		# action.move_to_element(getLink_button)# .perform()
		# time.sleep(25)
		# getLink_button.click()
		#print("CLICK  AND VISITE WEB-SITE [ 2 ]...... ",end='',flush=True)
		# driver.get(url_click_ads)
		# input("")
		#//*[@id="Blog1_blog-pager-older-link"]
		# //*[@id="post-body-4310463428394459903"]/div[1]
		driver.get(second_2_visit)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="post-body-2346695118421539823"]'))))
		print("UUUUU")
		time.sleep(5)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'yass-search-box'))))
		time.sleep(5)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
		# getLink_button.send_keys(Keys.TAB*8)
		#yass-search-box
		time.sleep(5)
		getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Blog1_blog-pager-older-link"]/i')))
		# search-wrapper
		getLink_button.click()
		driver.execute_script("window.scrollTo(0, 0);window.scrollTo(0, 0);")


		# cnf_bvb.send_msg("oooooooooooooooooooo")
		append_to_l0g("VISITE WEB-SITE [ 2 ] : [ "+second_2_visit+"]  OK")


		time.sleep(8)

	except Exception as e:
		print(e)
	driver.delete_all_cookies()



def starting_tasks():
	width ,height=cnf_bvb.resolution_func()


######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		mod_vpn2.fnc_vpn ()
		# cnf_bvb.alias_send_msg_2()
		# os.environ['DISPLAY']
		visible_v=cnf_bvb.visible_v
		display = Display(visible=visible_v, size=(width,height)).start()
		driver=mod_driver2.build_driver(width ,height)
		lets_play(driver)
		display.stop()
		

	except Exception as error:
		print (str(error))
	clean_up()



os.system("rm -rf /tmp/*")





def main():
	starting_tasks()
	# append_to_l0g("text_add")


if __name__ == '__main__':

	main()


# begaining_loop()
