from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.index, name='index'),
    path('login_page/', views.index, name='login_page'),
    path('start_page/game_page/', views.index2, name='index2'),
    path('start_page/',views.index3, name = 'index3'),
    path('game_page/', views.game_page, name='game_page'),
    path('game_page/start_page',views.index3, name = 'index3'),
]