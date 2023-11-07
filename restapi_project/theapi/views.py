
from django.http import HttpResponse
from django.shortcuts import render
from theapi.serializers import NetSchool_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
#class based view
from rest_framework.views import APIView


# ListModelMixin, CreateModelMixin, RetriveModelMixin, UpdateModelMixin, DestroyModelMixin methods
from theapi.models import NetSchool
from theapi.serializers import NetSchool_Serializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class NetList(GenericAPIView, ListModelMixin):
    queryset = NetSchool.objects.all()
    serializer_class = NetSchool_Serializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class NetCreation(GenericAPIView, CreateModelMixin):
    queryset = NetSchool.objects.all()
    serializer_class = NetSchool_Serializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class NetGet(GenericAPIView, RetrieveModelMixin):
    queryset = NetSchool.objects.all()
    serializer_class = NetSchool_Serializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NetUpdate(GenericAPIView, UpdateModelMixin):
    queryset = NetSchool.objects.all()
    serializer_class = NetSchool_Serializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
class NetDestroy(GenericAPIView, DestroyModelMixin):
    queryset = NetSchool.objects.all()
    serializer_class = NetSchool_Serializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        


# Class based view
class NetSchoolCreate(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            # complex data
            net = NetSchool.objects.get(id=id)
            # python dictionary
            netserializer = NetSchool_Serializer(net)
            return Response(netserializer.data)
        
        # complex data
        net = NetSchool.objects.all()
        # python dictionary
        netserializer = NetSchool_Serializer(net, many=True)
        return Response(netserializer.data)
    
    def post(self, request, pk=None, format=None):
        serializer = NetSchool_Serializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'msg': 'Successfully inset data'})
        return Response(serializer.errors)
    
    def put(self, request, pk, format=None):
        id = pk
        net = NetSchool.objects.get(pk=id)
        serializer = NetSchool_Serializer(net, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully update data'})
        return Response(serializer.errors)
    
    def patch(self, request, pk, format=None):
        id = pk
        net = NetSchool.objects.get(pk=id)
        serializer = NetSchool_Serializer(net, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully update partial data'})
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        id = pk
        net= NetSchool.objects.get(pk=id)
        net.delete()
        return Response({'msg': 'Successfully delete data'})
        




# Function Based View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def netschool_create(request, pk=None):
    if request.method=='GET':
        id = pk
        if id is not None:
            # complex data
            net = NetSchool.objects.get(id=id)
            # python dictionary
            netserializer = NetSchool_Serializer(net)
            return Response(netserializer.data)
        
        # complex data
        net = NetSchool.objects.all()
        # python dictionary
        netserializer = NetSchool_Serializer(net, many=True)
        return Response(netserializer.data)
    
    if request.method == 'POST':
        serializer = NetSchool_Serializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'msg': 'Successfully inset data'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = pk
        net = NetSchool.objects.get(pk=id)
        serializer = NetSchool_Serializer(net, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully update data'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = pk
        net = NetSchool.objects.get(pk=id)
        serializer = NetSchool_Serializer(net, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully update partial data'})
        return Response(serializer.errors)
    
    
    if request.method == 'DELETE':
        id = pk
        net= NetSchool.objects.get(pk=id)
        net.delete()
        return Response({'msg': 'Successfully delete data'})
        
