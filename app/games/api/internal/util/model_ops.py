from ..exceptions import NotAllowed, NotFound
from django.core.exceptions import ObjectDoesNotExist


def assert_nexist(queryset, k):
    if queryset.count() == 0:
        return k()
    else:
        raise NotAllowed("Object already exists")

def assert_exist(queryset, k, error_msg="No matching object"):
    if queryset.count() > 0:
        return k()
    else:
        raise NotFound(error_msg)


def get_by_id(model, id, k):
    try:
        o = model.objects.get(pk=id)
        return k(o)
    except ObjectDoesNotExist:
        raise NotFound("Could not find %s with id '%s'" % (str(model), id))

def remove_by_id(model, id, k):
    def exec(o):
        o.delete()
        return k()
    return get_by_id(model, id, exec)
