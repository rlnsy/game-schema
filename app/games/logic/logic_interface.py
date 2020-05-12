from .exceptions import LogicNotImplemented

class GameLogic:

    def default_creator_roles(self):
        """
        Should return a list of the ids for roles
        that the creator of a game session adopts by
        default.
        """
        return []

    def create_action(self, action_type_id, params):
        """
        Should create an instance of Action and return it
        """
        raise LogicNotImplemented("create_action must be overidden by Logic class")

    def is_legal(self, role_id, action, state_index):
        """
        Should return True if the given role_id is allowed to
        perform action at the given state no. and
        False otherwise
        """
        raise LogicNotImplemented("is_legal must be overidden by Logic class")

    def role_does(self, role_id, action, state_index):
        """
        Should update internal state at the given index based
        on the given role performing action.
        """
        raise LogicNotImplemented("role_does must be overidden by Logic class")

    def is_terminal(self, state_index):
        """
        Should return True if the state at given index
        is a terminal state, False otherwise.
        """
        raise LogicNotImplemented("is_terminal must be overidden by Logic class")
