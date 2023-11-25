from django.urls import path, reverse

from . import views

app_name = 'naloge'

urlpatterns = []

for kt in views.task_map.values():
    if kt.obv is not None:
        urlpatterns += kt.obv.urlpatterns()
    if kt.nnz is not None:
        urlpatterns += kt.nnz.urlpatterns()
