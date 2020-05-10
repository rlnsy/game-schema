from games.logic.api.core import GameLogic
from games.logic.api.errors import (
    ObjectExists,
    MissingModelParameter,
    CalleeKeyError
)
from games.logic.api.models import (
    assert_nexist
)

from .models import Roll

class DiceLogic(GameLogic):

    def default_creator_roles(self):
        return ['Dice_roller']

    def create_action(self, action_type_id, params):
        """
        Should create and instance of Action and return it
        """
        if action_type_id == 'Dice_RollAction':
            try:
                num_shakes = params['num_shakes']
                return assert_nexist(Roll.objects.filter(num_shakes=num_shakes),
                    lambda: Roll(num_shakes=num_shakes))
            except KeyError as k:
                raise MissingModelParameter(k)
            except ObjectExists:
                return Roll.objects.get(num_shakes=num_shakes)
        else:
            raise CalleeKeyError("action_type_id '%s' is invalid" % action_type_id)
