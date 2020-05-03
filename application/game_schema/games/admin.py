from django.contrib import admin
from .models.games_core import Game
from .models.games_players import Player
from .models.games_session import Session

# Register your models here.
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Session)
