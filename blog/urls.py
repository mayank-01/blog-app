from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # For Function Based Views
    path('', views.post_list, name="post_list"),
    path('post-create', views.post_create, name="post_create"),
    path('post-update/<int:id>', views.post_update, name="post_update"),
    path('post-delete/<int:id>', views.post_delete, name="post_delete"),
    path('post-detail/<int:id>', views.post_detail, name="post_detail"),

    # For Middleware Practice
    path('excp/', views.excp),
    path('user/', views.user_info),
]