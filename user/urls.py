from django.template.context_processors import static
from django.urls import path

from Project2 import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/',views.user_update, name='user_update'),
    path('password/',views.change_password, name='change_password'),
]
