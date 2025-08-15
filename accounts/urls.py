from .views import *
from django.urls import path

urlpatterns = [
    path('user/', get_user, name='get_user'),
    path('user/new/', new_user, name='new_user'),
    path('user/delete/', delete_user, name='delete_user'),
    path('users/', get_all_user, name='get_all_user'),
]
