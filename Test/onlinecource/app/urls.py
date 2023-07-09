from django.urls import path,include
from.import views
urlpatterns = [
     path("",views.home,name='home' ),
     path("login/",views.login,name="login"),
     path("signup/",views.signup,name="signup"),
     path("courses/",views.courses,name="courses"),
     path("student_pro/",views.student_pro,name="student_pro"),
     path("python/",views.python,name="python"),
     path("java/",views.java,name="java"),
     path("ccc/",views.ccc,name="ccc"),
     path("main/",views.main,name="main"),
     path("ccc_content/",views.ccc_content,name="ccc_content"),
     path("java_content/",views.java_content,name="java_content"),
     path("python_content/",views.python_content,name="python_content"),
]