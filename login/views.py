from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as mysql

# Create your views here.
em=''
pw=''

def login(request):
    global em,pw
    if request.method=='POST':
        mydb=mysql.connect(host='localhost',user='root',password='code-with-me',database='guri',auth_plugin='mysql_native_password')
        cursor=mydb.cursor()
        d=request.POST
        for key , value in d.items():
            if key=='email' :
                em=value

            if key=='password':
                pw=value
        c="select * from sign where  email='{}'and password='{}' ".format(em,pw)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
                return render (request,'error.html')

        else:
            return render(request,'welcome.html')



    return render(request,'login.html')


# Create your views here.
