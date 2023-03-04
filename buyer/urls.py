
from django.urls import path
from .views import Listslide, ListCategory,ListMyrequest,ListFcategory,subcategoryView,ListFcategory
from seller.views import Popular,Recent_added #seller app popular view


urlpatterns = [
    path('slide/', Listslide.as_view(), name='slide'),

    path('categories/', ListCategory.as_view(), name='category'),
    path('listFcategory/', ListFcategory.as_view(), name='ListFcategory'),
    #seller request view
    path('my-request/', ListMyrequest.as_view(), name='myquest'),

    path('sub-categories/<int:id>', subcategoryView.as_view(), name='subcatagory'),

    path('get-Fcategories/1', Popular.as_view(), name='popular'), #connect seller app view
    path('get-Fcategories/2', Recent_added.as_view(), name='new-recommentation'),
    #path('get-categories/3/', Recent_added.as_view(), name='new-recommentation'),

    

    


]