from django.db import models
from .games_core import Agent

class Player(models.Model):
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    token = models.CharField(max_length=50, blank=False, null=False) # fixed length 50
