from django.urls import path
from . import views

app_name = "superadmin"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
]