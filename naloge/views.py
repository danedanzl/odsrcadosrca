from django.shortcuts import render

from . import task
from . import forms
from common import kt

from naloge.models import MchoiceTask

def get_mchoicetask(category, name):
    return MchoiceTask.objects.get(category=category, name=name)
    return None

ktji = [
        kt.KT(3066, 4064,
              (task.Task("obv_alergije", "Alergije"),
               get_mchoicetask(category="nnz", name="epipen"))),
        kt.KT(3019, 4620,
              (task.Task("obv_splosno", "Pristop, pregled, klic na 112"),
               task.Task("nnz_klic", "Klic na 112", forms.NNZKlic))),
        kt.KT(8893, 3616,
              (task.Task("obv_zapora", "Zapora dihalne poti"),
               task.Task("nnz_zadusitve", "Zadušitve"))),
        kt.KT(6415, 6859,
              (task.Task("obv_mraz", "Poškodbe zaradi mraza"),
               task.Task("nnz_ozebline", "Ozebline"))),
        kt.KT(8759, 9918,
              (task.Task("obv_imobilizacija", "Imobilizacija"),
               get_mchoicetask(category="nnz", name="imobilizacija"))),
        kt.KT(8404, 4747,
              (get_mchoicetask(category="obv", name="krvavitve"),
               task.Task("nnz_krvavitve", "Krvavitve"))),
        kt.KT(5647, 9156,
              (task.Task("obv_opekline", "Opekline"),
               task.Task("nnz_opekline", "Opekline", forms.NNZOpekline))),
        kt.KT(9384, 3296,
              (task.Task("obv_polozaji", "Položaji"),
               task.Task("nnz_nezavest", "Nezavest"))),
        kt.KT(1430, 7966,
              (get_mchoicetask(category="obv", name="tpo"),
               task.Task("nnz_ozivljanje", "Oživljanje"))),
        kt.KT(2777, 2654,
              (get_mchoicetask(category="obv", name="zastrupitve"),
               None)),
        kt.KT(2047, 5706,
              (get_mchoicetask(category="obv", name="stanja"),
               None)),
]

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

task_map = {kt.urlid : kt for kt in ktji}
