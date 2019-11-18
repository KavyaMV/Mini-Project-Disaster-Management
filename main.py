from flask import Flask,render_template,request,make_response,url_for,session,redirect
import db
import guest
import admin
import selectplace
# from flask.ext.session import Session
app = Flask(__name__)
app.secret_key = "disater"
import mimetypes
mimetypes.add_type("text/css", ".css", True)
# @app.route("/home")
@app.route("/",methods=["GET","POST"])
def hello():
	# resp = make_response(render_template('index.html'))
	# resp.headers['Content-type'] = 'text/css; charset=utf-8'
	return render_template('index.html')

@app.route("/reg",methods=["GET","POST"])
def reg():
	utype=request.form.get('txttype')
	name=request.form.get('txtname')
	hname=request.form.get('txthname')
	place=request.form.get('place')
	dist=request.form.get('district')
	pin=request.form.get('txtpin')  
	phone=request.form.get('txtphone')  
	gender=request.form.get('radiogen')  
	dob=request.form.get('caldob')  
	email=request.form.get('txtemail')
	passw=request.form.get('txtpassword') 
	guest.register(utype,name,gender,dob,hname,place,dist,pin,phone,email)
	guest.login(utype,email,passw)
	return redirect(url_for("hello"))

@app.route("/regpol",methods=["GET","POST"])
def  regpol():
	servicetype=request.form.get('txtsertype')
	idno=request.form.get('txtidno')
	headofservice=request.form.get('txtheadname')
	noofemployees=request.form.get('txtemployeeno')
	phone=request.form.get('txtphone')
	place=request.form.get('place')
	dist=request.form.get('district')
	email=request.form.get('txtemail')
	passw=request.form.get('txtpassword')
	guest.regem(servicetype,idno,headofservice,noofemployees,phone,place,dist,email)
	guest.login(servicetype,email,passw)
	return redirect(url_for("hello"))

@app.route("/resource",methods=["GET","POST"])
def resource():
	resourcetype=request.form.get('txtrestype')
	resname=request.form.get('txtresname')
	resquantity=request.form.get('txtqua')
	guest.regres(session["usertype"],resourcetype,resname,resquantity,session["userid"])
	return("Registered sucessfully")

@app.route("/shelter",methods=["GET","POST"])
def shelter():
	stype=request.form.get('sheltype')
	acc=request.form.get('txtaccommodate')
	fac=request.form.get('facility')
	place=request.form.get('place')
	dist=request.form.get('district')
	name=request.form.get('txtname')  
	guest.regshelter(stype,name,acc,fac,place,dist,session["usertype"],session["userid"])
	return("Registered sucessfully")

@app.route("/skill",methods=["GET","POST"])
def skill():
	skill=request.form.get('Skills')
	guest.saveskill(skill,session["userid"])
	return("data saved")


@app.route("/regem",methods=["GET","POST"])
def regem():
	state=db.dbstate()
	return render_template("regpol.html",state=state)


@app.route("/register",methods=["GET","POST"])
def register():
	state=db.dbstate()
	return render_template("reg.html",state=state)

# @app.route("/getDistrict",methods=["GET","POST"])
# def getdistrict():
# 	state=request.form.get('state')
# 	dist=db.dbdistrict(state)
# 	s="<select class= form-control name = district> <option>................select.............</option>"
# 	for d in dist:
# 		s=s+"<option value="+str(d[0])+">"+d[1]+"</option>"
# 	s=s+"</select>"
# 	print(s)
# 	return s

@app.route("/getdistrict",methods=["GET","POST"])
def getdistrict():
	state=request.form.get('state')
	dist=selectplace.getDistrict()
	s="<select class= form-control  onchange='getplace(this.value)'  name = district> <option>................select.............</option>"
	for d in dist:
		s=s+"<option value="+str(d)+">"+str(d)+"</option>"
	s=s+"</select>"
	
	return s

@app.route("/getplace",methods=["GET","POST"])
def getplace():
	district=request.form.get('place')
	place=selectplace.getPlace(district)
	# print(place)
	s="<select class= form-control name = place> <option>................select.............</option>"
	for p in place:
		s=s+"<option value="+str(p)+">"+str(p)+"</option>"
	s=s+"</select>"
	return s


@app.route("/login",methods=["GET","POST"])
def login():
	return render_template("login.html")

