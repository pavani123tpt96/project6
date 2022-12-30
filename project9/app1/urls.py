from django.urls import path
from app1.views import *
app_name='something1'

urlpatterns=[
    path('jinja_print/',jinja_print,name='jinja_print'),
    path('detail_view/',detail_view,name='detail_view'),
]