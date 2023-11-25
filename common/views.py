from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404

from naloge.views import task_map
from naloge.task import Task

def index(request):
    # TODO: display login info for logged in users somewhere
    return render(request, "common/homepage.html")

def ktlist(request):
    is_obv = True # TODO
    ktji = []
    obv = []
    for _,kt in sorted(list(task_map.items())):
        o = ktji
        if kt.nnz is None:
            o = obv
        o.append({
            'url' : reverse("img", kwargs={ 'imgid': kt.imgid }),
            'imgurl': f"img/nav/{kt.imgid}.jpg",
            'done': False, # TODO
        })
    if not is_obv:
        obv[0] = None
    last = ktji[-1]
    ktji = list(zip(ktji[::2], ktji[1::2]))
    return render(request, "common/pick_kt.html", { 'kts' : ktji, 'last': last,
                                                   'obv0' : obv[0], 'obv1': obv[1]})

def kt(request, kt):
    if kt := task_map.get(kt):
        # TODO: pick difficulty based in request.user
        return redirect(kt.obv.info_viewname)
    else:
        raise Http404

def img(request, imgid):
    for kt in task_map.values():
        if kt.imgid == imgid:
            url = f"img/nav/{kt.imgid}.jpg"
            return render(request, "common/kt_details.html", { 'kt': kt, 'imgurl': url })
    else:
        raise Http404
