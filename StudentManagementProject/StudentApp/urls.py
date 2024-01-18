from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.login_fun,name='log'),
    #it will redirect to login.html page
    path('reg',views.register_fun,name='reg'),# redirect to register page
    path('home',views.home_fun,name='home'),# redirect to home page
    path('add_course',views.addcourse_fun,name='add_course'),#redirect to addcourse page
    path('display_course',views.display_course_fun,name='display_course'), # it will collect data from course table and send to displaycourse.html
    path('update_course/<int:courseid>',views.update_course_fun,name='update_course'),
    path('delete_course/<int:courseid>',views.deleta_course_fun,name='delete_course'),
    path('addstudent',views.addstudent_fun,name='addstudent'),
    path('displaystudent',views.displaystudent_fun,name='displaystudent'),
    path('updatestudent/<int:studid>',views.updatestudent_fun,name='updatestudent'),
    path('deletestudent/<int:studid>',views.deletestudent_fun,name='deletestudent'),
    path('logout',views.logout_fun,name='logout')
]