from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post-create', views.PostCreateView.as_view(), name="post_create"),
    path('post-update/<int:id>', views.PostUpdateView.as_view(), name="post_update"),
    path('post-delete/<int:id>', views.PostDeleteView.as_view(), name="post_delete"),
    path('post-detail/<int:id>', views.PostDetailView.as_view(), name="post_detail"),
]