import mysql.connector
from datetime import datetime
import pandas as pd
import selectplace
mydb=mysql.connector.connect(host="localhost",user=" root",passwd="",database="disaster_management1")

def getviewusers():
	sql ="select * from tbl_registration where user_type = 'User'"
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False

def getviewvol():
	sql ="select tbl_registration.* from tbl_registration,tbl_login where user_type = 'Volunteer' and tbl_login.status='Not verified' and username=email_id"
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	print(result)
	return list(result)
		

def getviewpolice():
	sql ="select tbl_services.* from tbl_services,tbl_login where emer_type = 'Police station' and tbl_login.status='Not verified' and username=email"
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False

def getviewfirestation():
	sql ="select tbl_services.* from tbl_services,tbl_login where emer_type = 'Fire station' and tbl_login.status='Not verified' and username=email"
	# print(sql)
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	# print(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False


def getregviewvol():
	sql ="select tbl_registration.* from tbl_registration,tbl_login where user_type = 'Volunteer' and tbl_login.status='Accept' and username=email_id"
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False

def getregviewpolice():
	sql ="select tbl_services.* from tbl_services,tbl_login where emer_type = 'Police station' and tbl_login.status='Accept' and username=email"
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False

def getregviewfirestation():
	sql ="select tbl_services.* from tbl_services,tbl_login where emer_type = 'Fire station' and tbl_login.status='Accept' and username=email"
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False

def displayshelteradmin():
	mycursor = mydb.cursor()
	sql = "select * from tbl_shelter "
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else :
		return False


def savealert(alerttype,desc,datee,place,dist):
	mycursor = mydb.cursor()
	timee=datetime.now().time()
	sql = "INSERT INTO tbl_alert(alert_type,place,district,datee,timee,descrption)VALUES (%s,%s,%s,%s,%s,%s)"
	val = (alerttype,place,dist,datee,timee,desc)
	mycursor.execute(sql,val)
	mydb.commit()

def getalertlist():
	sql ="select * from tbl_alert "
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False

def getremovealertadmin(alert_id):
	sql="delete from tbl_alert where alert_id='"+alert_id+"'"
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	# print (sql)
	sql ="select * from tbl_alert"
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False
	mydb.commit()

def getalertwithplacedetaisl():
	sql = "select * from tbl_alert"
	cursor = mydb.cursor()
	cursor.execute(sql)
	result=cursor.fetchall()
	
	if len(result)>0:
		alertList = []

		for item in list(result):
			print("item si ====", item)
			alertDict = {}
			alertDict["alert_type"] = item[1] + " - " + item[6] + " - " + item[2]
			alertDict["alert_X"] = selectplace.getlatLong(item[2])[0][0]
			alertDict["alert_Y"] = selectplace.getlatLong(item[2])[1][0]
			alertList.append(alertDict)



		return alertList
	else:
		return False
	mydb.commit()
