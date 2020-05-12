from django.db import models

import string

class Agent(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return self.id


PLAYER_TOKEN_LENGTH = 50
PLAYER_TOKEN_CHARS = [c for c in string.printable if c not in string.whitespace]

class Player(models.Model):
    agent_id = models.OneToOneField(Agent, on_delete=models.CASCADE, primary_key=True)
    display_name = models.CharField(max_length=50)
    token = models.CharField(max_length=50, blank=False, null=False) # fixed length 50
    def __str__(self):
        return "%s (%s)" % (self.display_name, self.agent_id)
