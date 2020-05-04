from rest_framework.views import Response
from . import http_status as status
from games.api.internal import exceptions
import logging
import traceback

def _respond(msg, status_code):
    return Response(
        data=msg,
        status=status_code
    )

def _parse_exn(e):
    msg = str(e)
    def res(status):
        return _respond(msg, status)
    if isinstance(e, exceptions.NotAllowed):
        return res(status.CLIENT_FORBIDDEN)
    if isinstance(e, exceptions.NotFound):
        return res(status.CLIENT_NOT_FOUND)
    else:
        logging.getLogger(__name__).error(traceback.format_exc())
        return _respond("An error occurred :(", status.SERVER_INTERNAL_ERROR)

def wrap_http_response(proc, success_create=False):
    """
    Executes the given procedure and translates success
    or errors into the appropriate response
    """
    try:
        if not callable(proc):
            """ TODO: allow trace to the caller """
            raise Exception("wrapped procedure is not callable")
        result = proc()
        success_code = status.SUCCESS_CREATE if success_create else status.SUCCESS_OK
        return _respond(result, success_code)
    except Exception as e:
        return _parse_exn(e)
