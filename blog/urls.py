from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post-_list"),
]# Create your views here.g