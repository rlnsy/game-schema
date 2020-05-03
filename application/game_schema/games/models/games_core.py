from django.db import models


class Game(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

class Agent(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

class Role(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

class Action(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    subtype_id = models.CharField(max_length=100, null=False)
