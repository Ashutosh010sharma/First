from django.contrib import admin
from .models import Courses_details,Student

# Register your models here.
class Courses_details_Admin(admin.ModelAdmin):
    list_display=('course_name','course_discription','lectures_list')
    search_fields=('course_name',)
    list_filter=['course_content']

class Student_Admin(admin.ModelAdmin):
    list_display=('name','email','phone','password')
    search_fields=('password',)
    list_filter=['name']

admin.site.register(Courses_details,Courses_details_Admin)
admin.site.register(Student,Student_Admin)











admin.site.site_header=" Substring Technologies  Portal Administration"
admin.site.site_title="Admin Dashboard"
admin.site.index_title=" Welcome To  Substring Technologies "