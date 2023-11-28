from django.urls import path, reverse

from . import views

urlpatterns = []

for kt in views.ktji:
    if kt.obv is not None:
        urlpatterns += kt.obv.urlpatterns()
    if kt.nnz is not None:
        urlpatterns += kt.nnz.urlpatterns()
