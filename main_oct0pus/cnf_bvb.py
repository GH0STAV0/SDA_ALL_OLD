import random , os ,requests
import json
import socket
import socket
hostname_os=socket.getfqdn()
goog="/root/g00g"
pwd = os.path.dirname(os.path.realpath( __file__ ))

visible_v=0

if "LOOKE3" in hostname_os:
	print(hostname_os)
	visible_v=1



def read_current_acc_goo():
	with open(goog,'r') as file:
		lines = file.readlines()
		lines=lines[0].replace("\n","")
	return lines

print(read_current_acc_goo())
# g00g_acc=read_current_acc_goo()
# g00g_acc="garmiyashour"
# 
# erogomayke
g00g_acc="erogomayke"

# g00g_acc="laminewalter7"
# g00g_acc="dahmandargo"
# g00g_acc="xamiramogdan"
pofile_path=pwd+"/"+g00g_acc

print(pofile_path)



########################################################################################################################

def send_msg_dock(text):

	msg_telegram="[ "+hostname_os +" ]"+text
	token = "5261450305:AAEROP9j6569RV4rKsE_tStXCdnLSX7Gz1Y"
	# chat_id = "-643828126"
	chat_id = "-615987943"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 
	results = requests.get(url_req)
	print(results.json())
	
###############################################################################################################################

print("extact")
comom="cp po/"+g00g_acc+".tar.gz ./"
os.system(comom)
comom_2="tar xvf "+g00g_acc+".tar.gz"
os.system(comom_2)






