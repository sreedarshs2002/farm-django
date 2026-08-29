from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('cows',views.cows,name='cows'),
    path('products',views.products,name='products'),
    path('gallery',views.gallery,name='gallery'),
    path('messages',views.messag,name='messages'),
  

]