from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path("<int:kt>", views.kt, name="kt"),
    path("i/<int:imgid>", views.img, name="img"),
    path("cheat/<int:imgid>", views.cheat, name="img"),
    path("list", views.ktlist, name="ktlist"),
    path("group", views.group_selection, name="group_selection"),
    path("nnz", views.pick_nnz, name="nnz"),
    path("obv", views.pick_obv, name="obv"),
    path("reset", views.cookie_reset, name="reset"),
    path("start", views.register, name="register"),
]
