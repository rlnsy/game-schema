from games.models.games_core import ActionType, Action
from .util.model_ops import get_by_id
from games.logic.logic_dispatch import find as find_logic
from games.logic.game_wrapper import exec_logic
from rest_framework import serializers
from .exceptions import GameImplementationError, NotFound

class ActionTypeSerializer(serializers.HyperlinkedModelSerializer):
    game_id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    class Meta:
        model = ActionType
        fields = ['type_id', 'game_id']

def list_action_types():
    action_types = ActionType.objects.all()
    return list([ActionTypeSerializer(t).data for t in action_types])

def manifest_action(action_type_id, params):
    def verify_action_object(a):
        if not isinstance(a, Action):
            raise GameImplementationError("create_action returned a non-Action")
        action_id = a.pk
        try:
            get_by_id(Action, action_id,
                lambda a:
                    {
                        'message': "Action record created",
                        'action_id': action_id
                    })
        except NotFound:
            raise GameImplementationError("create_action did not save action")
    def dispatch(t):
        game_id = t.game_id.pk
        return find_logic(game_id,
            lambda l: 
            exec_logic(lambda: l.create_action(action_type_id, params), verify_action_object))
    return get_by_id(ActionType, action_type_id, dispatch)


def list_actions():
    actions = Action.objects.all()
    def serialize(a):
        return {
            'action_id': a.pk,
            'type_id': a.action_type.pk
        }
    return list([serialize(a)for a in actions])
