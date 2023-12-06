from django.shortcuts import render
import mysql.connector as sql

# Create your views here.
def signaction(request):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="your_password_here", database='project', auth_plugin="mysql_native_password")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "st_name":
                st_name = value
            if key == "cln":
                cln = value
            if key == "uln":
                uln=value
            if key == "protit":
                protit = value
            if key == "prodesc":
                prodesc = value
            satus="no"
        c = "INSERT INTO users VALUES('{}','{}','{}','{}','{}','{}')".format(st_name,cln,uln,protit,prodesc,satus)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')
