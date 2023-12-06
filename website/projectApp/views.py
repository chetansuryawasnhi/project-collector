from django.shortcuts import render
import mysql.connector as sql

# Create your views here.
def signinaction(request):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Chetan", database='project', auth_plugin="mysql_native_password")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "cln":
                cln = value
            if key == "univname":
                st_name = value
            if key == "password":
                protit = value
            

        c = "INSERT INTO collage values('{}','{}','{}')".format(cln,st_name,protit)
        cursor.execute(c)
        m.commit()

    return render(request,'projectApp.html')
