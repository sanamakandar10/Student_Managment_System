from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from StudentApp.models import Course, City, Student


# Create your views here.
def login_fun(request):
    if request.method=='POST':
        user_name=request.POST['txtname']
        user_pass=request.POST['pwd']
        u1=authenticate(username=user_name,password=user_pass)
        if u1 is not None:
            if u1.is_superuser:
                request.session['Uname'] = user_name
                login(request,u1)
                return redirect('home')
        else:
            return render(request,'login.html',{'msg':'Username and password is incorrect'})
    else:
        return render(request,'login.html')



def register_fun(request):
    if request.method=='POST':
        user_name=request.POST['txtname']
        user_pass=request.POST['pwd']
        user_email=request.POST['txtemail']
        if User.objects.filter(username=user_name).exists():
            return render(request,'register.html',{'msg':'use proper username and email'})
        else:

            u1=User.objects.create_superuser(username=user_name,password=user_pass,email=user_email)
            u1.save()
            return redirect('log')
    else:

        return render(request,'register.html')

@login_required
@never_cache
def home_fun(request):
    return render(request,'home.html')

@login_required
@never_cache
def addcourse_fun(request):
    if request.method == 'POST':
        c1 = Course()
        c1.course_name = request.POST['txtcourse']
        c1.course_duration = request.POST['txtduration']
        c1.course_fees = int(request.POST['num1'])
        c1.save()
        return render(request,'addcourse.html',{'msg':'Successfully Added'})
    else:
        return render(request,'addcourse.html')

@login_required
@never_cache
def display_course_fun(request):
    course_data = Course.objects.all()
    return render(request,'displaycourse.html',{'data':course_data})

@login_required
@never_cache
def update_course_fun(request,courseid):
    c1 = Course.objects.get(id=courseid)
    if request.method == 'POST':
        c1.course_name=request.POST['txtcourse']
        c1.course_duration=request.POST['txtduration']
        c1.course_fees=int(request.POST['num1'])
        c1.save()
        return redirect('display_course')
    else:
        return render(request,'updatecourse.html', {'data': c1})

@login_required
@never_cache
def deleta_course_fun(request,courseid):
    c1 = Course.objects.get(id=courseid)
    c1.delete()
    return redirect('display_course')

@login_required
@never_cache
def addstudent_fun(request):
    if request.method == 'POST':
        s1 = Student()
        s1.stu_name = request.POST["txtname"]
        s1.stu_phno = int(request.POST["num1"])
        s1.stu_email = request.POST["email"]
        s1.stu_city = City.objects.get(city_name=request.POST["ddlcity"])
        s1.stu_course = Course.objects.get(course_name=request.POST["ddlcourse"])
        s1.paid_fees = int(request.POST["num2"])
        c1 = Course.objects.get(course_name=request.POST["ddlcourse"])

        s1.pending_fees = c1.course_fees - s1.paid_fees

        s1.save()
        return redirect('addstudent')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request,'addstudent.html',{'CityData':city, 'CourseData' : course })

@login_required
@never_cache
def displaystudent_fun(request):
    s1 = Student.objects.all()
    return render(request,'displaystudent.html',{'student':s1})

@login_required
@never_cache
def updatestudent_fun(request,studid):
    s1 = Student.objects.get(id=studid)
    if request.method == 'POST':
        s1.stu_name = request.POST["txtname"]
        s1.stu_phno = int(request.POST["num1"])
        s1.stu_email = request.POST["email"]
        s1.stu_city = City.objects.get(city_name=request.POST["ddlcity"])
        s1.stu_course = Course.objects.get(course_name=request.POST["ddlcourse"])
        s1.paid_fees = s1.paid_fees + int(request.POST["num2"])
        c1 = Course.objects.get(course_name=request.POST["ddlcourse"])
        if s1.pending_fees > 0:
            s1.pending_fees = c1.course_fees - s1.paid_fees
        else:
            s1.pending_fees = 0

        s1.save()
        return redirect('displaystudent')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request,'updatestudent.html',{'student':s1,'CityData': city, 'CourseData': course})

@login_required
@never_cache
def deletestudent_fun(request,studid):
    s1 = Student.objects.get(id=studid)
    s1.delete()
    return redirect('displaystudent')


def logout_fun(request):
    logout(request)

    return redirect('log')