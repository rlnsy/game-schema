from django.db.models import (
    IntegerField
)

from games.models import Action

from games.api.internal.exceptions import NotAllowed as ObjectExists
