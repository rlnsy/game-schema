from games.logic.api.errors import (
    MissingModelParameter, ExcessModelParameter)

def require_in(params, fields, k):
    d = {}
    for p in params:
        if p not in fields:
            raise ExcessModelParameter(p)
    for f in fields:
        if f in params:
            d[f] = params[f]
        else:
            raise MissingModelParameter(f)
    return k(d)

from games.api.internal.util.model_ops import assert_nexist
from .models import ObjectExists

def test_exist(query, exist_proc, nexist_proc):
    try:
        return assert_nexist(query, nexist_proc)
    except ObjectExists:
        return exist_proc()
