from games.logic.api.core import GameLogic
from games.logic.api import errors, models, assertions

from .models import Roll

class DiceLogic(GameLogic):

    def default_creator_roles(self):
        return ['Dice_roller']

    def create_action(self, action_type_id, params):
        """
        Should create and instance of Action and return it
        """
        if action_type_id == 'Dice_RollAction':
            def create(num_shakes):
                return assertions.test_exist(
                    Roll.objects.filter(num_shakes=num_shakes),
                    lambda: Roll.objects.get(num_shakes=num_shakes),
                    lambda: Roll(num_shakes=num_shakes))
            return assertions.require_in(
                params,
                ['num_shakes'],
                lambda d: create(d['num_shakes']))
        else:
            raise errors.CalleeKeyError("action_type_id '%s' is invalid" % action_type_id)
