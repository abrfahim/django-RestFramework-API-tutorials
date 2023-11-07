from django.contrib import admin
from crudapp.models import Operation_Execution
# Register your models here.

@admin.register(Operation_Execution)
class Operation_Execution_Admin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'course_name', 'duration', 'seat']