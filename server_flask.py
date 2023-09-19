from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import send_file
from flask import jsonify
from flask import session
import random as rd

import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbgatou",
        charset='utf8', buffered=True)


SESSION_TYPE = 'redis'
app = Flask(__name__)

app.secret_key = "1234"  

SP={}
SP["Theoretical"]=1
SP["Art"]=2
SP["Science"]=3
SP["IT"]=4
SP["Economics"]=5


#roots

@app.route("/")
def firstpage():
    
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('main.html', menu=t, user=fn)
    else:
        return render_template('index.html', menu="")


@app.route("/js/<file>")
def jsfile(file):
    return send_file(file)


@app.route("/img/<file>")
def images(file):
    return send_file(file)


@app.route("/css/<file>")
def cssread(file):  
    return send_file(file)


@app.route("/main")
def main():
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('main.html', menu=t, user=fn)
    else:
        return render_template('index.html', menu="")


@app.route("/login")
def login1():
    return render_template('login.html',menu="")


@app.route("/loginadmin")
def showdataadmin():
    return render_template('loginadmin.html',menu="")


@app.route("/signup")
def signup():
    return render_template('signup.html',menu="")


@app.route("/signup2", methods=['POST', 'GET'])
def singup2():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    if request.method == 'POST':
        e=str(request.form.get('username'))
        p=str(request.form.get('pwd'))
        fn=str(request.form.get('fname'))
        sp=str(request.form.get('sp'))
        sex=str(request.form.get('sex'))
        year=str(request.form.get('year1'))
        type="student"
        sql="insert into users set "
        sql=sql+"username='"+e+"',"
        sql=sql+"password='"+p+"',"
        sql=sql+"fullname='"+fn+"',"
        sql=sql+"type='student',"
        sql=sql+"speciality='"+sp+"',"
        sql=sql+"sex='"+sex+"',"
        sql=sql+"yearbirth='"+year+"'"
       
        try:
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            error=0
        except:
            error=1
           
    return jsonify({"err": error})
    

@app.route("/updateprofile", methods=['POST', 'GET'])
def upd2():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    if request.method == 'POST':
        e=str(request.form.get('username'))
        p=str(request.form.get('pwd'))
        fn=str(request.form.get('fname'))
        sp=str(request.form.get('sp'))
        sex=str(request.form.get('sex'))
        year=str(request.form.get('year1'))
        type=session["t"]
        sql="update users set "
        sql=sql+"username='"+e+"',"
        sql=sql+"password='"+p+"',"
        sql=sql+"fullname='"+fn+"',"
        sql=sql+"type='"+type+"',"
        sql=sql+"speciality='"+sp+"',"
        sql=sql+"sex='"+sex+"',"
        sql=sql+"yearbirth='"+year+"'"
        sql=sql+" where id="+str(session.get("u"))
        
        try:
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            error=0
        except:
            error=1
        
    return jsonify({"err": error})  
    

@app.route("/updateuser", methods=['POST', 'GET'])
def updateuser():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    if request.method == 'POST':
        e=str(request.form.get('username'))
        p=str(request.form.get('pwd'))
        fn=str(request.form.get('fname'))
        sp=str(request.form.get('sp'))
        sex=str(request.form.get('sex'))
        year=str(request.form.get('year1'))
        type=str(request.form.get('role'))
        idu=str(request.form.get('idu'))
        sql="update users set "
        sql=sql+"username='"+e+"',"
        sql=sql+"password='"+p+"',"
        sql=sql+"fullname='"+fn+"',"
        sql=sql+"type='"+type+"',"
        sql=sql+"speciality='"+sp+"',"
        sql=sql+"sex='"+sex+"',"
        sql=sql+"yearbirth='"+year+"'"
        sql=sql+" where id="+idu
        
        try:
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            error=0
        except:
            error=1
              
    return jsonify({"err": error})  
    
    
@app.route("/getuser")
def getuser():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    sql="select * from users where id="+str(session.get("u"))
    
    mycursor.execute(sql)
    r=mycursor.fetchone()
    mycursor.close()
    return jsonify(r)

    
@app.route("/users")
def user1():
        return render_template('users.html',menu=session['t'])
    
    
@app.route("/getusers")
def getusersjs():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    sql="select * from users"
    mycursor.execute(sql)
    records=mycursor.fetchall()
    mycursor.close()
    L=[]
    for rec in records:
        r={}
        r['id']=rec[0]
        r['fullname']=rec[1]
        r['username']=rec[2]
        r['password']=rec[3]
        r['sex']=rec[4]
        r['type']=rec[5]
        r['speciality']=rec[6]
        r['yearbirth']=rec[7]   
        L.append(r)
        
    return jsonify(L)
    
    
@app.route("/profile")
def profile():
    
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('profile.html', menu=t, user=fn)
    else:
        return render_template('index.html', menu="")


