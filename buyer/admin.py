from django.contrib import admin
from .models import Category,Slide,Myrequest,Fcategory,SubCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(Myrequest)

admin.site.register(Slide)

admin.site.register(Fcategory)
admin.site.register(SubCategory)


