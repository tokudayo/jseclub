from . import views
from django.urls import path

urlpatterns = [
    path('training', views.training, name='training'),
    path('event', views.event, name='event'),
]