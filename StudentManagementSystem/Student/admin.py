from django.contrib import admin
from Student.models import Student

# Register your models here.

class StudentModel(admin.ModelAdmin):
    list_display = ["id", "student_number", "first_name", "last_name", "email", "field_of_study", "gpa"]
    ordering = ["id"]

admin.site.register(Student, StudentModel)
