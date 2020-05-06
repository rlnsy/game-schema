from .exceptions import LogicNotImplemented

class GameLogic:

    def default_creator_roles(self):
        return []

    def create_action(self, action_type_id, params):
        """
        Should create and instance of Action, save it to the database, and return it
        """
        raise LogicNotImplemented("create_action must be overidden by Logic class")

    def get_action(self, action_type_id, action_id):
        raise LogicNotImplemented("get_action must be overidden by Logic class")
