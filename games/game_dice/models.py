from django.db import models
from games.models.games_core import Action


class Roll(Action):
    die_1_value = models.IntegerField()
    die_2_value = models.IntegerField()
