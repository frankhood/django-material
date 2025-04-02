from django.conf.urls import include
from . import modules
from django.urls import path


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(modules.urls)),
]
