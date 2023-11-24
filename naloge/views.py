from django.shortcuts import render

from . import task
from . import forms

def index(request):
    # TODO: tle pride neka logika ki te vrze na selection skupine ce se nisi
    # zbral skupine, ce si pa ze zbral skupino ti da pa na voljo slike za
    # orientacijo. Slike bi blo fino da so nekak oznacene tiste na kirih si ze
    # bil, oz. da se sploh ne pokazejo
    return HttpResponse("Dobrodošli na Od srca do srca!")

task_list = [
    task.Task("nnz_epipen", "Epipen"),
    task.Task("nnz_opekline", "Opekline"),
    task.Task("nnz_ozivljanje", "Oživljanje"),
    task.Task("nnz_zadusitve", "Zadušitve"),
    task.Task("nnz_imobilizacija", "Zlomi"),
    task.Task("nnz_klic", "Klic na 112", forms.NNZKlic),
    task.Task("nnz_krvavitve", "Krvavitve"),
    task.Task("nnz_nezavest", "Nezavest"),
    task.Task("nnz_ozebline", "Ozebline"),
    task.Task("obv_splosno", "Pristop, pregled, klic na 112"),
    task.Task("obv_zapora", "Zapora dihalne poti"),
    task.Task("obv_mraz", "Poškodbe zaradi mraza"),
    task.Task("obv_imobilizacija", "Imobilizacija"),
    task.Task("obv_krvavitve", "Rane in krvavitve"),
    task.Task("obv_alergije", "Alergije"),
    task.Task("obv_zastrupitve", "Zastrupitve"),
    task.Task("obv_stanja", "Stanja"),
]
