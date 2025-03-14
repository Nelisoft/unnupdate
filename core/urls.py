from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('create/', views.createPost, name='create'),
    path('contact/', views.Contact, name='contact'),
    path('<str:slug>/',views.PostDetails, name='post-details'),
    path('<slug:slug>/add-comment', views.Add_comment, name ='add-comment'),
   
]
