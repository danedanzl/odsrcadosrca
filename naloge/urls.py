from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),

	path("nnz_epipen", views.nnz_epipen, name="nnz_epipen"),
	path("nnz_opekline", views.nnz_opekline, name="nnz_opekline"),
	path("nnz_ozivljanje", views.nnz_ozivljanje, name="nnz_ozivljanje"),
	path("nnz_zadusitve", views.nnz_zadusitve, name="nnz_zadusitve"),
	path("nnz_imobilizacija", views.nnz_imobilizacija, name="nnz_imobilizacija"),
	path("nnz_klic", views.nnz_klic, name="nnz_klic"),
	path("nnz_krvavitve", views.nnz_krvavitve, name="nnz_krvavitve"),
	path("nnz_nezavest", views.nnz_nezavest, name="nnz_nezavest"),
	path("nnz_ozebline", views.nnz_ozebline, name="nnz_ozebline"),

	path("obv_splosno", views.obv_splosno, name="obv_splosno"),
	path("obv_zapora", views.obv_zapora, name="obv_zapora"),
	path("obv_mraz", views.obv_mraz, name="obv_mraz"),
	path("obv_imobilizacija", views.obv_imobilizacija, name="obv_imobilizacija"),
	path("obv_krvavitve", views.obv_krvavitve, name="obv_krvavitve"),
	path("obv_alergije", views.obv_alergije, name="obv_alergije"),
	path("obv_zastrupitve", views.obv_zastrupitve, name="obv_zastrupitve"),
	path("obv_stanja", views.obv_stanja, name="obv_stanja"),

]
