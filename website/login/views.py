from django.shortcuts import render
import mysql.connector as sql

em = ''
pwd = ''

# Create your views here.
def loginaction(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="your_password_here", database='project',
                        auth_plugin="mysql_native_password")
        cursor = m.cursor(dictionary=True)  # Use a dictionary cursor for easier result handling
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        # Use parameterized query to prevent SQL injection
        c = "SELECT * FROM collage WHERE college_name = %s AND password = %s"
        cursor.execute(c, (em, pwd))
        t = cursor.fetchall()

        if not t:
            return render(request, 'error.html')
        else:
            # Assuming you want to retrieve users based on the college_name obtained from the previous query
            l = "SELECT * FROM users WHERE college_name = %s"
            cursor.execute(l, (em,))
            re = cursor.fetchall()
            return render(request, "no.html", {'students': re})

    return render(request, 'login_page.html')
