import mysql.connector
from datetime import datetime
mydb=mysql.connector.connect(host="localhost",user=" root",passwd="",database="disaster_management1")


def dbstate():
	sql="select * from tbl_state"
	mycursor=mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	return(result)

# def dbdistrict(state):
# 	sql="select * from tbl_district where state_id='"+str(state)+"'"
# 	mycursor=mydb.cursor()
# 	mycursor.execute(sql)
# 	result=mycursor.fetchall()
# 	return(result)


def displayres():
	mycursor = mydb.cursor()
	sql = "select tbl_resources.*,tbl_registration.user_name as user_name from tbl_resources,tbl_registration where tbl_resources.reg_id=tbl_registration.regid"
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else :
		return False

def displayshelter():
	mycursor = mydb.cursor()
	sql = "select * from tbl_shelter "
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else :
		return False


# def getaccpetvol(email_id):
# 	mycursor = mydb.cursor()
# 	print(email_id)
# 	sql="update tbl_login set status = 'Accept' where username = '"+email_id+"'"
# 	mycursor.execute(sql)
# 	# result=mycursor.fetchall()
# 	mydb.commit()
# 	return "ok"



def getaccpetvol(email_id):
	mycursor = mydb.cursor()
	print(email_id)
	sql="update tbl_login set status = 'Accept' where username = '"+email_id+"'"
	print(sql)
	mycursor.execute(sql)
	# result=mycursor.fetchall()
	mydb.commit()
	return "ok"



def getrejectvol(email_id):
	mycursor = mydb.cursor()
	print(email_id)
	sql="update tbl_login set status = 'Reject' where username = '"+email_id+"'"
	print(sql)
	mycursor.execute(sql)
	# result=mycursor.fetchall()
	mydb.commit()
	return "ok"


def getaccpetpol(email_id):
	mycursor = mydb.cursor()
	print(email_id)
	sql="update tbl_login set status = 'Accept' where username = '"+email_id+"'"
	print(sql)
	mycursor.execute(sql)
	# result=mycursor.fetchall()
	mydb.commit()
	return "ok"
def getrejectpol(email_id):
	mycursor = mydb.cursor()
	print(email_id)
	sql="update tbl_login set status = 'Reject' where username = '"+email_id+"'"
	print(sql)
	mycursor.execute(sql)
	# result=mycursor.fetchall()
	mydb.commit()
	return "ok"

def getaccpetfire(email_id):
	mycursor = mydb.cursor()
	print(email_id)
	sql="update tbl_login set status = 'Accept' where username = '"+email_id+"'"
	print(sql)
	mycursor.execute(sql)
	# result=mycursor.fetchall()
	mydb.commit()
	return "ok"

def getrejectfire(email_id):
	mycursor = mydb.cursor()
	print(email_id)
	sql="update tbl_login set status = 'Reject' where username = '"+email_id+"'"
	print(sql)
	mycursor.execute(sql)
	# result=mycursor.fetchall()
	mydb.commit()
	return "ok"

def displayreslist():
	mycursor = mydb.cursor()
	sql = "select * from tbl_resources "
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else :
		return False


def savehelp(desc,name,regid):
	mycursor = mydb.cursor()
	datee=datetime.today()
	timee=datetime.now().time()
	sql= "INSERT INTO tbl_helprequest(help_type,date,time,status,requested_to,requester_name)values(%s,%s,%s,%s,%s,%s)"
	val =(desc,datee,timee,'Not Accepted',name,regid,)
	mycursor.execute(sql,val)
	mydb.commit()


def gethelplist():
	mycursor = mydb.cursor()
	sql="select tbl_helprequest.*,tbl_registration.user_name as user_name  from tbl_helprequest,tbl_registration where tbl_helprequest.requester_name = tbl_registration.regid "
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False


def gethelpvol(helpid,regid,usertype):
	mycursor = mydb.cursor()
	time=datetime.now().time()
	sql="update tbl_helprequest set status = 'Accept',assigned_to='"+str(regid)+"',assigned_time='"+str(time)+"' where help_id = "+str(helpid)+""
	print(sql)
	mycursor.execute(sql)
	mydb.commit()
	sql="select tbl_helprequest.*,tbl_registration.user_name as user_name  from tbl_helprequest,tbl_registration where tbl_helprequest.requester_name = tbl_registration.regid "
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	result=mycursor.fetchall()
	# print(result)
	return list(result)



def requesthistory(regid):
	mycursor = mydb.cursor()
	# sql="select * from tbl_helprequest where requester_name="+str(regid)+""
	sql="select tbl_helprequest.*,tbl_registration.user_name as user_name from tbl_helprequest,tbl_registration where tbl_helprequest.requester_name=tbl_registration.regid and tbl_helprequest.requester_name="+str(regid)+""
	print(sql)
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else :
		return False


def viewalert(regid,type,alert_id):
	mycursor = mydb.cursor()
	sql= "INSERT INTO tbl_viewalert(reg_id,usertype)values(%s,%s)"
	val =(regid,type)
	mycursor.execute(sql,val)
	mydb.commit()
	sql="select * from tbl_alert where alert_id='"+str(alert_id)+"'"
	mycursor = mydb.cursor()
	print(sql)
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else :
		return False
	# sql = "INSERT INTO tbl_viewalert(reg_id )VALUES (%s,%s,%s,%s,%s)"
	# val = (regid)
	# mycursor.execute(sql, val)
	# mydb.commit()


# def getname(regid):
# 	mycursor = mydb.cursor()
# 	sql = "select user_name from tbl_registration where regid ='"+str(regid)+"'"
# 	print(sql)
# 	mycursor.execute(sql)
# 	result=mycursor.fetchall()
# 	if len(result)>0:
# 		return list(result)
# 	else :
# 		return False