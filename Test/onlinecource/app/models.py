from django.db import models

# Create your models here.


class Courses_details(models.Model):
      course_name=models.CharField(primary_key=True,max_length=50,null=False)
      course_discription=models.TextField()
      lectures_list=models.TextField()
      course_content=models.CharField(max_length=100,null=False)

class Student(models.Model):
     
      name=models.CharField(max_length=45,null=True)
      email=models.EmailField(max_length=45,null=True)
      phone=models.CharField(max_length=10,null=True)
      address=models.TextField()
      courses=models.ForeignKey(Courses_details,null=True,on_delete=models.DO_NOTHING)
      student_id=models.CharField(max_length=45,null=True)
      password=models.CharField(primary_key=True,max_length=45,null=False)
      re_password=models.CharField(max_length=45,null=True)
      
          
      
          



