from django.contrib import admin
from django.urls import path, include

from .views import Info

urlpatterns = [
    path('', Info.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('games.api.external.urls')),
    path('info/', Info.as_view()),
]
