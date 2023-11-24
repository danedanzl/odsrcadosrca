from django.shortcuts import render, redirect
from django.http import Http404

from naloge.views import task_map
from naloge.task import Task

def index(request):
    # TODO: display login info for logged in users somewhere
    return render(request, "common/homepage.html")

def kt(request, kt):
    if name := task_map.get(kt):
        # TODO: pick difficulty based in request.user
        return redirect(Task(name[1], "").info_viewname)
    else:
        raise Http404
