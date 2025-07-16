from django.db import models
from baji10.models_config import BaseModel

class GameCategory(BaseModel):

    name = models.CharField(max_length=255)



class Tournament(BaseModel):
    name = models.CharField(max_length=255)




class Game(BaseModel):
    game_category = models.CharField(max_length=255)
    tournament = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    team1 = models.CharField(max_length=255)
    team2 = models.CharField(max_length=255)
    game_status = models.CharField(max_length=50, default="Upcoming")
    start = models.DateTimeField()
    end = models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=50, default="Deactive")




class GameQuestion(BaseModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='question')
    question = models.CharField(max_length=255)
    end = models.DateTimeField()




class QuestionAnswer(BaseModel):
    question = models.ForeignKey(GameQuestion, on_delete=models.CASCADE, related_name='answer')
    answer = models.CharField(max_length=255)
    rate = models.FloatField(default=1)
    bets = models.IntegerField(default=0)
    multi = models.IntegerField(default=0)
    possible_return = models.FloatField(default=0)

