from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[
    path('user/',user,name='user'),
    path('user1/',user1,name='user1'),
]