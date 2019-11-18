import mysql.connector
mydb=mysql.connector.connect(host="localhost",user=" root",passwd="",database="disaster_management1")

def register(utype,name,gender,dob,hname,place,dist,pin,phone,email):
	mycursor = mydb.cursor()
	sql = "INSERT INTO tbl_registration(user_type,user_name,gender,dob,h_name,place,district,pin,phone_no,email_id )VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val = (utype,name,gender,dob,hname,place,dist,pin,phone,email)
	mycursor.execute(sql,val)
	mydb.commit()

def regem(servicetype,idno,headofservice,noofemployees,phone,place,dist,email):
	mycursor = mydb.cursor()
	sql = "INSERT INTO tbl_services(emer_type,identification_no,name_of_head,no_of_employees,phone,place,district,email )VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	val = (servicetype,idno,headofservice,noofemployees,phone,place,dist,email)
	mycursor.execute(sql,val)
	mydb.commit()
	
def regres(usertype,resourcetype,resname,resquantity,regid):
	mycursor = mydb.cursor()
	sql = "INSERT INTO tbl_resources(usertype,res_type,res_name,quantity,reg_id )VALUES (%s,%s,%s,%s,%s)"
	val = (usertype,resourcetype,resname,resquantity,regid)
	mycursor.execute(sql, val)
	mydb.commit()
	
def getvolid(user):
	mycursor = mydb.cursor()
	sql = "select regid from tbl_registration where email_id ='"+user+"'"
	mycursor.execute(sql)
	result=mycursor.fetchone()
	return list(result)
# get normal people id

def getuser(user):
	mycursor = mydb.cursor()
	sql = "select regid,user_name from tbl_registration where email_id ='"+user+"'"
	mycursor.execute(sql)
	result=mycursor.fetchone()
	return list(result)


def getemer(user):
	mycursor = mydb.cursor()
	sql = "select emer_id ,name_of_head from tbl_services where email ='"+user+"'"
	mycursor.execute(sql)
	result=mycursor.fetchone()
	return list(result)

def regshelter(stype,name,acc,fac,place,dist,regid,usertype):
	mycursor = mydb.cursor()
	sql = "INSERT INTO tbl_shelter(shelter_type,shel_name,people_accomodation,facilities,place,district,reg_id,usertype)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	val = (stype,name,acc,fac,place,dist,regid,usertype)
	mycursor.execute(sql, val)
	mydb.commit()

def login(utype,email,passw):
	mycursor = mydb.cursor()
	sql = "INSERT INTO tbl_login(usertype,username,password,status)VALUES (%s,%s,%s,%s)"
	if utype=="User":
		val = (utype,email,passw,'Accept')
	else:
		val = (utype,email,passw,'Not Verified')
	mycursor.execute(sql,val)
	mydb.commit()

def saveskill(skill,regid):
	mycursor = mydb.cursor()
	sql= "INSERT INTO tbl_volunteer(vol_skills,reg_id)values(%s,%s)"
	val =(skill,regid)
	mycursor.execute(sql,val)
	mydb.commit()

def logincheck(user,passw):
	mycursor = mydb.cursor()
	sql = "select usertype from tbl_login where username ='"+user+"'and password='"+passw+"' and status= 'Accept' "
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)==1:
		return list(result)
	else:
		return False
	mydb.commit()

# def getid(userid):
# 	sql = "select requester_name from tbl_helprequest where assigned_to='"+userid+"'"
# 		mycursor = mydb.cursor()
# 	mycursor.execute(sql)
# 	result=mycursor.fetchall()
# 	if len(result)==1:
# 		return list(result)
# 	else:
# 		return False
# 	mydb.commit()


def saveupdate(itemtype,value,id):
	mycursor = mydb.cursor()
	sql = "INSERT INTO tbl_allocation(request_id,item_type,value)VALUES (%s,%s,%s)"
	print(value)
	val = (id,itemtype,value)
	mycursor.execute(sql, val)
	# mycursor = mydb.cursor()
	# sql="select shel_name from tbl_shelter where shelter_id='"+value+"'"
	# mycursor.execute(sql)
	# result=mycursor.fetchall()
	# print(result)
	# mycursor = mydb.cursor()
	# sql="select alloc_id from tbl_allocation where value='"+value+"'"
	# mycursor.execute(sql)
	# results=mycursor.fetchall()
	# print(result)
	# mycursor=mydb.cursor()
	# sql="update tbl_allocation set value='"+str(result)+"'where alloc_id='"+str(results)+"'"
	# print(sql)
	# mycursor.execute(sql)
	mydb.commit()



def viewpeople():
	mycursor = mydb.cursor()
	# sql="select tbl_allocation.*,tbl_helprequest.requester_name as requester_name,tbl_helprequest.requested_to as requested_to,tbl_registration.user_name as user_name from tbl_allocation,tbl_helprequest,tbl_registration where tbl_helprequest.requester_name=tbl_registration.regid and tbl_allocation.item_type='Shift'"
	sql="select * from tbl_allocation where item_type='Shift'"
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		return list(result)
	else:
		return False

def viewsheltertoall():
	result=[]
	mycursor = mydb.cursor()
	sql = "select * from tbl_shelter"
	mycursor.execute(sql)
	result=mycursor.fetchall()
	if len(result)>0:
		 result = list(result)
	else:
		result = []
	return result