@app.route("/checklogin", methods=['POST', 'GET'])
def checklogin():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    if request.method == 'POST':
        e=str(request.form.get('username'))
        p=str(request.form.get('pwd'))
       
        try:
            sql="select * from users where username='"+e+"' and password='"+p+"'"
            mycursor.execute(sql)
            r=mycursor.fetchone()
            mycursor.close()
            session['u']=r[0]
            session['fn']=r[1]
            session['t']=r[5]
            u=r[0]
            m=r[5]
            fn=r[1]
            
            return render_template('main.html',menu=m, user=fn)
        except:
            print("Not found")
            session['u']=None
            error=1
            m=""
            
            return render_template('login.html',menu=m,error=1)


@app.route("/putpoint")
def putpoint():
    if(session.get("u")!=None):
        return render_template('putpoint.html', menu=2)
    else:
        return render_template('index.html', menu=1)

    
@app.route("/logout")
def logout():
    session['u']=None
    session['t']=None
    session['fn']=None
    return render_template('index.html', menu="")
    

@app.route("/getdata", methods=['POST', 'GET'])
def getdata():
    if request.method == 'POST':
        print(str(request.form.get('email'))+" "+str(request.form.get('pwd')))
    return render_template('login.html')
   
    
@app.route("/lessons")
def lessons():
    
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('categories.html', menu=t, user=fn)
    else:
        return render_template('index.html', menu="")   
    
       
@app.route("/edituser/<id1>")
def edituser(id1):
    
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('edituser.html', menu=t, user=fn, idu=id1)
    else:
        return render_template('index.html', menu="")   


@app.route("/deleteuser/<id1>")
def deleteuser(id1):
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    mycursor.execute("delete from users where id="+str(id1))
    mydb.commit()
    mycursor.close()
    return jsonify({"err":"1"})         


@app.route("/delcat/<id1>")
def delcat(id1):
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    mycursor.execute("delete from categories where id="+str(id1))
    mydb.commit()
    mycursor.close()
    return jsonify({"err":"1"}) 


@app.route("/savecat/<id1>/<t>")
def savecat(id1,t):
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    mycursor.execute("update  categories set title='"+t+"' where id="+str(id1))
    mydb.commit()
    mycursor.close()
    return jsonify({"err":"1"})     
 
 
@app.route("/setval/<id1>/<d>")
def setval(id1,d):
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    mycursor.execute("delete from usr_rec where id_rec='"+str(id1)+"' and id_user="+str(session.get('u')))
    mycursor.execute("insert into usr_rec set degree="+str(d)+" , id_rec='"+str(id1)+"' , id_user="+str(session.get('u')))
    mydb.commit()
    mycursor.close()
    return jsonify({"err":"1"}) 


@app.route("/putViews/<id1>")
def putViews(id1):
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    mycursor.execute("update recommend set views=views+1 where id="+str(id1))
    mydb.commit()
    mycursor.close()
    return jsonify({"err":"1"}) 
   
   
@app.route("/ins")
def ins():
    
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('insrec.html', menu=t, user=fn)
    else:
        return render_template('index.html', menu="")   
  
  
@app.route("/ins2", methods=['POST', 'GET'])
def ins2():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    if request.method == 'POST':
        title=str(request.form.get('title'))
        dsc=str(request.form.get('descr'))
        url1=str(request.form.get('url'))
        cat=str(request.form.get('category'))
       
        sql="insert into recommend set "
        sql=sql+"title='"+title+"',"
        sql=sql+"perigrafi='"+dsc+"',"
        sql=sql+"link='"+url1+"',"
        sql=sql+"id_cat='"+cat+"',"
        sql=sql+"id_user='"+str(session.get('u'))+"',"
        sql=sql+"views=0, readn=0"
        
        try:           
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            error=0
        except:
            error=1
              
    return jsonify({"err": error})      

       
@app.route("/addcat", methods=['POST', 'GET'])
def addcat():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    if request.method == 'POST':
        cat=str(request.form.get('lesson'))
       
        sql="insert into categories set "
        sql=sql+"title='"+cat+"'"
               
        try:            
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            error=0
        except:
            error=1
              
    return jsonify({"err": error})      


@app.route("/getProfile")
def getProfile():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    sql="select * from users where id="+str(session.get('u'))
    
    mycursor.execute(sql)
    
    rec=mycursor.fetchone()
    mycursor.close()
    
    return jsonify(rec)     
 
 
@app.route("/getcats")
def getcats():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    sql="select * from categories order by title"
    mycursor.execute(sql)
    records=mycursor.fetchall()
    mycursor.close()
    L=[]
    for rec in records:
        r={}
        r['id']=rec[0]
        r['title']=rec[1] 
        L.append(r)
    return jsonify(L)   
  

  
