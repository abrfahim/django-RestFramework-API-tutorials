from rest_framework import serializers
from crudapp.models import Operation_Execution

class Operation_Execution_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Operation_Execution
        fields =['id','teacher_name', 'course_name', 'duration', 'seat']
