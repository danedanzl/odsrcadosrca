from functools import reduce

from django.urls import path, reverse

from . import views
from .tasklist import task_list

def hsh(s):
    return str(sum(ord(c)*17**i for i,c in enumerate(s)))[-3:]

urlpatterns = [
	path("", views.index, name="index"),
   ] + [path(f"{str(hsh(f.__name__))}_{f.__name__}", f, name=f.__name__) for f in task_list]
