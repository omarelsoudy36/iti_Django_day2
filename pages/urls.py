from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'), # الرابط الرئيسي الفاضي للمنيو
    path('rps/', views.rps_game, name='rps'),
    path('guess/', views.guess_game, name='guess'),
    path('lucky/', views.lucky_game, name='lucky'),
]
