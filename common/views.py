from enum import Enum
import functools

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, HttpResponseBadRequest

from naloge.views import task_map
from naloge.task import Task

class Group(Enum):
    OBV = 0
    NNZ = 1

def validate_cookies(fn):
    @functools.wraps(fn)
    def wrapper(request, *args, **kwargs):
        request.session = {}

        # group
        if (group := request.COOKIES.get("group")) == "nnz":
            group = Group.NNZ
        elif group == "obv":
            group = Group.OBV
        elif group is not None:
            return HttpResponseBadRequest()

        if (done := request.COOKIES.get("done")) is not None:
            if len(done) != 11 or done.count('0') + done.count('1') != 11:
                return HttpResponseBadRequest()
            done = [c == '1' for c in done]
        elif group is not None:
            return HttpResponseBadRequest()
        response = fn(request, group, done, *args, **kwargs)
        if done is not None:
            response.set_cookie("done", "".join(("1" if d else "0" for d in done)))
        return response
    return wrapper

@validate_cookies
def index(request, group, done):
    # TODO: display login info for logged in users somewhere
    return render(request, "common/homepage.html", { 'is_started' : group is not None})

def group_selection(request):
    return render(request, "common/group_selection.html")

def pick_nnz(request):
    response = redirect("ktlist")
    response.set_cookie("group", "nnz")
    response.set_cookie("done", "0"*11) # TODO move this to registration
    return response

def pick_obv(request):
    response = redirect("ktlist")
    response.set_cookie("group", "obv")
    response.set_cookie("done", "0"*11) # TODO move this to registration
    return response

@validate_cookies
def ktlist(request, group, done):
    if group is None:
        return redirect("group_selection")
    ktji = []
    for i,kt in enumerate(sorted(list(task_map.values()))):
        if group == Group.NNZ and kt.nnz is None:
            continue
        ktji.append({
            'url' : reverse("img", kwargs={ 'imgid': kt.imgid }),
            'imgurl': f"img/nav/{kt.imgid}.jpg",
            'done': done[i], # TODO
        })
    last = ktji[-1]
    ktji = list(zip(ktji[::2], ktji[1::2]))
    return render(request, "common/pick_kt.html", { 'kts' : ktji, 'last': last })

@validate_cookies
def kt(request, group, done, kt):
    curr = kt
    for i,kt in enumerate(sorted(list(task_map.values()))):
        if kt.urlid == curr:
            done[i] = True
            if group == Group.OBV:
                return redirect(kt.obv.info_viewname)
            elif kt.nnz is None:
                raise NotImplementedError("Ta naloga ni na voljo za to skupino")
            return redirect(kt.nnz.info_viewname)
    else:
        raise Http404

@validate_cookies
def img(request, group, done, imgid):
    for i,kt in enumerate(list(sorted(task_map.values()))):
        if kt.imgid == imgid:
            url = f"img/nav/{kt.imgid}.jpg"
            return render(request, "common/kt_details.html", { 'kt': kt, 'imgurl': url, 'done': done[i] })
    else:
        raise Http404
