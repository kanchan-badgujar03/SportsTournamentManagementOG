from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sports/', views.sports_list, name='sports_list'),
    path('add_sports/', views.add_sports, name='add_sports'),
    path('added_sports/', views.added_sports, name='added_sports'),
    path('players/', views.players_list, name='players_list'),
    path('result/', views.result, name='result'),
    path('sports/new/', views.sport_create, name='sport_create'),
    path('events/new/', views.event_create, name='event_create'),
    path('scores/new/', views.score_create, name='score_create'),
    path('football/', views.football_view, name='football'),
    path('add_team/', views.add_team, name='add_team'),
    path("add_game/", views.add_game, name="add_game"),
    path("teams/", views.manage_teams, name="manage_teams"),
    path("fdetails/", views.fdetails, name="fdetails"),
    path("bdetails/", views.bdetails, name="bdetails"),
    path("basketball/", views.basketball_view, name="basketball"),
    path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("update_sports_score/", views.update_sports_score, name="update_sports_score"),
    path("upload-page/", views.upload_page, name="upload_page"),
    path("schedule/", views.view_schedule, name="view_schedule"),
    
]
