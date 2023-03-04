
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from accounts.serializers import RegisterSerializer,UserroleSerializer,RegisterphoneSerializer
from accounts.utils import otp_generator
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions, generics, status
import requests
from accounts.models import Role


User = get_user_model()

# Create your views here.

class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
   # permission_classes = (permissions.IsAuthenticated,)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'response': serializer.data,
            'success': True,
            'message': 'User created successfully',

        })
        




def send_otp(phone):
    """
    This is an helper function to send otp to session stored phones or 
    passed phone number as argument.
    """

    if phone:

        key = otp_generator()
        phone = str(phone)
        otp_key = str(key)

        link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=7c59cf94-d129-11ec-9c12-0200cd936042&to={phone}&from=MMBook&templatename=mymedbook&var1={otp_key}&var2={otp_key}'

        result = requests.get(link, verify=False)

        return otp_key
    else:
        return False


class ValidatePhoneSendOTP(APIView):
    def post(self, request, *agrs, **kwargs):
        try:
            phone_number = request.data.get('phone')

            if phone_number:
                phone = str(phone_number)
                user = User.objects.filter(phone__iexact=phone)
              

                if user.exists():
                   # global data,old_otp,new_otp
                    data = user.first()
                    old_otp = data.otp
                    new_otp = send_otp(phone)
                    if old_otp:
                        data.otp = new_otp
                        data.save()
                        return Response({
                            'success':True,  
                            'message': 'OTP sent successfully',
                            'otp':data.otp,
                        })
                    
                    else:
                        data.otp = new_otp
                        data.save()
                        return Response({
                            'success':True,  
                            'message': 'OTP sent successfully',
                            'otp':data.otp,
                        })

                else:
                    data = user.first()
                    serializer = RegisterphoneSerializer(data=request.data)
                    serializer.is_valid()
                    serializer.save()
                    data.otp = new_otp
                    data.save()
                    return Response({
                                'success':True,
                                'message': 'User Register Success',
                                'otp':data.otp,
                               })
            else:
                return Response({
                    'success':False,  
                    'message': 'Phone number is required',
                   
                })
        except Exception as e:
            return Response({
                'message': str(e),
             
            })


# verify otp
class VerifyPhoneOTPView(APIView):
    def post(self, request, format=None):
        try:
            phone = request.data.get('phone')
            otp = request.data.get('otp')
            print(phone, otp)

            if phone and otp:
                user = User.objects.filter(phone__iexact=phone)
                if user.exists():
                    user = user.first()
                    if user.otp == otp:
                        login(request, user)
                        return Response({
                            'success': True,
                            'message': 'Login Successfully',
                            'token': AuthToken.objects.create(user)[1],
                            'response': {
                                'id': user.userid,
                                'name': user. business_name,
                                'email': user.email,
                                'phone': user.phone,
                                'address': user.address,
                                'city': user.city,
                                'userrole':user.userrole,
                            }})
                    else:
                        return Response({'message': 'OTP does not match'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Phone or OTP is missing'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                'success': False,
                'message': str(e),
                'details': 'Login Failed'
            })


# logout api view
class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        try:
            if request.User.auth_token:
                return Response({

                'token':request.User.auth_token.delete(),
                'success':True,  
                'message': 'Logout successfully',
            })
        except Exception as e:
            return Response({
                'success':False,  
                'message': str(e),
              
            })


class Setuserrole(generics.GenericAPIView):
      serializer_class=UserroleSerializer
      #permission_classes = (permissions.IsAuthenticated,)

      def put(self, request,id):
         user=get_object_or_404(User,pk=id)
         
         serializer=self.serializer_class(instance=user,data=request.data)
         
         if serializer.is_valid():
            serializer.save()

            return Response({
                    'success':True,  
                    'message': 'UserType Set SuccessFully',
                
                })
  
         return Response({
                    'success':False,  
                    'message': serializer.errors,
                    'status': status.HTTP_400_BAD_REQUEST,
                })
 