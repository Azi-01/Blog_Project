from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signUpView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', signUpView, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]