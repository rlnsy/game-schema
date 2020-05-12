from django.db import models
from .games_core import Game, Role
from .games_players import Agent


class Session(models.Model):
    creator_agent_id = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    time_init = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s:%s: %s" % (self.time_init, self.creator_agent_id, self.game_id)


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

class SessionEnd(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    time_at = models.DateTimeField(auto_now_add=True)

class Does(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    agent_role_id = models.ForeignKey(HasRole, on_delete=models.CASCADE)
