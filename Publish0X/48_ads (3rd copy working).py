import cnf_bvb
import mod_vpn2
import mod_driver2
import activation_link
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
import t00l
import io
from pydub import AudioSegment
import speech_recognition as sr
import railway_sql


# import pickle

telrgram_text=[]

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




def audio_fonction(download_link):
	#data = open('1.mp3', 'rb').read()
	# print("ok download_link")
	request = requests.get(download_link)
	# print("ok request download_link")
	audio_file = io.BytesIO(request.content)
	sound = AudioSegment.from_mp3(audio_file)
	dst = "test1.wav"
	sound.export(dst, format="wav")
	r = sr.Recognizer()
	with sr.WavFile("test1.wav") as source:
		audio = r.record(source)
	
	audio_output=r.recognize_google(audio)
	print("Transcription: " + audio_output)
	return audio_output






	#starting_tasks()
############################################################################################
def capatch(driver):
	print("\n # STARTING CAPATCHA  ")
	print(" |")
	# global new_amount
	driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/main/div/div[4]/div/form/div[5]/div/button'))))
	# without_captcha_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'without_captcha_button')))
	# without_captcha_button.send_keys(Keys.TAB )
	# time.sleep(2)
	# main_button=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'without_captcha_button')))
	# time.sleep(5)
	number_fra=driver.find_elements_by_tag_name("iframe")
	iframes = driver.find_elements_by_xpath("//iframe")
	print(str(len(iframes)))
	for index , iframe in enumerate(iframes):
		yhio=iframe.get_attribute('title')
		print(str(index)+" -- "+iframe.get_attribute('title'))
		if "AddThis"  in yhio :
			driver.switch_to.frame(index)
			print("SWITCH TO : "+yhio)
			time.sleep(6)
			try:
				# pass
				singup_green_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]')))
				singup_green_button.click()
				print("CHECK SUCCESS  ")
				try:
					# singup_green_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '')))
					donne_ok=WebDriverWait(driver, 9).until(EC.presence_of_element_located((By.XPATH,'//span[@aria-checked="true"]')))
					print('lucky captcha')
					driver.switch_to.default_content()
					time.sleep(2)
					return
				except Exception as e:
					raise e

				# /html/body/div[2]/div[3]/div[1]/div/div/span/div[4]
				print("GO TO CHALANGE ")
				driver.switch_to.default_content()
				time.sleep(5)
				break
			except Exception as e:
				print("NO N0 : AddThis")
				driver.switch_to.default_content()
				time.sleep(2)
				# reefree(driver)
				# break
				# reefree(driver)
	driver.switch_to.default_content()
	time.sleep(5)
	iframes = driver.find_elements_by_xpath("//iframe")
	print(str(len(iframes)))
	print("SEARCH IN ALL ")
	for index , iframe in enumerate(iframes):
		yhio=iframe.get_attribute('title')
		if "challenge"  in yhio :
			driver.switch_to.frame(index)
			print("SWITCH TO : "+yhio)
			time.sleep(7)
			try:
				# pass
				iframes = driver.find_elements_by_xpath("//iframe")
				NUMBER_OD_FRAME=len(iframes)
				print("IFRAM INSIDE THE FRAME 01 NUM "+str(NUMBER_OD_FRAME))
				if NUMBER_OD_FRAME ==1:
					print("IFRAM = 01  ")
					driver.switch_to.frame(1)
					time.sleep(5)
					# time.sleep(3)
				print("search  ")
				singup_green_button=WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-audio-button"]')))
				singup_green_button.click()
				print("audio-source clicked !!!!!!!!")
				try:
					main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-doscaptcha-body-text')))
					captcha_error_message=main_button.text
					print(" 000 : "+captcha_error_message)
				except Exception as e:
					print("NO ERROR MESSAGE ")
				eto_firstName=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'audio-source')))
				download_link = eto_firstName.get_attribute('src')
				# print(download_link)
				audio_output= audio_fonction(download_link)
				text_cap=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'audio-response')))
				text_cap.send_keys(audio_output)
				time.sleep(2)
				text_cap.send_keys(Keys.ENTER)
				try:
					error_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-audiochallenge-error-message')))
					captcha_error_message=main_button.text
					print(" multiple needed : "+captcha_error_message)
				except Exception as e:
					print("no multiple solution")
				driver.switch_to.default_content()
				os.system('rm test1.wav')
				print('Captcha resolved')
				print('audio_fonction')
				time.sleep(2)
				break
			except Exception as e:
				print("NO N0  ")
				driver.switch_to.default_content()
				time.sleep(3)
				reefree(driver)


	print("OUT CAPATCHA")
	time.sleep(2)
	print('CLOSE FONCTION CAPTCHA+ PASS')

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
		driver.get(url_1)
		try:

			ain_button=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.top-banner')))
			# ain_button.click()
			print('ok click')
			# time.sleep(15)
		# driver.get(url_6)
		except Exception as e:
			print("error scrol 1")

		# time.sleep(3)
		time.sleep(35)
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





