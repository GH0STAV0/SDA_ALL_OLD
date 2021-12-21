import mysql.connector

import time ,os
from datetime import datetime




vpn_folder="/root/VPN/N0RD/WORKING_CONFIG/"


all_vpn_config_file=os.listdir(vpn_folder)
# print(str(len(all_vpn_config_file)))

def creat_list_of_vpn():
	with open(file_list_1,'w') as fw:
		for i in all_vpn_config_file:
			fw.write(i+"\n")




mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")



def check_connect_mysql():
	print(" CHECK SQL  CONNECTION       : ",end='',flush=True)
	try:
		
		mycursor = mydb.cursor()
		print("MYSQL CONNECTED OK ")
	except  Exception as e :
		print(" SQL ERROR CONNECTION        : "+str(e)+" ",end='',flush=True)




def insert_to_db(cnf_name):

	
	mycursor = mydb.cursor()
	sql = "INSERT INTO nord_list (cnf_names, used) VALUES (%s, %s)"
	val = (cnf_name, "n")
	mycursor.execute(sql, val)
	time.sleep(2)

	mydb.commit()



def loop_conf():
	for i in all_vpn_config_file:
		print(i)
		insert_to_db(i)



# check_connect_mysql()
loop_conf()
