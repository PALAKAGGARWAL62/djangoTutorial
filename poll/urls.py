from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home' ),
    path('page1', page1, name='page1'),
]

app_name = 'poll'

