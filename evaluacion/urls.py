from django.urls import path

from . import views


app_name = "evaluacion"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("juego/<int:id>/", views.detalle, name="detalle"),
]