from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home' ),
    path('page1', page1, name='page1'),
    path('page2', page2, name='page2'),
    path('page3', page3, name='page3'),
]

app_name = 'poll'

