## Server
Rabis django 4.

## QR kode
Za generiranje QR kod rabis python package `segno` in
imagemagick command line orodja. Generiras z `./manage.py qr`. Output bo v mapi
`qr`. Generiranje traja neki cajta (pol minute pr men).

## Setup & Install
`./manage.py init`

## Implementiranje nalog
Nova naloga je sestavljena iz treh html komponent in enega forma na backendu.
Form v backendu pride v `naloge/forms.py`, uporabis ga tko da ga podas kot
tretji argument v `task_list` seznamu v `naloge/task.py`. Form zgleda tko da
nastejes polja ki bodo uporabljena. Implementirat mora tud metodo correct(), ki
preverja kolk prav je bla oddana resitev.

Poglej kako je `nnz_klic` narjena za reference. Ta primer vrne iz correct() nek
bool, ampak lahko bi vrnl tud karkoli drugega (recimo tocke med 1 in 10)
provided da je to pol uredu pohendlano v templatu.

Html komponente so: izobrazevalni tekst, stran z nalogo in stran z resitvijo.
Izobrazevalne tekste v html rihta Klemen, ostalo dvoje mormo pa mi. Stran z
resitvijo bi blo fino ce bi vsebovala kksn kratk povzetek zakaj je kej prov al
pa ne, ampak tega nimamo zares prpravlenga vsebinsko tko da je treba neki si
zmislt.

## Grafično/vizualni TODOji
Treba je vsem razen glavne strani popravit da bo logo\_small.png na vrhu
Treba je poskrbet da bodo stvari mele taprav title.
Treba je narest verzije slikic ki so oznacene kot ze obiskane.