@app.route("/logchk",methods=["GET","POST"])
def logchk():
	user=request.form.get('txtuser')
	passw=request.form.get('txtpass')
	r=guest.logincheck(user,passw)

	if r==False:
		return "failed"
	elif r[0][0] =="admin" and passw=="admin123":
		session['username'] = "admin@gmail.com"
		session["usertype"]= "admin"
		return render_template("admin/home.html")

	elif r[0][0] == "User":
		session['username'] = user
		session["usertype"]=r[0][0]
		session["userid"]=guest.getuser(user)[0]
		print(session["userid"],session["usertype"],session["username"])
		return render_template("user/home.html")

	elif r[0][0] == "Volunteer":
		session['username'] = user
		session["usertype"]=r[0][0]
		session["userid"]=guest.getvolid(user)[0]
		return render_template("volunteer/home.html")

	elif r[0][0] == "Fire station":
		session['username'] = user
		session["usertype"]=r[0][0]
		session["userid"]=guest.getemer(user)[0]
		return render_template("firestation/home.html")
		
	elif r[0][0] == "Police station":
		session['username'] = user
		session["usertype"]=r[0][0]
		session["userid"]=guest.getemer(user)[0]
		return render_template("policestation/home.html")


@app.route("/showresource",methods=["GET","POST"])
def showresource():
	return render_template("volunteer/resources.html")

@app.route("/showshelter",methods=["GET","POST"])
def showshelter():

	state=db.dbstate()
	return render_template("volunteer/shelter.html",state=state)

@app.route("/vol",methods=["GET","POST"])
def showvol():
	state=db.dbstate()
	return render_template("volunteer/vol.html")


@app.route("/volunteerhome",methods=["GET","POST"])
def volunteerhome():
	return render_template("volunteer/home.html")

@app.route("/displayresourcevol",methods=["GET","POST"])
def displayresourcevol():
	resources=db.displayres()
	return render_template("volunteer/viewres.html", resourcelist=list(resources))

@app.route("/displaysheltervol",methods=["GET","POST"])
def displaysheltervol():
	shelters=db.displayshelter()
	return render_template("volunteer/viewshelter.html", shelterlist=list(shelters))


# to Add resource by police

@app.route("/showresources",methods=["GET","POST"])
def showresources():
	return render_template("policestation/resources.html")

#view templates for police(resource,shelter)

@app.route("/policehome",methods=["GET","POST"])
def policehome():
	return render_template("policestation/home.html")	

@app.route("/displayresourcepol",methods=["GET","POST"])
def displayresourcepol():
	resources=db.displayres()
	return render_template("policestation/viewres.html",resourcelist=list(resources))


@app.route("/displayshelterpol",methods=["GET","POST"])
def displayshelterpol():
	shelter=db.displayshelter()
	return render_template("policestation/shelter.html",shelterlist=list(shelter))


# to add resource by fire station

@app.route("/showresourcesfir",methods=["GET","POST"])
def showresourcesfir():
	return render_template("firestation/resources.html")	



# to display shelter,resources for fire station

@app.route("/firestnhome",methods=["GET","POST"])
def firestnhome():
	return render_template("firestation/home.html")

@app.route("/displayresourcesfir",methods=["GET","POST"])
def displayresourcesfir():
	resources=db.displayres()
	return render_template("firestation/viewres.html",resourcelist=list(resources))

@app.route("/displayshelterfir",methods=["GET","POST"])
def displayshelterfir():
	shelter=db.displayshelter()
	return render_template("firestation/viewshelter.html",shelterlist=list(shelter))

# common people resource viewing

@app.route("/userhome",methods=["GET","POST"])
def userhome():
	return render_template("user/home.html")	

@app.route("/displayresourcecommon",methods=["GET","POST"])
def displayresourcecommon():
	resources=db.displayres()
	return render_template("user/viewresource.html",resourcelist=list(resources))

@app.route("/showalerts",methods=["GET","POST"])
def showalerts():
	data= admin.getalertlist()
	if data == False:
		data=[]
	return render_template("user/alerts.html",alertlist = list(data))


###


###admin home
@app.route("/adminhome",methods=["GET","POST"])
def adminhome():
	return render_template("admin/home.html")


@app.route("/view_vol",methods=["GET","POST"])
def view_vol():
	data= admin.getviewvol()
	if data == False:
		data=[]
	return render_template("admin/volregview.html", volList = list(data))

