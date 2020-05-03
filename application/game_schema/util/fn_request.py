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


def assert_nexist(queryset, k):
    if queryset.count() == 0:
        return k()
    else:
        return Response("Object already exists", status=status.CLIENT_FORBIDDEN)


def get_by_id(model, id, k):
    try:
        o = model.objects.get(pk=id)
        return k(o)
    except ObjectDoesNotExist:
        return Response("Could not find %s with id '%s'" % (str(model), id), 
                            status=status.CLIENT_NOT_FOUND)
