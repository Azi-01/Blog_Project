from django.urls import path
from .views import home, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('posts/<str:pk>', post_detail, name='post_detail'),
] 