@app.route("/view_police",methods=["GET","POST"])
def view_police():
	data= admin.getviewpolice()
	if data == False:
		data=[]
	return render_template("admin/polregview.html", policeList = list(data))

@app.route("/view_firest",methods=["GET","POST"])
def view_firestation():
	data= admin.getviewfirestation()
	# print(data)
	if data == False:
		data=[]
	return render_template("admin/firereglist.html", firestationtList = list(data))

@app.route("/acceptvol",methods=["GET","POST"])
def acceptvol():
	email=request.form['email_id']
	data= db.getaccpetvol(email)
	return "ok"

@app.route("/rejectvol",methods=["GET","POST"])
def rejectvol():
	email=request.form['email_id']
	data= db.getrejectvol(email)
	return "ok"

@app.route("/acceptpol",methods=["GET","POST"])
def acceptpol():
	email=request.form['email_id']
	data= db.getaccpetpol(email)
	return "ok"

@app.route("/rejectpol",methods=["GET","POST"])
def rejectpol():
	email=request.form['email_id']
	data= db.getrejectpol(email)
	return "ok"

@app.route("/acceptfire",methods=["GET","POST"])
def acceptfire():
	email=request.form['email_id']
	data= db.getaccpetfire(email)
	return "ok"

@app.route("/rejectfire",methods=["GET","POST"])
def rejectfire():
	email=request.form['email_id']
	data= db.getrejectfire(email)
	return "ok"

@app.route("/view_users",methods=["GET","POST"])
def view_users():
	data= admin.getviewusers()
	return render_template("admin/registeredusers.html", usersList = list(data))


@app.route("/regview_vol",methods=["GET","POST"])
def regview_vol():
	data= admin.getregviewvol()
	if data == False:
		data=[]
	return render_template("admin/viewregvolunteer.html", regvolList = list(data))

@app.route("/regview_police",methods=["GET","POST"])
def regview_police():
	data= admin.getregviewpolice()
	if data == False:
		data=[]
	return render_template("admin/listpolregview.html", regpoliceList = list(data))

@app.route("/regview_firest",methods=["GET","POST"])
def regview_firest():
	data= admin.getregviewfirestation()
	if data == False:
		data=[]
	return render_template("admin/viewfirereglist.html", regfirestationtList = list(data))


@app.route("/showres",methods=["GET","POST"])
def showres():
	return render_template("admin/viewresources.html")	

@app.route("/displayresourceadmin",methods=["GET","POST"])
def displayresourceadmin():
	resources=db.displayreslist()
	return render_template("admin/listres.html", reslist=list(resources))

@app.route("/displayshelteradmin",methods=["GET","POST"])
def displayshelteradmin():
	shelter=admin.displayshelteradmin()
	return render_template("admin/adminviewshelter.html",adminshelterlist=list(shelter))

@app.route("/adminshowshelter",methods=["GET","POST"])
def adminshowshelter():
	state=db.dbstate()
	return render_template("admin/shelter.html",state=state)

#Alerts

@app.route("/createalert",methods=["GET","POST"])
def createalert():
	state=db.dbstate()
	return render_template("admin/createalert.html",state=state)

@app.route("/savealert",methods=["GET","POST"])
def savealert():
	alerttype=request.form.get('alerttype')
	desc=request.form.get('txtareadescription')
	place=request.form.get('place')
	dist=request.form.get('district')
	datee=request.form.get('txtdate')
	# timee=request.form.get('txttime')
	admin.savealert(alerttype,desc,datee,place,dist)
	return("Successful")

@app.route("/listalert",methods=["GET","POST"])
def listalert():
	data= admin.getalertlist()
	if data == False:
		data=[]
	return render_template("admin/alertlist.html",alertlist = list(data))

@app.route("/listalertpol",methods=["GET","POST"])
def listalertpol():
	data= admin.getalertlist()
	if data == False:
		data=[]
	return render_template("policestation/alertlist.html",alertlist = list(data))

@app.route("/listalertvol",methods=["GET","POST"])
def listalertvol():
	data= admin.getalertlist()
	if data == False:
		data=[]
	return render_template("volunteer/alertlist.html",alertlist = list(data))

@app.route("/listalertfir",methods=["GET","POST"])
def listalertfir():
	data= admin.getalertlist()
	if data == False:
		data=[]
	return render_template("firestation/alertlist.html",alertlist = list(data))


