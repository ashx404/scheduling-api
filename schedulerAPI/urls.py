from django.urls import path
from .views import ping
from .views import schedulingAPI

urlpatterns = [
    path("ping", ping, name="ping"),
    path("schedule", schedulingAPI, name="schedulingAPI")
]
