class NotAllowed(Exception):
    pass

class NotFound(Exception):
    pass

class AlreadyHasRole(NotAllowed):
    pass

class GameImplementationError(Exception):
    pass

class MissingRequiredData(Exception):
    pass
    