from django.urls import path
from .views import user_login, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('user_login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register')
]
