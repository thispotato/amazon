from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.index , name = 'index'),
    url(r'^product/(?P<product_slug>[-\w]+)/$' , views.product , name= 'products'),
    url(r'^category/(?P<category_slug>[-\w]+)/$' , views.category , name= 'category')
]