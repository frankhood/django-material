from django.views import generic
from django.urls import path


urlpatterns = [
    path('', generic.TemplateView.as_view(template_name="accounting/index.html"), name="index"),
]
