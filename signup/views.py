from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as mysql
nm=""
em=""
pw=""

def signup(request):
    global nm,em,pw 
    if request.method=="POST":
        mydb=mysql.connect(host="localhost",user="root",
                           password="code-with-me",database="guri",auth_plugin="mysql_native_password")
        
        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='name':
                nm=value
            if key=='email':
                em=value
            if key=='password':
                pw=value
        c="INSERT INTO sign(name,email,password)VALUES ('{}','{}','{}')".format(nm,em,pw)
        cursor.execute(c)
        mydb.commit()
        return redirect("login/")
        
    return render(request,"signup.html")
# Create your views here.
