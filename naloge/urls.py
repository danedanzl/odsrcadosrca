from django.urls import path, reverse

from . import views

urlpatterns = [
	path("", views.index, name="naloge_index"),
]

for t in views.task_list:
    urlpatterns += t.urlpatterns()