######################USER AGENT ###################################################

def reefree(driver):
	print('TRY TO REFRESH')
	pox_init(driver)
	# driver.get('https://www.publish0x.com/?a=4oeE8D0Nd0')

############################################ - 3 ) P0X ###################################################

def pox_init(driver):
	driver.get('https://www.publish0x.com/')
	time.sleep(3)

	############################################//*[@id="registerPopupCloseModal"]
	try:
		singup_green_button=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registerPopupCloseModal"]')))
		singup_green_button.click()
		time.sleep(3)
		#registerPopup
		# input('')
		print('no close s87ac')
	except Exception as e:
		print('no close s87ac')

	############################################/html/body/div[6]/div/div /html/body/div[7]/div/div[1]/div/div/img

	############################################

	try:
		#//*[@id="registerPopupCloseModal"] /html/body/div[7]/div/div[1]/div/div
		singup_green_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registrationButton"]')))
		singup_green_button.click()

		time.sleep(3)
		singup_email_green_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registrationModal"]/div/div/div/p[1]/a')))
		singup_email_green_button.click()
		time.sleep(3)
		####################################
		# singup_green_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[1]/div/div/img')))
		# singup_green_button.click()

		try:
			singup_green_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[1]/div/div/img')))
			singup_green_button.click()
			time.sleep(3)
			# pass
		except Exception as e:
			# raise e
			print('no close 1')
		capatch(driver)
		# input('')
		print('FILL USER + PASS')
		singup_email_green_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
		singup_email_green_button.click()
		user_arr_info=[]
		user_arr_info=t00l.generate_name_add()
		singup_email_green_button.send_keys(user_arr_info[0],Keys.TAB,user_arr_info[1],Keys.TAB,user_arr_info[1])
		# /html/body/div[3]/main/div/div[4]/div/form/div[5]/div/button
		singup_email_green_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/main/div/div[4]/div/form/div[5]/div/button')))
		singup_email_green_button.click()
		# input('op')
	except Exception as e:
		print(e)

	############################################
	try:
		# //*[@id="name"]
		# /html/body/div[3]/main/div/div/div/div/div/div[1]
		name_green_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
		name_green_button.click()
		time.sleep(3)
		name_green_button.send_keys(user_arr_info[5],Keys.TAB*3,Keys.ENTER )
	except Exception as e:
		raise e

	############################################
	try:
		time.sleep(3)
		name_green_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/main/div/div/div/div/div/div[1]')))
		verrrr=name_green_button.text
		print(verrrr)
		link_activ=activation_link.gather_acces(user_arr_info[0])
		print("activation_link", end='',flush=True)
		driver.get(link_activ)
		print("ok")
		input("")
		
		# /html/body/div[3]/main/div/div[2]/div/div/div[3]/button
		# singup_email_green_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/main/div/div[2]/div/div/div[3]/button')))
		# singup_email_green_button.click()
		
		# driver.

	except Exception as e:
		print("oh noooo")

	tip_now(driver,user_arr_info)
	# input("pox")


############################################ - 1 ) starting_tasks ###################################################
def tip_now(driver,user_arr_info):
	print("tipping "+user_arr_info[5])
	railway_sql.insert_to_db_ph0x(user_arr_info[0],user_arr_info[1],user_arr_info[5])

	driver.get("https://www.publish0x.com/desire4fire/stellar-lumens-and-the-newest-thing-nft-ebooks-the-future-of-xelknme")
	driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div[10]/div/div'))))
	name_green_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/main/div/div[10]/div/div[1]/form/div/div[3]/button')))
	# https://www.publish0x.com/n0xin0x/russian-regulators-find-common-ground-bitcoin-can-t-be-used-xjopxvy
	

	name_green_button.click()
############################################ - 1 ) starting_tasks ###################################################

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



	try:
		stage_1()### CLEAR
		visible_v=cnf_bvb.visible_v
		mod_vpn2.fnc_vpn ()
		# display = Display(visible=visible_v, size=(width,height)).start()
		# cnf_bvb.alias_send_msg_2()
		# os.environ['DISPLAY']

		driver=mod_driver2.build_driver(width ,height)
		pox_init(driver)
		# input("")

		# lets_play(driver)
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
