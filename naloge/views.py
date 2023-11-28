from django.shortcuts import render

from . import task
from . import forms
from common import kt

from naloge.models import MchoiceTask

def get_mchoicetask(category, name):
    return MchoiceTask.objects.get(category=category, name=name)
    return None

ktji = [
        kt.KT(2777, 2654, #3066, 4064,
              (task.Task("obv_alergije", "Alergije", forms.OBVAlergije),
               get_mchoicetask(category="nnz", name="epipen")),
              "Pri edinem sidru v Ljubljani",
              "Kongresni trg - po sredinskih stopnicah v garažno hišo pod Kongresnim trgom (poleg glavne blagajne)"),
        kt.KT(3019, 4620,
              (get_mchoicetask(category="obv", name="splosno"),
               task.Task("nnz_klic", "Klic na 112", forms.NNZKlic)),
             "Zraven je zelo znan Ljubljanski hotel - poimenovan po mogočni živali",
             "Vošnjakova ulica 2"),
        kt.KT(2047, 5706, #8893, 3616,
              (task.Task("obv_zapora", "Zapora dihalne poti", forms.TrivialForm),
               task.Task("nnz_zadusitve", "Zadušitve", forms.NNZZadusitve)),
             "Na nasprotni strani parka se nahaja vrhovno sodišče Republike Slovenije",
             "Dalmatinova ulica 4"),
        kt.KT(8893, 3616, #6415, 6859,
              (task.Task("obv_mraz", "Poškodbe zaradi mraza", forms.OBVMraz),
               task.Task("nnz_ozebline", "Ozebline", forms.TrivialForm)),
             "Nasproti hotela, ki nosi enako ime kot ljubljanska pivovarna",
             "Miklošičeva cesta 5"),
        kt.KT(5647, 9156, #8759, 9918,
              (task.Task("obv_imobilizacija", "Imobilizacija", forms.OBVImobilizacija),
               get_mchoicetask(category="nnz", name="imobilizacija")),
             "V bližini se nahaja radiotelevizija Slovenija (RTV)",
             "Komenskega ulica 4"),
        kt.KT(6415, 6859, #8404, 4747,
              (get_mchoicetask(category="obv", name="krvavitve"),
               task.Task("nnz_krvavitve", "Krvavitve", forms.NNZKrvavitve)),
             "AED se nahaja okoli stavbe, ki ima razgled na staro mestno elektrarno z visokim dimnikom.",
             "Kotnikova ulica 5"),
        kt.KT(8759, 9918, #5647, 9156,
              (task.Task("obv_opekline", "Opekline", forms.OBVOpekline),
               task.Task("nnz_opekline", "Opekline", forms.NNZOpekline)),
             "Na križišču, kjer stoji Sokolski dom",
             "Rozmanova ulica 12"),
        kt.KT(3066, 4064, #9384, 7966,
              (task.Task("obv_polozaji", "Položaji", forms.OBVPolozaji),
               task.Task("nnz_nezavest", "Nezavest", forms.NNZNezavest)),
              "Podhod pri slovenskem hramu kulture",
              "Spodnja etaža MAXI (delovni čas: pon. - ned. med 5.00 ter 23.00)"),
        kt.KT(1430, 3296,
              (get_mchoicetask(category="obv", name="tpo"),
               task.Task("nnz_ozivljanje", "Oživljanje", forms.TrivialForm)),
            "Na obrobju Emone",
            "Mirje 19"),
        kt.KT(8404, 4747,#2777, 2654,
              (get_mchoicetask(category="obv", name="zastrupitve"),
               None),
             "Na lokaciji se nahaja tudi plesni teater Ljubljana",
             "Prijateljeva 2"),
        kt.KT(9384, 7966,# 2047, 5706,
              (get_mchoicetask(category="obv", name="stanja"),
               None),
              "Pri starejših občanih v Trnovem",
              "Devinska ulica 1b")
]

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

task_map = {kt.urlid : kt for kt in ktji}
