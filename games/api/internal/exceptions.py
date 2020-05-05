class NotAllowed(Exception):
    pass

class NotFound(Exception):
    pass

class AlreadyHasRole(NotAllowed):
    pass

class GameLogicError(Exception):

    def __init__(self, e):
        msg = "An error occurred in game logic"
        if e is not None:
            msg = msg + ": %s" % str(e)
        super(GameLogicError, self).__init__(msg)

class LogicKeyError(GameLogicError):

    def __init__(self, key):
        if key is None:
            raise TypeError("Bad key arg cannot be null")
        else:
            msg = "Unresolved id '%s'" % str(key)
            super(LogicKeyError, self).__init__(msg)
    