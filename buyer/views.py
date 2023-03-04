from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework import serializers
from .models import Category,Slide,Myrequest,Fcategory,SubCategory
from .serializers import CategorySerializer, SlideSerializer,MyrequestSerializer,FcategorySerializer,ScategorySerializer
from rest_framework.response import Response
from rest_framework import permissions, generics, status

# Create your views here.


class Listslide(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = SlideSerializer(queryset, many=True)
        return Response({
                'success':True,
                'message': 'Slide_list',
                'response':serializer.data,
                
                              })




class ListCategory(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response({
                'success':True,
                'message': 'category_list',
                'response':serializer.data,
                
                              })




class subcategoryView(generics.GenericAPIView):
    serializer_class=ScategorySerializer
    queryset=SubCategory.objects.all()

    def get(self,request,id):
        categorys=Category.objects.get(pk=id)

        scat=SubCategory.objects.all().filter(CategoryId=categorys)

        serializer=self.serializer_class(instance=scat,many=True)

        return Response({
                'success':True,
                'message': 'Subcategory_list',
                'response':serializer.data,
                
                              })




class ListMyrequest(generics.ListCreateAPIView):    
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Myrequest.objects.all()
    serializer_class = MyrequestSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = MyrequestSerializer(queryset, many=True)
        return Response({
                'success':True,
                'message': 'MyRequest_list',
                'response':serializer.data,
                
                              })



class DetailMyrequest(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = (permissions.IsAuthenticated,)
    queryset = Myrequest.objects.all()
    serializer_class = MyrequestSerializer


class ListFcategory(generics.ListCreateAPIView):    
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Fcategory.objects.all()
    serializer_class = FcategorySerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = FcategorySerializer(queryset, many=True)
        return Response({
                'success':True,
                'message': 'Fcategory_list',
                'response':serializer.data,
                
                              })


