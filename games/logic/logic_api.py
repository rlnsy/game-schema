from games.logic.logic_interface import GameLogic

class CalleeError(Exception):
    pass

class ModelParameterError(CalleeError):
    pass

class MissingModelParameter(ModelParameterError):
    def __init__(self, key):
        if key is None:
            raise TypeError("Bad key arg cannot be null")
        else:
            msg = "Missing parameter '%s'" % str(key)
            super(MissingModelParameter, self).__init__(msg)

class CalleeKeyError(CalleeError):
    pass

from games.api.internal.util.model_ops import assert_nexist
from games.api.internal.exceptions import NotAllowed as ObjectExists
