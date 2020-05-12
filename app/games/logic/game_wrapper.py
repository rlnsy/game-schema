from .exceptions import (
    GameLogicError, 
    LogicNotImplemented
)
from games.api.internal.exceptions import MissingRequiredData
from .api.errors import ModelParameterError, CalleeError

def exec_logic(logic_proc, k):
    if not callable(logic_proc):
        raise TypeError("Logic procedure is not callable")
    try:
        result = logic_proc()
    except LogicNotImplemented as e:
        raise e
    except Exception as e:
        if isinstance(e, ModelParameterError):
            raise MissingRequiredData(e)
        elif isinstance(e, CalleeError):
             raise e
        else:
            raise GameLogicError(e)
    return k(result)
