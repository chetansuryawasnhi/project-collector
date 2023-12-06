from django.shortcuts import render
import mysql.connector as sql
st_name=''
# Create your views here.
def ok(request):
    global st_name
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="your_password_here", database='project', auth_plugin="mysql_native_password")
        cursor = m.cursor()
        d = request.POST
      # Initialize st_name outside the loop

        for key, value in d.items():
            if key == "ok":
                st_name = value
        c = "INSERT INTO users (student_name)VALUES('{}')".format(st_name)
        cursor.execute(c)
        m.commit()

    return render(request, 'no.html')
