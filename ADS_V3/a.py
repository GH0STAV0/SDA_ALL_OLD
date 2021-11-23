
import os



pwd = os.path.dirname(os.path.realpath( __file__ ))

vpn_folder=pwd+"/CHEAP_VPN/"

all_vpn_config_file=os.listdir(vpn_folder)

print(len(all_vpn_config_file))




def creat_list_of_vpn():
	with open('list_1','w') as fw:
		for i in all_vpn_config_file:
			fw.write(i+"\n")


creat_list_of_vpn()