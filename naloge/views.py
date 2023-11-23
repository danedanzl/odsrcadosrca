# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from . import task

def index(request):
    # TODO: tle pride neka logika ki te vrze na selection skupine ce se nisi
    # zbral skupine, ce si pa ze zbral skupino ti da pa na voljo slike za
    # orientacijo. Slike bi blo fino da so nekak oznacene tiste na kirih si ze
    # bil, oz. da se sploh ne pokazejo
    return HttpResponse("Dobrodošli na Od srca do srca!")

    return HttpResponse("Naloga Epipen za kategorijo Nič ne znam")
    return HttpResponse("Naloga Opekline za kategorijo Nič ne znam")
    return HttpResponse("Naloga Oživljanje za kategorijo Nič ne znam")
    return HttpResponse("Naloga Zadušitve za kategorijo Nič ne znam")
    return HttpResponse("Naloga Zlomi in zvini - imobilizacija za kategorijo Nič ne znam")
    return render(request, "naloge/nnz_klic.html", {'task_name': 'nnz_klic_task'})
    return HttpResponse("nnz_klic_task")
    return HttpResponse("Naloga Krvavitve za kategorijo Nič ne znam")
    return HttpResponse("Naloga Nezavest za kategorijo Nič ne znam")
    return HttpResponse("Naloga Ozebline za kategorijo Nič ne znam")
    return HttpResponse("Naloga Pristop, pregled, komunikacija, splošne stvari obveščanje in klic na 112 za kategorijo Obvladam")
    return HttpResponse("Naloga Zapora dihalne poti za kategorijo Obvladam")
    return HttpResponse("Naloga Poškodbe zaradi mraza za kategorijo Obvladam")
    return HttpResponse("Naloga Imobilizacija za kategorijo Obvladam")
    return HttpResponse("Naloga Rane in krvavitve za kategorijo Obvladam")
    return HttpResponse("Naloga Alergije za kategorijo Obvladam")
    return HttpResponse("Naloga Zastrupitve za kategorijo Obvladam")
    return HttpResponse("Naloga Stanja za kategorijo Obvladam")

task_list = [task.Task(t) for t in [
    "nnz_epipen",
    "nnz_opekline",
    "nnz_ozivljanje",
    "nnz_zadusitve",
    "nnz_imobilizacija",
    "nnz_klic",
    "nnz_krvavitve",
    "nnz_nezavest",
    "nnz_ozebline",
    "obv_splosno",
    "obv_zapora",
    "obv_mraz",
    "obv_imobilizacija",
    "obv_krvavitve",
    "obv_alergije",
    "obv_zastrupitve",
    "obv_stanja",
]]
