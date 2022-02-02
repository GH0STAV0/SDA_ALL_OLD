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
url_6=cnf_bvb.url_6

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
	os.system("rm -rf  __pycache__/ ")
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
		# driver.get("http://c0rner-bit.eu.org/index.html")
		###############################################################################################
		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)
		# driver.get("https://www.sec4891.eu.org/index.html")
		# driver.get("http://zone4891.eu.org/index.html")
		# driver.get("http://targirien.totalh.net/index.html") https://retro.mydiscussion.net/index.html
		# driver.get("http://crypto.synergize.co/index.html")
		driver.get("http://desk.my-board.org/index.html")
		try:

			ain_button=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.top-banner')))
			# ain_button.click()
			print('ok click')
			# time.sleep(15)
		# driver.get(url_6)
		except Exception as e:
			print("error scrol 1")

		# time.sleep(3)
		time.sleep(25)
		# driver.get(url_1)
		# print(" [ "+url_1+" ]")
		# append_to_l0g("CLICK  AND VISITE WEB-SITE   [ "+url_1+" ] OK")
		# time.sleep(25)

		
	except Exception as e:
		print(e)
	print("CLICK  AND VISITE WEB-SITE [ 2 ]...... ",end='',flush=True)

		# driver.get(second_2_visit)
		# try:

		# 	driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="post-body-2346695118421539823"]'))))
		# 	print("UUUUU")
		# 	time.sleep(10)
		# 	driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'yass-search-box'))))
		# 	time.sleep(10)
		# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
		# 	time.sleep(10)
		# 	getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Blog1_blog-pager-older-link"]/i')))
		# 	getLink_button.click()
		# 	driver.execute_script("window.scrollTo(0, 0);window.scrollTo(0, 0);")
		# except Exception as e:
		# 	print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")


		# cnf_bvb.send_msg("oooooooooooooooooooo")
	append_to_l0g("VISITE WEB-SITE [ 2 ] : [ +second_2_visit+]  OK")
		# time.sleep(2)
		# driver.execute_script("window.open('');")
		# driver.switch_to.window(driver.window_handles[2])
		# driver.get("http://dark-market.ueuo.com/index.html")
		# time.sleep(8)
		# time.sleep(3)


	driver.delete_all_cookies()
	print("Remove Cookies")



def blogger(driver):
	try:

		ain_button=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.top-banner')))
		ain_button.click()
		print('ok click')
		time.sleep(25)
	# driver.get(url_6)
	except Exception as e:
		print("error scrol 1")
		#####################################################################################
	driver.get(url_6)
	time.sleep(5)
	# input("")
	try:
		accept_coockies=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'cookieChoiceDismiss')))
		accept_coockies.click()
		time.sleep(5)
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	except Exception as e:
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	time.sleep(3)
	try:
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML4'))))
		time.sleep(5)
		# driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'PopularPosts1'))))
		# time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML2'))))
		time.sleep(5)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(10)
	except Exception as e:
		print("error scrol 1")
	try:
		post1_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[1]/div[1]/div[2]/a')))
		post1_coockies.click()
		print("1111111111111111111111111")
		time.sleep(5)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML4'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'PopularPosts1'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML2'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(10)

		# time.sleep(5)
		post2_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[2]/div[1]/div[2]/a')))
		post2_coockies.click()
		print("22222222222222222222222222222222")
		time.sleep(5)

		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(5)
		#time.sleep(4)

		post3_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[3]/div[1]/div[2]/a')))
		post3_coockies.click()
		print("X3333333333333333333")
		# input('')
		time.sleep(3)
		time.sleep(5)
	except Exception as e:
		print("error scrol 1")
	# time.sleep(1)
	# driver.execute_script("window.open('');")
	# time.sleep(3)
	# driver.switch_to.window(driver.window_handles[1])
	# time.sleep(3)

def starting_tasks():
	width ,height=cnf_bvb.resolution_func()


######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		visible_v=cnf_bvb.visible_v
		display = Display(visible=visible_v, size=(width,height)).start()
		mod_vpn2.fnc_vpn ()
		# cnf_bvb.alias_send_msg_2()
		# os.environ['DISPLAY']
		driver=mod_driver2.build_driver(width ,height)
		lets_play(driver)
		#driver.delete_all_cookies()
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
