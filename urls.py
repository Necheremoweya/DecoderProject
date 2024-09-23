from django.urls import path
from . import views

urlpatterns = [
    path('', views.decode_message, name='decode_message'),
]