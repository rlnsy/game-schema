from games.logic import logic_api

from .models import Roll

class DiceLogic(logic_api.GameLogic):

    def default_creator_roles(self):
        return ['Dice_roller']

    def create_action(self, action_type_id, params):
        """
        Should create and instance of Action and return it
        """
        if action_type_id == 'Dice_RollAction':
            try:
                num_shakes = params['num_shakes']
                return logic_api.assert_nexist(Roll.objects.filter(num_shakes=num_shakes),
                    lambda: Roll(num_shakes=num_shakes))
            except KeyError as k:
                raise logic_api.MissingModelParameter(k)
            except logic_api.ObjectExists:
                return Roll.objects.get(num_shakes=num_shakes)
        else:
            raise logic_api.CalleeError("action_type_id '%s' is invalid" % action_type_id)
