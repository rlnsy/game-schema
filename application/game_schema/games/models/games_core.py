from django.db import models


class Game(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return "game: %s" % self.id

class Role(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return "role: %s" % self.id

class Action(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    subtype_id = models.CharField(max_length=100, null=False)
    def __str__(self):
        return "action (%s): %s" % (self.game_id, self.subtype_id)
