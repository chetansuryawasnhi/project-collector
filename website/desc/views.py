from django.shortcuts import render
import mysql.connector as sql
uni=""
def desc(request):
        if request.method=="POST":
            global uni
        
            m = sql.connect(host="localhost", user="root", password="your_password_here", database='project', auth_plugin="mysql_native_password")
            cursor = m.cursor(dictionary=True)  # Use dictionary=True to fetch results as dictionaries
            d=request.POST
            for key,value in d.items():
                if key=="universityName":
                    uni=value
            l = f"select * from users where university_name='{uni}'"
            cursor.execute(l)
            re = cursor.fetchall()

            if re==():
                pass
            else: 
                return render(request, 'desc.html', {'students': re})
            
        return render(request,'main.html')