user_agent_list = [
'AppleCoreMedia/1.0.0.12B466 (Apple TV; U; CPU OS 8_1_3 like Mac OS X; en_us)'
,'Mozilla/5.0 (Android 7.0; Mobile; LG-M150; rv:68.0) Gecko/68.0 Firefox/68.0'
,'Mozilla/5.0 (Android 8.0.0; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0'
,'Mozilla/5.0 (Android 8.1.0; Tablet; rv:68.0) Gecko/68.0 Firefox/68.0'
,'Mozilla/5.0 (Android 9; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0'
,'Mozilla/5.0 (Linux; Android 10; PH-1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 10; Pixel 2 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 10; Pixel 2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 10; Pixel 3 Build/QP1A.190711.020.C3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 10; Pixel XL Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 10; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.0.3; HTC Sensation 4G Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.0.3; KFTT) AppleWebKit/537.36 (KHTML, like Gecko) Silk/73.7.5 like Chrome/73.0.3683.90 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.2.2; GT-I9152 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.4.2; GT-N5110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.4.2; RCT6773W22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.4.2; TegraNote-P1640 Build/KOT49H; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.0.2; SM-A500H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.0.2; SM-T357T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.0.2; SM-T530NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.0.2; SM-T530NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.0; RCT6213W87DK) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 YaBrowser/19.4.1.454.01 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.0; SM-N900T Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/229.0.0.35.117;]'
,'Mozilla/5.0 (Linux; Android 5.1.1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/4.4.1 Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; AFTB) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.16 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.26'
,'Mozilla/5.0 (Linux; Android 5.1.1; AFTT) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.16 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; KFAUWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; KFDOWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/71.2.4 like Chrome/71.0.3578.98 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; KFDOWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; KFFOWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; KFGIWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; KFSUWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; KFSUWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/77.1.127 like Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; LG-AS330) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; LGL43AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G530R7 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-T377P) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-T900) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG-SM-T337A Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SM-G360T1 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.81 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SM-T280) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SM-T330NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SM-T670) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; SM-T670) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1.1; Vodafone Smart ultra 6 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1; BLU Advance 5.0 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1; HTC Desire 626s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-L22 Build/HUAWEILUA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1; NX16A11264) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 5.1; XT1526) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; CPH1613) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; LG-M153 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; LG-M153) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; LGLS676) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; N9136) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G900I) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G900P Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-J700M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-S327VL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG-SM-T377A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-G550T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-G550T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-G550T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-G900V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-J327P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-N910S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-N920V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-T350 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; SM-T800) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; XT1254) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; Z798BL Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0.1; Z799VL Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.2454.95 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0; 5010X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0; CAM-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0; F3313) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 6.0; RCT6603W47M7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; 5049Z Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; ASUS_A002A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; Alcatel_5044C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; Astra Young Pro Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; Infinix X571) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-H872 Build/NRD90U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-K425 Build/NRD90U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-LS777) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-M210) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-M430) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-TP260 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 7.0; LG-TP260) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-TP450 Build/NRD90U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-V521) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LG-V521) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LGMP260 Build/NRD90U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LGMS210 Build/NRD90U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; LGMS210) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; P00I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; RS988) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J710F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-N920T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-G920A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-G920P Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 Flipboard/4.2.23/4722,4.2.23.4722'
,'Mozilla/5.0 (Linux; Android 7.0; SM-G920V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-G928V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-J327T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-J327T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-J327T1 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-J327T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-J327T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-N9208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-N920P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-N920T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-T585) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-T810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-T810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-T810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-T813) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; SM-T813) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; ST1009X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0; XT1663) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; A574BL Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 7.1.1; A574BL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 7.1.1; Coolpad 3632A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; General Mobile 4G Dual) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4) Plus Build/NCRS26.58-44-20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.111 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; Moto E (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; NX591J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; REVVLPLUS C3701A Build/143.54.190611.3701A-TMO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-J320A) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG-SM-T377A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SM-J700T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SM-T350) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SM-T377T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SM-T550 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; X20 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; Z851M Build/NMF26V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.1; Z899VL Build/NMF26V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 7.1.1; Z982 Build/NMF26V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 7.1.1; Z982) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/4.4.1 Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; AFTKMST12 Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.26'
,'Mozilla/5.0 (Linux; Android 7.1.2; AFTKMST12) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.16 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.26'
,'Mozilla/5.0 (Linux; Android 7.1.2; AFTN Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.26'
,'Mozilla/5.0 (Linux; Android 7.1.2; KFKAWI Build/NS6301; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; KFKAWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; KFMUWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; LG-SP200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; LG-SP200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; LM-X210(G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; LM-X210) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; RCT6973W43R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; ASUS_Z01FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; AUM-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; BRAVIA 4K GB Build/OPR2.170623.027.S25; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 8.0.0; CMR-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; EVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; G3223) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; LG-H910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; LG-H931) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; LG-H932) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/8.2 Chrome/63.0.3239.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-J337T Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-J737P) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-N950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G891A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G935A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-A720F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/231.0.0.39.113;]'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G570Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930T Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930V Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930VL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G935P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G935T Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.112 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-J337T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-J737A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-J737T1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-N950F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-N950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-N950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-N950U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; SM-S367VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36 OPT/1.22.80'
,'Mozilla/5.0 (Linux; Android 8.0.0; VS995) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; XT1635-02) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; moto e5 play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; moto e5 play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; moto e5 supra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.0.0; moto g(6)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; 5041C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; 6062W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; A502DL Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; A502DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; BKK-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; C4 Build/OPM2.171019.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; Coolpad 3310A Build/3310A.SPRINT.190213.0S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X604 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; Joy 1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LAVA LE9820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LG-Q710AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-Q610(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN) Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/235.0.0.38.118;]'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-V405) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X210(G) Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 agentweb/4.0.2 UCBrowser/11.6.4.950'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X210(G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X210(G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X210(G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X212(G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X220PM Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X410(FG)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X410(FG)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X410(FG)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LM-X410.FGN Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LML414DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; LML713DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5S) Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; One) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36/TansoDL'
,'Mozilla/5.0 (Linux; Android 8.1.0; RCT6873W42BMF8KC Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; REVVL 2 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; REVVL 2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-J727T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-J727T1 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-J727T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-T580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG-SM-J727A Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J260T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J260T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J260T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J410F Build/M1AJB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J727P Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J727T Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J727T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J727T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J727T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J727V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-J727V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-P580) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-T380) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-T580) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Safari/537.36 EdgA/42.0.2.3928'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-T580) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-T580) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-T580) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; TECNO CF8 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/239.0.0.41.152;]'
,'Mozilla/5.0 (Linux; Android 8.1.0; V1818CA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; meizu C9 Build/OPM2.171019.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 DuckDuckGo/5'
,'Mozilla/5.0 (Linux; Android 9; 1825) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; ANE-LX2 Build/HUAWEIANE-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.132 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/236.0.0.40.117;]'
,'Mozilla/5.0 (Linux; Android 9; BLA-A09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; CLT-L04) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; CPH1911 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/239.0.0.41.152;]'
,'Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; ELE-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; G8142) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; GM1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; GM1917) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; INE-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; LM-G710 Build/PKQ1.181105.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; LM-V405 Build/PKQ1.190202.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.15'
,'Mozilla/5.0 (Linux; Android 9; LM-V405) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; LM-V500N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; MI 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Mi A2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Moto Z (2)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Nokia 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6013 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; PAR-AL00 Build/HUAWEIPAR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/235.0.0.38.118;]'
,'Mozilla/5.0 (Linux; Android 9; Pixel 2 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.190105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Pixel 3a XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; REVVLRY ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; RMX1801) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Redmi 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G892U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G955F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G9600 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J415F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737P) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.0 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N960U1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-T720) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SHIELD Android TV Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-A105M Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/237.0.0.44.120;]'
,'Mozilla/5.0 (Linux; Android 9; SM-A205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 9; SM-A530N Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;KAKAOTALK 1908560'
,'Mozilla/5.0 (Linux; Android 9; SM-A600T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-A605F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-A920F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G892A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G950U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 9; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G950U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G955U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.73 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 9; SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G9600) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G960U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/233.0.0.36.117;]'
,'Mozilla/5.0 (Linux; Android 9; SM-G960U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 9; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G960U1 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 9; SM-G960U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3921.2 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G965U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G970U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 9; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G970U1 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-J337P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-J600G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.73 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/238.0.0.41.116;]'
,'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-J737A Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 9; SM-J737A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-J737V Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 [Pinterest/Android]'
,'Mozilla/5.0 (Linux; Android 9; SM-J737V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N950U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 9; SM-N950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N960U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 9; SM-N960U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 9; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N960U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N975U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.73 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 9; SM-N975U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 9; SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-N976V Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]'
,'Mozilla/5.0 (Linux; Android 9; SM-S367VL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-S767VL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-T597P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; SM-T720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; TECNO KC8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; cp3705A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; moto g(6) Build/PPS29.118-15-11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36;dailymotion-player-sdk-android 0.1.31'
,'Mozilla/5.0 (Linux; Android 9; moto g(6) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; moto g(7) play Build/PCYS29.105-134-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.132 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/235.0.0.38.118;]'
,'Mozilla/5.0 (Linux; Android 9; moto g(7) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; moto g(7) power) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; moto g(7) power) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; moto z4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; Android 9; moto z4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'
,'Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; GT-P3113 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'
,'Mozilla/5.0 (Linux; U; Android 4.1.2; ar-ae; GT-I8160 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
,'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Nexus 7 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30; DailymotionEmbedSDK 1.0'
,'Mozilla/5.0 (Linux; U; Android 4.4; en-us; SM-E500H Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
,'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; LGMS550 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/534.30'
,'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-J737T1 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/534.30'
,'Mozilla/5.0 (Linux; U; Android 7.0; TECNO CA6 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 OPR/5.3.2254.135058'
,'Mozilla/5.0 (Linux; U; Android 7.1.2; id-id; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.5.6'
,'Mozilla/5.0 (Linux; U; Android 9; in-id; CPH1911 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/25.6.0.0.5beta'
,'Mozilla/5.0 (Linux; U; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 OPR/44.1.2254.143214'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:68.0) Gecko/20100101 Firefox/68.0'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
,'Mozilla/5.0 (PlayStation 4 6.72) AppleWebKit/605.1.15 (KHTML, like Gecko)'
,'Mozilla/5.0 (SMART-TV; LINUX; Tizen 3.0) AppleWebKit/538.1 (KHTML, like Gecko) Version/3.0 TV Safari/538.1'
,'Mozilla/5.0 (SMART-TV; Linux; Tizen 3.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/47.0.2526.69 TV safari/537.36'
,'Mozilla/5.0 (SMART-TV; Linux; Tizen 4.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/56.0.2924.0 TV Safari/537.36'
,'Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
,'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
,'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36 Maxthon/5.2.7.5000'
,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.1.3683.41 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94'
,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/82.0.144 Chrome/76.0.3809.144 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
,'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
,'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18995'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19493'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.110 Safari/537.36 Vivaldi/2.7.1628.30'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.94'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3907.0 Safari/537.36 Edg/79.0.279.0'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Windows NT 10.0; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/80.0.180 Chrome/74.0.3729.180 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/82.0.144 Chrome/76.0.3809.144 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0 Waterfox/56.2.14'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
,'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Windows NT 6.1; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko'
,'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; rv:11.0) like Gecko'
,'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
,'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
,'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Windows NT 6.3; rv:69.0) Gecko/20100101 Firefox/69.0'
,'Mozilla/5.0 (Windows; U; Windows NT 10.0; en-US; Valve Steam GameOverlay/1568860339; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS aarch64 12371.75.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.105 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS armv7l 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS x86_64 10895.78.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.120 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS x86_64 11021.81.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS x86_64 11895.118.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.159 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS x86_64 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS x86_64 12239.92.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS x86_64 12239.92.4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS x86_64 12371.46.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.63 Safari/537.36'
,'Mozilla/5.0 (X11; CrOS x86_64 12371.65.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.93 Safari/537.36'
,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Safari/537.36'
,'Mozilla/5.0 (X11; U; U; Linux x86_64; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
,'Mozilla/5.0 (X11; U; U; Linux x86_64; pt-pt) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
,'Mozilla/5.0 (X11; U; U; Linux x86_64; th-th) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
,'Mozilla/5.0 (X11; U; U; Linux x86_64; vi-vn) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
,'Mozilla/5.0 (X11; U; U; Linux x86_64; zh-cn) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
,'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
,'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'
,'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'

]










