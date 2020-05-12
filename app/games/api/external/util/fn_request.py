from rest_framework.views import Response
from . import http_status as status
from django.core.exceptions import ObjectDoesNotExist


def req_fields(request, field_names, k):
    d = {}
    for f in field_names:
        if f in request.data:
            d[f] = request.data[f]
        else:
            return Response("Missing field '%s' in request" % f, status=status.CLIENT_BAD_REQUEST)
    return k(d)

def req_params(request, param_names, k):
    p = {}
    for n in param_names:
        if n in request.query_params:
            p[n] = request.query_params[n]
        else:
            raise Exception("Missing expected query param '%s'" % n)
    return k(p)
