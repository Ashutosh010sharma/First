from django.shortcuts import render
from django.contrib import messages
from .models import Student,Courses_details

# Create your views here.
def home(request):
    return render(request,'app/html/home.html')
    
def login(request):    
    if request.method=="GET":
        return render(request,'app/html/login.html') 
    if  request.method=="POST":
          id=request.POST["userid"]
          password=request.POST["userpass"]
          print(id,password)
          student_list=Student.objects.filter(email=id,password=password)
          x=len(student_list)
         # print("length is ", x)
          if x>0:
                student_object=Student.objects.get(password=password)
                request.session["session_key"]=password
                context={"student_data":student_object}
                
                return render (request,'app/main/main.html',context)
          else:

               messages.error(request,"Invalid Credential")
               return render (request,'app/html/login.html')
          
def student_pro(request):
    logged_in_student=request.session["session_key"]
    student_logged_in_object=Student.objects.get(password=logged_in_student)
    context={"student_data": student_logged_in_object}
    return render(request,'app/html/student_pro.html')

def signup(request):
    if request.method=='GET':
        return render(request,'app/html/signup.html')
    if request.method=='POST':
        email=request.POST['userid']
        password=request.POST['userpass1']
        re_password=request.POST['re-enter']
        if (password==re_password):
            student=Student(email=email,password=password,re_password=re_password)
            student.save()
            messages.success(request,'successfully sign-up')
            return render (request,'app/main/main.html')
           
        else:
            messages.error(request,'re-enter password not matched')
            return render (request,'app/html/signup.html')
        




def courses(request):
    courses_info_list=Courses_details.objects.all()
    context={
        "courses_data":courses_info_list
    }
    return render (request,'app/html/courses.html',context)

def python(request):
    return render(request,'app/main/python.html')
def ccc(request):
    return render(request,'app/main/ccc.html')
def java(request):
    return render(request,'app/main/java.html')
def main(request):
    return render(request,'app/main/main.html')
def ccc_content(request):
    return render(request,'app/main/ccc_content.html')
def java_content(request):
    return render(request,'app/main/java_content.html')
def python_content(request):
    return render(request,'app/main/python_content.html')
   
