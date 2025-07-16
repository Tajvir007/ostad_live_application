from django.urls import path
from . import views

app_name = "others"

urlpatterns = [
    path('manage-club/', views.manage_club, name="manage_club"),
]
