from django.db import models


from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Slide(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)



class Category(models.Model):
    #categoryId=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/",default="", null=True, blank=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=200)
   # categorys = models.ManyToManyField(Category, related_name="category")
    CategoryId=  models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)


    def __unicode__(self):
        return self.title


#populor/new-recomentations
class Fcategory(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/",default="", null=True, blank=True)

    
    def __str__(self):
        return self.title



class Myrequest(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='myreguest')
    item = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='item')
    kilograms = models.IntegerField(blank=True, null=True,)
    phone_no = models.CharField(max_length=10,blank=True, null=True,)
    description = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to="images/",  blank = True, null=True, default='')
    date=models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(User, on_delete = models.CASCADE, blank = True,default='')
    latitude = models.FloatField(null=True)
    longitude= models.FloatField(null=True)
  
   

