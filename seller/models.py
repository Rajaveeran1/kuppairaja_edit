from django.db import models
from buyer.models import Category,SubCategory


from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.   

class Product(models.Model):
    productdetails = models.TextField(max_length=1000, null=True,default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    item = models.ForeignKey(SubCategory,blank=True, on_delete=models.PROTECT,default=1, related_name='subcategory')
    kilograms = models.IntegerField(default='')
    #item=models.ManyToManyField(SubCategory, related_name="category")
    price = models.FloatField(default='') 
    phoneno = models.CharField(max_length=10,default='')
    address = models.TextField(blank=True, default='')
    date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='',max_length=25)
    favourite = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    userid = models.ForeignKey(User, on_delete = models.CASCADE, blank = True,default='')
    latitude = models.FloatField(default=11.749710927476007)
    longitude= models.FloatField(default=79.76045317140348)


  
    def __str__(self):
        return self.productdetails 
    

class MultipleImages(models.Model):
    scrapimageid=models.AutoField(primary_key=True)
    scrapid = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "images")
    scrapimage= models.ImageField(upload_to="images/", blank=True,null=True)

