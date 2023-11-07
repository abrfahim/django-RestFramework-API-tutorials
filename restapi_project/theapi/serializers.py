from rest_framework import serializers
from theapi.models import NetSchool

class NetSchool_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NetSchool
        fields =['id','teacher_name', 'course_name', 'duration', 'seat']


# class NetSchool_Serializer(serializers.Serializer):
#     teacher_name = serializers.CharField(max_length=25)
#     course_name = serializers.CharField(max_length=20)
#     duration = serializers.IntegerField()
#     seat = serializers.IntegerField()
    
#     def create(self, validate_data):
#         return NetSchool.objects.create(**validate_data)
    
#     def update(self, instance, validated_data):
#         instance.duration = validated_data.get('duration', instance.duration)
        
#         instance.save()
#         return instance