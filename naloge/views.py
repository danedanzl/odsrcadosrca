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
    task.Task("obv_tpo", "Temeljni postopki oživljanja"),
    task.Task("obv_zapora", "Zapora dihalne poti"),
    task.Task("obv_polozaji", "Položaji"),
    task.Task("obv_krvavitve", "Rane in krvavitve"),
    task.Task("obv_opekline", "Opekline"),
    task.Task("obv_mraz", "Poškodbe zaradi mraza"),
    task.Task("obv_alergije", "Alergije"),
    task.Task("obv_imobilizacija", "Imobilizacija"),
    task.Task("obv_zastrupitve", "Zastrupitve"),
    task.Task("obv_stanja", "Stanja"),
]

task_map = {
        3066 : ('obv_alergije', 'nnz_epipen'),
        3019 : ('obv_splosno', 'nnz_klic'),
        8893 : ('obv_zapora', 'nnz_zadusitve'),
        6415 : ('obv_mraz', 'nnz_ozebline'),
        8759 : ('obv_imobilizacija', 'nnz_imobilizacija'),
        8404 : ('obv_krvavitve', 'nnz_krvavitve'),
        5647 : ('obv_opekline', 'nnz_opekline'),
        9384 : ('obv_polozaji', 'nnz_nezavest'),
        1430 : ('obv_tpo', 'nnz_ozivljanje'),
        2777 : ('obv_zastrupitve', None),
        2047 : ('obv_stanja', None),
}
