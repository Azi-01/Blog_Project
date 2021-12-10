from django.urls import path
from .views import home, post_detail, delete_post, delete_comment, create_post

urlpatterns = [
    path('', home, name='home'),
    path('posts/<str:pk>', post_detail, name='post_detail'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<str:pk>/delete/', delete_post, name='delete_post'),
    path('delete_comment/<str:pk>', delete_comment, name='delete_comment'),
] 