def dist(r1):
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    sql="select * from users where id="+str(session.get('u'))
    
    mycursor.execute(sql)
    rec=mycursor.fetchone()
    
    
    r=str(r1)
    sql="select * from recommend where id='"+r+"' "
    
    mycursor.execute(sql)
    rec1=mycursor.fetchone()
       
    
    
    sql="select avg(degree) as av from usr_rec where id_rec='"+r+"' "
    mycursor.execute(sql)
    rec2=mycursor.fetchone()
    
    try:
      sql="select degree from usr_rec where id_rec='"+r+"' and id_user="+str(session.get('u'))
      mycursor.execute(sql)
      rec21=mycursor.fetchone()
      #mesos oros vathmologias xrhstwn
      x51=1-float(rec21[0])/5
    except:
      x51=0.5

    sql="select * from users where id="+str(rec1[6])
    
    mycursor.execute(sql)
    rec3=mycursor.fetchone()
    mycursor.close()   
    
    #fylo
    if(rec3[4]==rec[2]):
     x1=0
    else:
     x1=1

        
    #eidikotita
    try:
     x2=abs(SP[rec3[6]]-SP[rec[6]])/4
    except:
     x2=1
    
    #typos
    if(rec3[5]=='teacher'):
     x3=0
    else:
     x3=1
     
    #ilikia
    if(abs(rec3[7]-rec[7])>20):
     x4=1
    else:
     x4=abs(rec3[7]-rec[7])/20
     
    #views
    if(rec1[4]>100):
     x6=0
    else:
     x6=1-rec1[4]/100
    
    #mesi vathmologia
    try:
     x5=1-float(rec2[0])/5
    except:
     x5=1
    if(x51>0.5):
     d=1
    else:
     d=(x1+x2+x3+x4+3*x5+x6+4*x51)/12
       
    return d
 
 
def sortbyd(d):
 return d["dist"]
 
 
@app.route("/getrecom/<id1>")
def getrecom(id1):
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    sql="select *,users.id as idu from recommend,users where users.id=recommend.id_user and id_cat='"+id1+"' "
    mycursor.execute(sql)
    records=mycursor.fetchall()
    mycursor.close()
    L=[]
    for rec in records:
     r={}
     r['id']=rec[0]
     r['title']=rec[1] 
     r['link']=rec[2] 
     r['perigrafi']=rec[3] 
     r['dist']=dist(r['id']);
     r['user']=rec[10]
     L.append(r)
    
    L2=sorted(L,key=sortbyd)
    return jsonify(L2)      


@app.route("/getmyrecom")
def getmyrecom():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    sql="select *, categories.title as ltitle from recommend,categories where categories.id=recommend.id_cat  and id_user="+str(session.get('u'))
    mycursor.execute(sql)
    records=mycursor.fetchall()
    mycursor.close()
    L=[]
    for rec in records:
     r={}
     r['id']=rec[0]
     r['title']=rec[1] 
     r['link']=rec[2] 
     r['perigrafi']=rec[3] 
     r['ltitle']=rec[10] 
     L.append(r)
    return jsonify(L)   


@app.route("/getval")
def getval():
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    L=[]
    try:
      sql="select id_rec,degree from usr_rec where  id_user="+str(session.get('u'))
      mycursor.execute(sql)
      records=mycursor.fetchall()
      mycursor.close()
    
      for rec in records:
        r={}
        r["id"]=rec[0]
        r["d"]=rec[1]
        L.append(r)
    except:
      L=[]
    return jsonify(L)   


@app.route("/getval2")
def getval2():
    global mydb,mycursor
    
    sql="select id_rec,avg(degree) from usr_rec group by id_rec"
    try:
     mycursor=mydb.cursor(buffered=True)
     mycursor.execute(sql)
     records=mycursor.fetchall()
     mycursor.close()
     L=[]
     
     for rec in records:
      r={}
      r["id"]=rec[0]
      r["d"]=str(rec[1])
      L.append(r)
    except Exception as e:
      print(e)
      L=[]
    return jsonify(L)   

    
@app.route("/edituserjs/<id1>")
def edituserjs(id1):
    global mydb,mycursor
    mycursor=mydb.cursor(buffered=True)
    sql="select * from users where id='"+id1+"'"
    
    mycursor.execute(sql)
    r=mycursor.fetchone()
    mycursor.close()
    
    return jsonify(r)   

        
@app.route("/recom2")
def recom2():
    
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('recom2.html', menu=t, user=fn)
    else:
        return render_template('index.html', menu="")  

        
@app.route("/myrec")
def myrec():
    
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('myrec.html', menu=t, user=fn)
    else:
        return render_template('index.html', menu="")  
  
  
@app.route("/recom21/<id>")
def recom21(id):
    
    if(session.get("u")!=None):
        fn=session.get("fn")
        t=session.get("t")
        return render_template('rec21.html', menu=t, user=fn,idr=id)
    else:
        return render_template('index.html', menu="")           

#api

app.run(debug=True,threaded=True,port=5000)
    