#p_vpn_g="/root/install_add/moya/yserverListTCP/"
#
############################# VPN ##################################""



ads=['148554','148477','148709','143423','146817','147629','147257','148786','146991','148787','148066','148643','148283','144375','148279','144442','148555','148264','148804','148556','147277','147415','146209','148523','148680','144002','148540','147710','144323','144498','148758','144525','148263','146622','142824','146831','147535','148510','148600','145992','148482','139001','148628','148784','148685','147791','148059','144604','147966','146160','139480','148498','148760','148657','148721','148577','146708','148761','148762','139705','146145','143247','148717','148677','148539','148749','145585','148476','148522','147370','139134','148471','148759','148061','147081','145096','148242']

random_ads=random.choice(ads)

hostname_os=socket.getfqdn()

def send_msg(text):

	msg_telegram="[ "+hostname_os +" ]"+text
	token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	chat_id = "-643828126"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 
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
		print(" [ "+ip + " ] ["+tz+" ] [ "+loc+" ]")
	except Exception as e:
		ip=""
		tz="OKEurope/Paris"
		loc=""
	return ip,tz ,loc
########################################################################################################################################


pwd = os.path.dirname(os.path.realpath( __file__ ))
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

	# display_aary=['1366x768','2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x800','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','2160x4096','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x800','1920x1080','1920x1080','1366x768','1920x1080' ,'1280x720','2560x1440','1080x1920','1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1440x2560','1440x2560' ,'1080x1920','1080x1920','1080x1920' ,'1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920' ,'1080x1920','1080x1920','1080x1920' ,'1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','1920x1080','1920x1080','1280x768','1440x1440','1280x720','1280x720',  '1080x1920', '1080x1920','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x800','1280x800','1024x600','2048x1536' ,'1200x1920','1280x720' ,'1200x1920','1200x1920','1024x600','1024x600','1280x800','1920x1080','1920x1080'  ,'2048x1536','1280x800' ,'1280x800','1280x800','1024x600','1024x600','1280x800','1024x600' ,'1536x2048' ,'1080x1920','1080x1920','1280x800','1280x800','1024x600','1280x800','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x800','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','1080x1920','1125x2436','1125x2436','1242x2688','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']

	display_aary=['1366x768']#,'2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x800','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','2160x4096','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x800','1920x1080','1920x1080','1366x768','1920x1080' ,'1280x720','2560x1440','1080x1920','1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1440x2560','1440x2560' ,'1080x1920','1080x1920','1080x1920' ,'1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920' ,'1080x1920','1080x1920','1080x1920' ,'1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','1920x1080','1920x1080','1280x768','1440x1440','1280x720','1280x720',  '1080x1920', '1080x1920','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x800','1280x800','1024x600','2048x1536' ,'1200x1920','1280x720' ,'1200x1920','1200x1920','1024x600','1024x600','1280x800','1920x1080','1920x1080'  ,'2048x1536','1280x800' ,'1280x800','1280x800','1024x600','1024x600','1280x800','1024x600' ,'1536x2048' ,'1080x1920','1080x1920','1280x800','1280x800','1024x600','1280x800','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x800','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','1080x1920','1125x2436','1125x2436','1242x2688','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']

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
random_url=main_domain_BVB+random.choice(urls_BVB)
user_agent = random.choice(user_agent_list)


