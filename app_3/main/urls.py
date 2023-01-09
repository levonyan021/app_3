from django.urls import path, include
from .views import *


app_name = 'main'
urlpatterns = [
    path('service/', service, name='service'),
    path('home/', index, name='index'),
    path('about/', about, name='about'),
    path('', home, name='home'),
    path('contact/', contact, name='contact' )
]
