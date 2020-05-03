from django.db import models


class Roll(models.Model):
    die_1_value = models.IntegerField()
    die_2_value = models.IntegerField()
