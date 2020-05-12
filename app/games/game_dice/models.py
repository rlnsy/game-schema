from games.logic.api.models import IntegerField, Action


class Roll(Action):
    #die_1_value = models.IntegerField()
    #die_2_value = models.IntegerField()
    num_shakes = IntegerField()
