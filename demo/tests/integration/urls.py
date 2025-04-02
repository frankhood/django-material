from django.conf.urls import include
from django.views import generic

from . import views
from django.urls import path

urlpatterns = [
    path('', generic.RedirectView.as_view(url='./city/'), name="index"),
    path('city/', include(views.CityViewSet().urls)),
    path('continent/', include(views.ContinentViewSet().urls)),
    path('country/', include(views.CountryViewSet().urls)),
    path('ocean/', include(views.OceanViewSet().urls)),
    path('sea/', include(views.SeaViewSet().urls)),
]
