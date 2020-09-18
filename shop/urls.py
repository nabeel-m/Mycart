from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('fashion/',views.fashion,name="fashion"),
    path('fashion/menfashion',views.menfashion,name="menfashion"),
    path('fashion/menfashion/shirts',views.shirts,name="shirts"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('tracker/',views.tracker,name="tracker"),
    path('search/',views.search,name="search"),
    path('productview/',views.productview,name="productview"),
    path('checkout/',views.checkout,name="checkout"),
]