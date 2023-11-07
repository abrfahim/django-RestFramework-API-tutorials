from django.contrib import admin
from theapi.models import NetSchool
# Register your models here.


@admin.register(NetSchool)
class NetSchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'course_name', 'duration', 'seat']