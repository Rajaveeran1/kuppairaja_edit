
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
#from rest_framework import permissions
from rest_framework import serializers
from .models import Category, Product, MultipleImages
from buyer.models import Myrequest, Fcategory#buyerapp,purpose for popular
from buyer.serializers import MyrequestSerializer, FcategorySerializer#buyerapp
from .serializers import CategorySerializer, ProductSerializer,MultipleImageSerializer
from rest_framework import permissions, generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from .models import Product
from rest_framework.views import APIView


from django.contrib.auth import get_user_model

User=get_user_model()



  #my scrabs views
class Myads(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def get(self,request,userid):
        userid=User.objects.get(pk=userid)
        
        myproperty=Product.objects.all().filter(userid=userid)

        serializer=self.serializer_class(instance=myproperty,many=True)

        return Response({
            'scucess': True,
            'message': 'My Ads List',
            'response': serializer.data,

        })


class ListCategory(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# create post

class ListProduct(generics.ListCreateAPIView):    
   # permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #filter the product
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['product_details']
    ordering_fields = ['kilograms']
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        total= Product.objects.count()
    
        return Response({
                'success':True,
                'message': 'scrap_list',
                'totalScrap':total,
                'response':serializer.data,
                
                              })



class CreateProduct(generics.GenericAPIView):
    def post(self, request, *agrs, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success':True,
                'message': 'Post Create SuccessFully',
               # 'response':serializer.data
                          })
        


                        
class DetailProduct(generics.RetrieveUpdateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer



"""
class DetailProduct(APIView):

    def post(self,request,*args, **kwargs):
        id = request.data.get('id')
        products = Product.objects.filter(id__iexact=id)
        serializer = ProductSerializer()
        if products.exists():
                 return Response({
                'success':True,
                'message': 'Detail Scrap',
                'status': status.HTTP_200_OK,
                'response':serializer.data
                              })
      
          
        else:
                 return Response({
                'success':True,
                'message': 'ScrapId exits',
                'status': status.HTTP_400_BAD_REQUEST,
                }
            )

      """  
        


class Recent_added(generics.GenericAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def get(self,request,userid):
        userid=User.objects.get(pk=userid)
        
        myproperty=Product.objects.all().filter(userid=userid).order_by('-id')[:10]

        serializer=self.serializer_class(instance=myproperty,many=True)

        return Response({
            'scucess': True,
            'message': 'reced-added-List',
            'response': serializer.data,

        })
    
"""
class Recent_added(generics.ListCreateAPIView):
     #permission_classes = (permissions.IsAuthenticated,)
     queryset = Product.objects.all().order_by('-id')[:10]
     serializer_class = ProductSerializer

     def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response(data)"""

class Recent_reuest(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
     queryset = Myrequest.objects.all().order_by('-id')[:10]
     serializer_class = MyrequestSerializer

     def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response({
            'scucess': True,
            'message': 'Recent Reuest List',
            'response': serializer.data,

        })
      

class Popular(generics.ListCreateAPIView):
     #permission_classes = (permissions.IsAuthenticated,)
     queryset = Product.objects.all().order_by('-kilograms')[:10]
     serializer_class = ProductSerializer

     def get(self, request):
       
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response(data)


#multiple images save
class Multipleimage(generics.GenericAPIView):
    def post(self, request, *agrs, **kwargs):
        serializer = MultipleImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success':True,
                'message': 'Image Upload SuccessFully',
                'response':serializer.data
                          })
        

