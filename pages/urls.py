from django.urls import path
from .views import home, post_detail, delete_comment

urlpatterns = [
    path('', home, name='home'),
    path('posts/<str:pk>', post_detail, name='post_detail'),
    path('delete_comment/<str:pk>', delete_comment, name='delete_comment'),
] 