# Help Request

@app.route("/createhelprequest",methods=["GET","POST"])
def createhelprequest():
	# data=db.getname(session["userid"])
	return render_template("user/helprequest.html")

@app.route("/savehelprequest",methods=["GET","POST"])
def savehelprequest():
	desc=request.form.get('txthelprequest')
	name=request.form.get('txtname')
	db.savehelp(desc,name,session["userid"])
	return("saved")


@app.route("/listhelpvol",methods=["GET","POST"])
def listhelpvol():
	data= db.gethelplist()
	return render_template("volunteer/viewhelp.html",helplist = list(data))

@app.route("/listhelppol",methods=["GET","POST"])
def listhelppol():
	data= db.gethelplist()
	return render_template("policestation/viewhelp.html",helplist = list(data))

@app.route("/viewhelpfire",methods=["GET","POST"])
def viewhelpfire():
	data= db.gethelplist()
	return render_template("firestation/viewhelp.html",helplist = list(data))


@app.route("/accepthelp",methods=["GET","POST"])
def accepthelp():
	helpid=request.form['help_id']
	data= db.gethelpvol(helpid,session["userid"],session["usertype"])
	return "ok"



@app.route("/requesthistory",methods=["GET","POST"])
def requesthistory():
	data=db.requesthistory(session["userid"])
	if data == False:
		data=[]
	return render_template("user/viewhelp.html",helplist=list(data))

@app.route("/removealertadmin",methods=["GET","POST"])
def removealertadmin():
	alert_id=request.args.get('id')
	print(alert_id)
	data=admin.getremovealertadmin(alert_id)
	if data == False:
		data=[]
	return render_template("admin/alertlist.html",alertlist=list(data))	
	# return("ok")

@app.route("/editalertadmin",methods=["GET","POST"])
def editalertadmin():
	alert_id=request.args.get('id')
	state=db.dbstate()
	return render_template("admin/createalert.html",state=state)
	
@app.route("/mapload",methods=["GET","POST"])
def mapload():
	alertData = admin.getalertwithplacedetaisl()
	return render_template("map.html",data=alertData)
	
@app.route("/viewalertfire",methods=["GET","POST"])
def viewalertfire():
	alert_id=request.args.get('id')
	print(alert_id)
	data=db.viewalert(session["userid"],session["usertype"],alert_id)
	return render_template("firestation/viewalert.html",alertlist=list(data))


@app.route("/viewalertvol",methods=["GET","POST"])
def viewalertvol():
	alert_id=request.args.get('id')
	print(alert_id)
	data=db.viewalert(session["userid"],session["usertype"],alert_id)
	return render_template("volunteer/viewalert.html",alertlist=list(data))

@app.route("/viewalertpol",methods=["GET","POST"])
def viewalertpol():
	alert_id=request.args.get('id')
	print(alert_id)
	data=db.viewalert(session["userid"],session["usertype"],alert_id)
	return render_template("policestation/viewalert.html",alertlist=list(data))

@app.route("/updatehelpvol",methods=["GET","POST"])
def updatehelpvol():
	# helpid=request.form['help_id']
	result=guest.viewsheltertoall()
	return render_template("volunteer/updatehelp.html", data = result)

@app.route("/updatehelpfire",methods=["GET","POST"])
def updatehelpfire():
	# helpid=request.form['help_id']
	result=guest.viewsheltertoall()
	return render_template("firestation/updatehelp.html", data = result)

@app.route("/updatehelppol",methods=["GET","POST"])
def updatehelppol():
	# helpid=request.form['help_id']
	result=guest.viewsheltertoall()
	return render_template("policestation/updatehelp.html", data = result)


@app.route("/saveupdate",methods=["GET","POST"])
def saveupdate():
	# guest.getid(session["userid"])
	itemtype=request.form.get('txtupdate')
	value=request.form.get('updatehelp')
	guest.saveupdate(itemtype,value,session['userid'])
	return "ok"

@app.route("/viewacc",methods=["GET","POST"])
def viewacc():
	data=guest.viewpeople()
	return render_template("volunteer/peopleacc.html",peoplelist=list(data))

@app.route("/logout",methods=["GET","POST"])
def logout():
	session.clear()
	return redirect(url_for("hello"))
	

if __name__ == "__main__":
	app.run(debug=True)