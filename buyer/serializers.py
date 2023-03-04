from rest_framework import serializers
from .models import Slide,Category,Myrequest,Fcategory,SubCategory
from seller.models import MultipleImages

#topbar_slide
class SlideSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Slide
        fields = ["id","image"]



class CategorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField( max_length = None,allow_null = False, use_url=True, required =False)
    class Meta:
        model = Category
        fields = ["id", "title","image",]



class FcategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fcategory
        fields = ["id","title","image"]



class ScategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ['id',"title"]




class MultipleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleImages
        fields = [
            'scrapimageid',
            'scrapimage'
        ]



class MyrequestSerializer(serializers.ModelSerializer):
    #images = MultipleImageSerializer(many=True, read_only=True,required=False) 
    
    class Meta:
        model = Myrequest
        fields = [ 
                  'id', 
                  'category',
                  'item',
                  'kilograms',
                  'phone_no',
                  'description',
                  #"images",
                  'latitude',
                  'longitude',
                  'userid',
          ]
    
    def create(self, validated_data):

        return Myrequest.objects.create(**validated_data)

