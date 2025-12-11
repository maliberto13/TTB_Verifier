
from django.urls import path
from . import views

app_name = 'verifier'
urlpatterns = [
    path('', views.base, name='base'),
    path('upload', views.upload, name='upload'),
]
