from django.template.context_processors import static
from django.urls import path

from Project2 import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/',views.user_update, name='user_update'),
    path('password/',views.change_password, name='change_password'),
    path('reserve/', views.reserve, name='reserve'),
    path('deletereserve/<int:id>', views.deletereserve, name='deletereserve'),
    path('comments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),

]
