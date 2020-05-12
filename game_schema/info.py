from django.http import HttpResponse
from django.views import View
from django.conf import settings

import datetime as dt
import json


INFO = "NOT LOADED"

with open("info.json") as f:
    INFO = json.loads(f.read())

INFO['deployment_mode'] = "dev" if settings.DEBUG else "prod"
INFO['deployment_time'] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
INFO['timezone'] = settings.TIME_ZONE

class Info(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(INFO), content_type="application/json")
