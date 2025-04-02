from django.conf.urls import include
from django.views import generic

from . import views
from django.urls import path


urlpatterns = [
    path('', generic.RedirectView.as_view(
        url='./departments/'), name="index"),
    path('departments/', include(views.DepartmentViewSet().urls)),
    path('employees/', include(views.EmployeeViewSet().urls)),
]
