from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_page/game_page/', views.index2, name='index2'),
    path('start_page/',views.index3, name = 'index3')
]