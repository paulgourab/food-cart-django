from django.urls import path, include

from foodcart import views

urlpatterns = [
    path('', views.home, name='Home'),
]
