from django.db import models


class Game(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return self.id

class Role(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return "role: %s" % self.id

class ActionType(models.Model):
    type_id = models.CharField(max_length=100, primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return "%s:%s" % (self.game_id, self.type_id)

class Action(models.Model):
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
