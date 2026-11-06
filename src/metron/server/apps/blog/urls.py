from django.urls import path

from metron.server.apps.blog import views

urlpatterns = [
    path("", views.home, name="home"),
]
