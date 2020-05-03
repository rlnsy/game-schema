from rest_framework.views import Response
from . import http_status as status


def req_fields(request, field_names, k):
    d = {}
    for f in field_names:
        if f in request.data:
            d[f] = request.data[f]
        else:
            return Response("Missing field '%s' in request" % f, status=status.CLIENT_BAD_REQUEST)
    return k(d)


def assert_nexist(queryset, k):
    if queryset.count() == 0:
        return k()
    else:
        return Response("Object already exists", status=status.CLIENT_FORBIDDEN)

