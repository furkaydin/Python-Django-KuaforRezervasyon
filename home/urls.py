from django.template.context_processors import static
from django.urls import path

from Project2 import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]