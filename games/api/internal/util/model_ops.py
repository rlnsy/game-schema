from ..exceptions import NotAllowed, NotFound
from django.core.exceptions import ObjectDoesNotExist


def assert_nexist(queryset, k):
    if queryset.count() == 0:
        return k()
    else:
        raise NotAllowed("Object already exists")


def get_by_id(model, id, k):
    try:
        o = model.objects.get(pk=id)
        return k(o)
    except ObjectDoesNotExist:
        raise NotFound("Could not find %s with id '%s'" % (str(model), id))
