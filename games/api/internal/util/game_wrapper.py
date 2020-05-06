from games.logic.exceptions import GameLogicError

def exec_logic(logic_proc, k):
    if not callable(logic_proc):
        raise TypeError("Logic procedure is not callable")
    try:
        result = logic_proc()
    except Exception as e:
        raise GameLogicError(e)
    return k(result)
