import cnf_bvb
import sql_gc_get

# import mod_vpn2
import mod_driver2
import emoji
import gc_ac__sql
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
# xamiramogdan hghjghj
telrgram_text=[]
# email="azfounmondilla"111mmm
# email="jilalydillaly"
# email="abouichrine"
# email="almidaopo"
# email="don0mar0l0k0"
# email="abedrahman0x"
# email="boudabkafaycel"
# email="caldinomajbri"iiiop
# email=gc_ac__sql.get_gc_account()



email=cnf_bvb.g00g_acc
cnf_bvb.extact_gc_profile()
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""
# email=""

# email="don0mar0l0k0"
# email="xamiramogdan"
# email="xamiramogdan"
# email="xamiramogdan"
# email="xamiramogdan"
# email="xamiramogdan"

# email="laminewalter7"
# email="kalawssimatrix"
# email=
# email="xamiramogdan"
# email="almidaopo"
# email="abedrahman0x"
# email="don0mar0l0k0"
# email="xamiramogdan"
# email="xamiramogdan"
# email="xamiramogdan"
# email="xamiramogdan"
# email="xamiramogdan"
# paxx="agoon007"
paxx="g0ping0*"


url_1="https://console.cloud.google.com/"


user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]



random_ads=cnf_bvb.random_ads
url_click_ads="https://click.a-ads.com/1859747/"+random_ads+"/"
########################################################################################################################################


###################################################################################################


def clean_up():
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log && rm ipifo.json > /dev/null 2>&1")
	os.system("rm -rf rm -rf __pycache__/")
	init_fire()
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
###################################################################################################






	#starting_tasks()
############################################################################################









def lets_play(driver) :
	time.sleep(1)
	staage="STARTING GOO_LET_PLAY [ "+cnf_bvb.g00g_acc+" ] ["#+os.system("echo $WEBHOOK_URL")+" ] "
	print(staage)
	cnf_bvb.send_msg_dock(staage)

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

###########################################################################

def check_reconect(driver):
	print("CHECK TEMINAL DISPONIBILITY ..... ",end='',flush=True)
	try:
		reconnect_button=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloudshell"]/div/horizontal-split/div[2]/devshell/terminal-container/terminal-status-bar/status-message/mat-toolbar/button[2]')))
		reconnect_button.click()
		print("syeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!!!!!")
		starting_tasks()
		
	except Exception as e:
		print("still  not  fucking  reconect!!!!!!")
		open_login_button=WebDriverWait(driver, 58).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
		open_login_button.click()
		open_login_button.send_keys("clear && docker ps",Keys.ENTER)
		time.sleep(300)
		# driver.save_screenshot("scr.png")
		print("OK XTERMINAL FOUND !!!!!!")
		check_reconect(driver)

def check_recovery(driver):
	print("CHECK RECOVERY MAIL !!!!!!")
	try:
		#/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]
		#//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]/div
		click_on_recovery_email=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]/div')))
		click_on_recovery_email.click()
		time.sleep(5)
		# //*[@id="knowledge-preregistered-email-response"]
		input_on_recovery_email=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
		input_on_recovery_email.send_keys("cha3b0n@protonmail.com",Keys.ENTER)
		print("OK recovery EMAIL ENTRED !!!!!!")
		time.sleep(8)



	except Exception as e:
		print("NO RECOVERY ")



#################################"MAIN STARTING"##############################
def ads_class(driver):

	try:
		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)
		driver.get("https://shell.cloud.google.com/?cloudshell=true&show=terminal")
		time.sleep(10)
		# # input('')
		try:
			shell_limit=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/cloud-shell-root/div/stand-alone/div[1]/div/loading-screen/div/div/div[2]/div[1]/div/div/div/div')))
			print("ok this account DOWN")
			cnf_bvb.send_msg_dock("ok this account DOWN")
			sql_gc_get.change_gc_acc()
			return
			# 
		except:
			print("ok this account ACTIVE")
			cnf_bvb.send_msg_dock("ok this account ACTIVE")

		try:


			
			open_login_button=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
			print("we are here")
			staage="OK XTEMINAL ACTIVATED [ "+cnf_bvb.g00g_acc+" ] ["#+os.system("echo $WEBHOOK_URL")+" ] "
			print(staage)
			cnf_bvb.send_msg_dock(staage)
			open_login_button.click()
			open_login_button.send_keys("sudo su",Keys.ENTER)
			time.sleep(10)
			open_login_button.send_keys("clear && docker ps",Keys.ENTER)
			time.sleep(3)
			open_login_button.send_keys("./start.sh",Keys.ENTER)
			time.sleep(25)
			check_reconect(driver)
		except Exception as e:
			print(e+" errrrrrrrro1") 

	except Exception as e:
		print("ads error")
	# driver.delete_all_cookies()
	
######################USER AGENT ###################################################
		
def starting_tasks():
	width ,height=cnf_bvb.resolution_func()

	try:
		stage_1()### CLEAR
		# mod_vpn2.fnc_vpn ()
		cnf_bvb.extact_gc_profile()
		visible_v=cnf_bvb.visible_v
		# display = Display(visible=visible_v, size=(width,height)).start()
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