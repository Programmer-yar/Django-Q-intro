from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.test, name="test1"),
    path('2', views.index, name="test2"),
    path('3', views.with_django_q, name='test3'),
]
