from django.urls import path
from . import views

app_name = "game_control"

urlpatterns = [
    path('bet-control/', views.bet_control, name="bet_control"),
    path('game-category/', views.game_category, name="game_category"),
    path('tournament/', views.tournament, name="tournament"),
    path('bet-control/add-game/', views.add_game, name="add_game"),
    path('bet-control/add-game-question/<int:pk>/', views.add_question, name="add_game_question",),
    path('bet-control/add-game-question-answer/<int:pk>/', views.add_answer, name="add_game_question_answer",),
]