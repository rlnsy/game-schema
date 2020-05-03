from django.db import models
from .games_core import Game, Agent, Role


class Session(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    time_init = models.DateTimeField(auto_now_add=True)


"""
NOTE:
Since composite keys are not yet supported in Django,
we opt for a default integer key
"""

class HasRole(models.Model):
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=False)

class State(models.Model):
    state_index = models.IntegerField(null=False)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)

class Terminal(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    time_at = models.DateTimeField(auto_now_add=True)

class Does(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    agent_role_id = models.ForeignKey(HasRole, on_delete=models.CASCADE)
