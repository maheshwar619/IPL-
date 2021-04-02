from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path('upload/', views.profile_upload, name='upload'),
    path('home/', views.home, name='home'),
    # path('displaytrans/', views.displaytrans, name='displaytrans'),
    path('population-chart/', views.population_chart, name='population-chart'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('maximum_player_match/', views.maximum_player_match, name='maximum_player_match'),
    path('toss_winner/', views.toss_winner, name='toss_winner'),
    path('winner/', views.winner, name='winner'),

]