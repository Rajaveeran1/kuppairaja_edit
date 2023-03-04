
import imp
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Role,User


User = get_user_model()

# Create your serializers here.

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["userid", "business_name", "phone" ,"email","address","city","state","country","image",'zipcode']
        extra_kwargs = {
            "userid": {"read_only": True},
            "business_name": {"required": True},
            "phone": {"required": True},
            "email": {"required": True},
        }

"""
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user"""


class RegisterphoneSerializer(serializers.ModelSerializer):
  
        
     class Meta:
        model = User
        fields = ["userid", "phone"]
        extra_kwargs = {
            "userid": {"read_only": True},
            "phone": {"required": True},
            "business_name": {"required": False},
            "email": {"required": False},
        }

"""
class RegisterphoneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["userid", "phone"]
        extra_kwargs = {
            "userid": {"read_only": True},
            "phone": {"required": True},
            "business_name": {"required": False},
            "email": {"required": False},
        }


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user"""


"""class UserroleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "userrole" ]
        extra_kwargs = {
            "userrole": {"required": True}, #required fields
        }

      
    def create(self, validated_data):

        return User.objects.create(**validated_data)"""



class UserroleSerializer(serializers.ModelSerializer):
    userrole = serializers.CharField(max_length=25)
  
    class Meta:
        model=User
        fields = [ "userrole" ]
 