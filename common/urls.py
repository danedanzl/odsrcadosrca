from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path("<int:kt>", views.kt, name="kt"),
    path("i/<int:imgid>", views.img, name="img"),
    path("list", views.ktlist, name="ktlist"),
]
