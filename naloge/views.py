# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Dobrodošli na Od srca do srca!")

def nnz_epipen(request):
	return HttpResponse("Naloga Epipen za kategorijo Nič ne znam")

def nnz_opekline(request):
	return HttpResponse("Naloga Opekline za kategorijo Nič ne znam")

def nnz_ozivljanje(request):
	return HttpResponse("Naloga Oživljanje za kategorijo Nič ne znam")

def nnz_zadusitve(request):
	return HttpResponse("Naloga Zadušitve za kategorijo Nič ne znam")

def nnz_imobilizacija(request):
	return HttpResponse("Naloga Zlomi in zvini - imobilizacija za kategorijo Nič ne znam")

def nnz_klic(request):
	return HttpResponse("Naloga Klic na 112 za kategorijo Nič ne znam")

def nnz_krvavitve(request):
	return HttpResponse("Naloga Krvavitve za kategorijo Nič ne znam")

def nnz_nezavest(request):
	return HttpResponse("Naloga Nezavest za kategorijo Nič ne znam")

def nnz_ozebline(request):
	return HttpResponse("Naloga Ozebline za kategorijo Nič ne znam")

def obv_splosno(request):
	return HttpResponse("Naloga Pristop, pregled, komunikacija, splošne stvari obveščanje in klic na 112 za kategorijo Obvladam")

def obv_zapora(request):
	return HttpResponse("Naloga Zapora dihalne poti za kategorijo Obvladam")

def obv_mraz(request):
	return HttpResponse("Naloga Poškodbe zaradi mraza za kategorijo Obvladam")

def obv_imobilizacija(request):
	return HttpResponse("Naloga Imobilizacija za kategorijo Obvladam")

def obv_krvavitve(request):
	return HttpResponse("Naloga Rane in krvavitve za kategorijo Obvladam")

def obv_alergije(request):
	return HttpResponse("Naloga Alergije za kategorijo Obvladam")

def obv_zastrupitve(request):
	return HttpResponse("Naloga Zastrupitve za kategorijo Obvladam")

def obv_stanja(request):
	return HttpResponse("Naloga Stanja za kategorijo Obvladam")

task_list = [
	nnz_epipen,
	nnz_opekline,
	nnz_ozivljanje,
	nnz_zadusitve,
	nnz_imobilizacija,
	nnz_klic,
	nnz_krvavitve,
	nnz_nezavest,
	nnz_ozebline,
	obv_splosno,
	obv_zapora,
	obv_mraz,
	obv_imobilizacija,
	obv_krvavitve,
	obv_alergije,
	obv_zastrupitve,
	obv_stanja,
]
