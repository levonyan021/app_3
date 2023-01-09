from django.urls import path, include
from .views import index, about, home, service


app_name = 'main'
urlpatterns = [
    path('service/', service, name='service'),
    path('home/', index, name='index'),
    path('about/', about, name='about'),
    path('', home, name='home'),
]
