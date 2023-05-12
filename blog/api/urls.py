from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.GetAllPosts, name="posts"),
    path('createnewpost/', views.CreatePost, name="createPost"),
    path('deletepost/', views.DeletePost, name="deletePost"),

]
