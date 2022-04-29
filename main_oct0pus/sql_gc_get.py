import mysql.connector
import time ,os
from datetime import datetime
HOST="remotemysql.com"
USERNAME="f6V3kVwxvH"
PASSWORD="sOVnW1130i"
DATABASE="f6V3kVwxvH"

mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)

this_table="gc_acc"

def get_actif_account():
	mycursor = mydb.cursor()
	sql = "SELECT * FROM `"+this_table+"` WHERE (`acc_status`='A') ORDER BY RAND() LIMIT 1"
	mycursor.execute(sql)
	record = mycursor.fetchall()
	for row in record:
		fresh_gc_acc=str(row[1])
		# print(fresh_gc_acc)
	mycursor.close()
	mydb.close()
	return fresh_gc_acc


def restored_fresh_sql_table():
	# 

	print(" Reset All G_C table  OF  : ",end='',flush=True)
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	mycursor = mydb.cursor()
	sql = "UPDATE `"+this_table+"` SET    `acc_status` = 'NA'"
	mycursor.execute(sql)
	mydb.commit()
	mycursor.close()
	mydb.close()
	print("[ SUCCED ] ")



def update_to_db_as_used(cnf_name):
	# mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	# # check_connect_mysql()
	restored_fresh_sql_table()

	print(" UPDATE_SQL STATUS CONFIG [ "+cnf_name+" ] : ",end='',flush=True)
	mycursor = mydb.cursor()
	input=("A",cnf_name)
	# this_table=set_table(typ0)

	sql = "UPDATE `"+this_table+"` SET acc_status= %s  WHERE account_id = %s"
	mycursor.execute(sql,input)
	mydb.commit()
	mycursor.close()
	mydb.close()
	print("[ SUCCED ] ")
	# get_value_cnf(cnf_name)
##







# activ_acc=get_actif_account()
# print(activ_acc)
#"garmiyashour")
# update_to_db_as_used("erogomayke")