##URLS 
#firefox_options_binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox"
# new_driver_path = '/usr/bin/geckodriver_30'
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
	# firefox_version=['97.0.1']
	# firefox_version=['49.0b9']
	firefox_version=['57.0.1','58.0.1','59.0.1','60.0.1esr']
	random_firefox_version=random.choice(firefox_version)
	print("[ "+random_firefox_version +" ]", end=" ")
	new_binary_path="/root/EXTRAT/firefox-"+random_firefox_version+"/firefox/firefox"
	return new_binary_path









#['A9eUDU','NSpuuT','QgAzfX','jcrQpf','Z43671L','qjyP9X','Lz5rZS','j4g90O','brEiiVC','m503b','Gt2SxI','JOGiue4','8TYNXx','tL9Djz','rRYTiWV','PAvn1b','MwJeqF','ojwCL6y','5FGm7h','oXLIpl','L9jF4q','k3ml8RT','HbY3VOi','tGEKGa','stpEoEW','nKrKHc','ckStn2','UW56O4j','3VVPaa','Vvg0AB','DAzYNN','wEQ1j5','WYUA3CJ','C3g3NK','J6s9otD','7EtS006','UgZFoh','S2AMic','PhViZ1','LAza9z','Oddviy','HdPv9G','C9rRrE6','OUtWAW','QtCv7B','houxkS','EgQNIl','hMnyaa','PH4skF','McVohw','vi4BLYl','jaICfMC','8kQsQv','qvnsbY','d74rYIU','rXGRT8k','QujMcAw','qT1Y4T','G6xg8C','Radrdm','Oy7TqVC','hXnY2DM','o3DUu4','4wSzSD','xCDZ9N','yx50ta','ed4IGa','caUu5s','IZJjJZ','lEad2tu','su6CfC','CJ39da','3vEkmK','vWtD4WF','NrAPc9','8GesGO','OhJe4H','OGOUq2T','oU80T6','R4Ktpr','tL5vN9','Njl1h7N','7Kwu0k','Euf3eTN','0MZii60','LBWpwj','qFICk6','7RR01e','klzHsV0','ehxxXf','J1RzVe']
#urls_GH=['8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','g79adj','Ogm9Fe','pbB4FW','Wb4G42','vxsmiu','LtsqzD','W1dSue','NfLgjN','Ncvmrn','dsXNeT','JJzyo6i','qBsgAZc','cmhj27','LGfo9ZI','2T52Bt','R5DAtXN','oqPFU5','VQEqp9','0xrm94','v7AH3F','8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','g79adj','Ogm9Fe','pbB4FW','Wb4G42','vxsmiu','LtsqzD','W1dSue','NfLgjN','Ncvmrn','dsXNeT','JJzyo6i','qBsgAZc','cmhj27','LGfo9ZI','2T52Bt','R5DAtXN','oqPFU5','VQEqp9','0xrm94','v7AH3F','8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','khnRUV']
#user_agent_list = cnf.user_agent_list
#urls_GH=['8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','g79adj','Ogm9Fe','pbB4FW','Wb4G42','vxsmiu','LtsqzD','W1dSue','NfLgjN','Ncvmrn','dsXNeT','JJzyo6i','qBsgAZc','cmhj27','LGfo9ZI','2T52Bt','R5DAtXN','oqPFU5','VQEqp9','0xrm94','v7AH3F','8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','g79adj','Ogm9Fe','pbB4FW','Wb4G42','vxsmiu','LtsqzD','W1dSue','NfLgjN','Ncvmrn','dsXNeT','JJzyo6i','qBsgAZc','cmhj27','LGfo9ZI','2T52Bt','R5DAtXN','oqPFU5','VQEqp9','0xrm94','v7AH3F','8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','khnRUV']
#["sn2vgs","M8BX8A","EyHrD3","ZZzgb1l","MdTnsuI","gN1mJQ","mI1T0i","l9jANS","8TPX61g","q1phNNH","5MIExQ","Xv9Nkf","2utWpm","zTStzf","JQmh5fX","tuT54V","KADHzC","jLCRoA","cMHri7","oyaoulR","9z5KG6","oVrrNo","njEU7u","Ttbmqjj","hPfQsN","Dooegb","UXeGw4m","zM7ygn","TeVc5QR","KQ6vNo","AphqLR","N5OG6Z","O2FzPd","kXo8RS","TS0YkTN","Le6NaU","7QPGmV","5OjOVA","2Nb0TO","fBWF3B","Yk3PlM"]
#urls_GH=['kLposqf','2i6AK3','gVWSZi','hdFVGw','rFzcZY','8puju4','8bQMlRe','3LLjtm','B6W2GN','anAEGH','0OL88G','VbbhP3','gYYy1H','ttdkQ7','ZZyy2Fq','5dWeY27','uOsF3c','z3AgxI','8vuydD','Y24S8OJ','BV99fG','Paeqqo0','7kXMXL','qtZ9Ad','0agPaL7','AtZvno','P8FFPV','LvIGpy','kiAKGIx','Xjq6xs','hW7bdb','WQr8hj','0kLLTYd','wA5YS59','PjZjirc','0clpiZ','Ge2aAp','w21z4S','anqbTw','47TdEQ','1jc2AM','1nstCv','2InzVhX','5tmZut','xFT51W','QGaIM5','TYG15ub','A0hp3o','VUiQHXQ','x5GL0w','i32bpO','wJgUHO','W6TNFn','iwUa9sU','RiVjQ7','XFx1W8','k7A2U8','xJnGcw3','NbJcOQ','UHIFBzy','huj9BE','bB55K9k','b9MfOd','wAy0VDp','sRmH9kk']
#p_vpn_dead="/root/OUOIO/project_02/NORD_CONFIG/DEAD_CONFIG_TCP/"
##  DEAD_CONFIG_TCP dead config path yserverListTCP
#visibility="visible=1"
#
#p_vpn_g="/root/OUOIO/project_04_a_ads/NORD_CONFIG/ovpn_tcp/"