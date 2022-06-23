from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'food', views.FoodView)

urlpatterns = [
    path('home', views.home, name='home'),
    path('allproducts', views.get_all_products, name='get_all_products'),
    path('allmobiles', views.get_all_mobiles, name='get_all_mobiles'),
    path('create', views.post_Product, name = 'post_Product' ),

    path('product/<int:id>', views.product_details, name ='product_details' ),





   
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))


]