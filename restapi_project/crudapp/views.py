from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from crudapp.models import Operation_Execution
from crudapp.serializers import Operation_Execution_Serializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
# Create your views here.

# ListCreateAPIView, RetrieveUpdateDestroyAPIView methods

class NewOperation(ListCreateAPIView):
    queryset = Operation_Execution.objects.all()
    serializer_class = Operation_Execution_Serializer
    
class NextOperation(RetrieveUpdateDestroyAPIView):
    queryset = Operation_Execution.objects.all()
    serializer_class = Operation_Execution_Serializer
    
    
# Model View Set

class MultiOperation(viewsets.ModelViewSet):
    # list, create, update, partial update, delete
    queryset = Operation_Execution.objects.all()
    serializer_class = Operation_Execution_Serializer
    permission_classes = [IsAdminUser]