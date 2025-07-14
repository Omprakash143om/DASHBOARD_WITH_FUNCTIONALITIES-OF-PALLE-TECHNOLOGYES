from django.contrib import admin
from .models import Student, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)