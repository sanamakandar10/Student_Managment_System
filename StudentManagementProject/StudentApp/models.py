from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_duration = models.CharField(max_length=150)
    course_fees = models.IntegerField()

    def __str__(self):
        return self.course_name

class City(models.Model):
    city_name = models.CharField(max_length=150)

    def __str__(self):
        return self.city_name

class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_phno = models.BigIntegerField()
    stu_email = models.CharField(max_length=150)
    paid_fees = models.IntegerField()
    pending_fees = models.IntegerField()
    stu_course = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
    stu_city = models.ForeignKey(City,on_delete=models.CASCADE,default=None)
