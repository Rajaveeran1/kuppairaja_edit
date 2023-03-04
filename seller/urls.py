
from django.urls import path
from .views import ListCategory, DetailCategory,CreateProduct, DetailProduct,Recent_added,Recent_reuest,Multipleimage,Myads,ListProduct
from .views import Recent_added


urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>', DetailCategory.as_view(), name='singlecategory'),


    path('products/', ListProduct.as_view(), name='products'),
    path('listproducts/', ListProduct.as_view(), name='products'),
    path('product-detail/<int:pk>', DetailProduct.as_view(), name='singleproduct'),


    path('recent-added/<int:userid>', Recent_added.as_view(), name='recent-added'),

    #buyerapp module
    path('recent-request/', Recent_reuest.as_view(), name='recent-request'),

    path('my-ads/<int:userid>', Myads.as_view(), name='my-ads'),
    
    path('multipleimages/', Multipleimage.as_view(), name='Multipleimage'),
    


]