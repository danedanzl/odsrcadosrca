from django.urls import path, reverse

from . import views

urlpatterns = [
	path("", views.index, name="naloge_index"),
]

for kt in views.task_map.values():
    urlpatterns += kt.obv.urlpatterns()
    if kt.nnz is not None:
        urlpatterns += kt.nnz.urlpatterns()
