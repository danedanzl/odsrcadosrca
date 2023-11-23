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

task_list = [task.Task(*t) for t in [
    ("nnz_epipen", "Epipen"),
    ("nnz_opekline", "Opekline"),
    ("nnz_ozivljanje", "Oživljanje"),
    ("nnz_zadusitve", "Zadušitve"),
    ("nnz_imobilizacija", "Zlomi"),
    ("nnz_klic", "Klic na 112"),
    ("nnz_krvavitve", "Krvavitve"),
    ("nnz_nezavest", "Nezavest"),
    ("nnz_ozebline", "Ozebline"),
    ("obv_splosno", "Pristop, pregled, klic na 112"),
    ("obv_zapora", "Zapora dihalne poti"),
    ("obv_mraz", "Poškodbe zaradi mraza"),
    ("obv_imobilizacija", "Imobilizacija"),
    ("obv_krvavitve", "Rane in krvavitve"),
    ("obv_alergije", "Alergije"),
    ("obv_zastrupitve", "Zastrupitve"),
    ("obv_stanja", "Stanja"),
]]
