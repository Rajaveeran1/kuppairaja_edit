from rest_framework import serializers
from .models import Category, Product,MultipleImages
from buyer.serializers import ScategorySerializer,CategorySerializer




class MultipleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleImages
        fields = [
            'scrapid',
            'scrapimageid',
            'scrapimage'
        ]


class ProductSerializer(serializers.ModelSerializer):
    images = MultipleImageSerializer(many=True, read_only=True)
    #category = CategorySerializer(many=True, read_only=True)
    #item = ScategorySerializer(many=True, read_only=True)
    #category = serializers.StringRelatedField()
    uploadedImages = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)
    
    
    class Meta:
        model = Product
        fields = [ 
                  'id', 
                  "productdetails",
                  'category',
                  'kilograms',
                  "price",
                  'phoneno',
                  'address',
                  'item',
                  'date',
                  'userid',
                  'images',
                  'latitude',
                  'longitude',
                  'likes',
                  'views',
                  'favourite',
                  'status',
                  'uploadedImages'
          ]
            #optional_fields = ['uploaded_images', ]
            
        extra_kwargs = {
            "latitude" : {"required":False},
            "longitude" : {"required":False},


            
        }
    def to_representation(self, instance):
        rep = super(ProductSerializer, self).to_representation(instance)
        rep['category'] = instance.category.title
        return rep
    
    def to_representation(self, instance):
        rep = super(ProductSerializer, self).to_representation(instance)
        rep['item'] = instance.item.title
        return rep
    
    def create(self, validated_data):
        uploadedImages = validated_data.pop("uploadedImages")
        scrapid = Product.objects.create(**validated_data)
        for scrapimage in uploadedImages:
            newproductImage = MultipleImages.objects.create(scrapid=scrapid, scrapimage=scrapimage)
        return scrapid
        



      