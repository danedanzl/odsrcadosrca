from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from naloge.models import MchoiceTask, MchoiceQuestion, MchoiceAnswer

MA = MchoiceAnswer.objects.create
MQ = MchoiceQuestion.objects.create
MT = MchoiceTask.objects.create

def mk_nnz_imobilizacija():
    if MchoiceTask.objects.filter(display_name="Zvini in zlomi - imobilizacija",
                                  name="imobilizacija", max_points=0,
                                  category="nnz").count() == 0:
        print(f"creating nnz: Zvini in zlomi - imobilizacija")
        with transaction.atomic():

            nal = MT(display_name="Zvini in zlomi - imobilizacija",
                     name="imobilizacija", max_points=0, category="nnz")


            vpr1 = MQ(nal=nal, vpr="Očka Peter je med obiranjem drevesa poleti "
                                   "padel iz visoke lestve. Kaj moraš najprej "
                                   "narediti?")
            vpr2 = MQ(nal=nal, vpr="Ko je poskusil dvigniti pretežke uteži, se je "
                                   "Lukatu kar naenkrat vdala desna roka in zdaj ne "
                                   "more več premikati roke v komolcu. Na srečo so "
                                   "uteži padle mimo njega in ga niso dodatno "
                                   "poškodovale. Kaj narediš?")
            vpr3 = MQ(nal=nal, vpr="Na pohodu se Izak cel dan pritožuje, da se mu "
                                   "ne da več hoditi in da ga boli gleženj. Ko "
                                   "zvečer da nogo iz gojzarja, vidi, da je njegov "
                                   "gleženj otekel in ga strašansko boli že samo ob "
                                   "dotiku. Kaj se mu je najverjetneje zgodilo in "
                                   "kaj naj naredi?")


            MA(vpr=vpr1, ans="Hitro ga premakni v senco, da ne bo dehidriran.", prav=False)
            MA(vpr=vpr1, ans="Spravi ga v sedeč položaj, da se umiri od šoka pri padcu.", prav=False)
            MA(vpr=vpr1, ans="Roko mu daj v ruto pestovalko, saj ga boli.", prav=False)
            MA(vpr=vpr1, ans="Ne premikaj ga, saj ima mogoče poškodovano hrbtenico.", prav=True)

            MA(vpr=vpr2, ans="Rečeš mu, naj se spravi iz fitnesa, saj nima tu nič več iskati, če je poškodovan.", prav=False)
            MA(vpr=vpr2, ans="Komolec hladiš, ter nanj nalepiš obliž, da se bo hitreje zacelil.", prav=False)
            MA(vpr=vpr2, ans="Roko mu daš v ruto pestovalko, čeprav ga po njegovih besedah “boli ko svinja”.", prav=False)
            MA(vpr=vpr2, ans="Komolec hladiš in ga poviješ tako, da ga ne more premikati.", prav=True)

            MA(vpr=vpr3, ans="Gleženj si je zvil. Mora si ga naravnati nazaj in oteklina bo splahnela.", prav=False)
            MA(vpr=vpr3, ans="V gleženj ga je pičila/ugriznila neka žival. Gleženj naj hladi in izjoka vso bolečino.", prav=False)
            MA(vpr=vpr3, ans="Gleženj si je zvil. Čimbolj naj ga razgibava, kljub bolečini, saj se bo tako najhitreje spravil v normalno stanje.", prav=False)
            MA(vpr=vpr3, ans="Gleženj si je zvil. Nanj naj si da obkladek in ga povije tako, da se ne bo premikal. Izogiba naj se hoji.", prav=True)

def mk_obv_krvavitve():
    if MchoiceTask.objects.filter(display_name="Rane in krvavitve",
                                  name="krvavitve", max_points=0,
                                  category="obv").count() == 0:
        print(f"creating obv: Rane in krvavitve")
        with transaction.atomic():
            obvl_krvavitve = MT(display_name="Rane in krvavitve", name="krvavitve",
                                max_points=0, category="obv")

            vpr = MQ(nal=obvl_krvavitve, vpr="Kaj je notranja krvavitev?")
            MA(vpr=vpr, ans="Kri znotraj žil.", prav=False)
            MA(vpr=vpr, ans="Krvavitev znotraj telesa, ki je lahko smrtno nevarna.", prav=True)
            MA(vpr=vpr, ans="Krvavitev, ko je poškodovanec v notranjem prostoru.", prav=False)

            vpr = MQ(nal=obvl_krvavitve, vpr="Kaj je tujek?")
            MA(vpr=vpr, ans="Priseljenec.", prav=False)
            MA(vpr=vpr, ans="Zdravilo za pike eksotičnih mušic.", prav=False)
            MA(vpr=vpr, ans="Tuj predmet v telesu.", prav=True)
            MA(vpr=vpr, ans="Tuj predmet v bližini telesa.", prav=False)

            vpr = MQ(nal=obvl_krvavitve, vpr="Kaj je šok?")
            MA(vpr=vpr, ans="Bolezensko stanje, ko srce ne zmore dovajati dovolj krvi vsem organom.", prav=True)
            MA(vpr=vpr, ans="Reakcija, ko sosed prevara sosedo.", prav=False)
            MA(vpr=vpr, ans="Reakcija na pik čebele.", prav=False)
            MA(vpr=vpr, ans="Naslov pesmi Damjana Murka.", prav=False)

            vpr = MQ(nal=obvl_krvavitve, vpr="Kaj je imobilizacija?")
            MA(vpr=vpr, ans="Pritrditev uda, tujka ali drugega dela telesa, da mu je onemogočeno premikanje.", prav=True)
            MA(vpr=vpr, ans="Povitje noge ali roke.", prav=False)
            MA(vpr=vpr, ans="Odvzem prevoznega sredstva.", prav=False)
            MA(vpr=vpr, ans="Zlom, ki se ne premika več.", prav=False)

            vpr = MQ(nal=obvl_krvavitve, vpr="Kaj je sterilno?")
            MA(vpr=vpr, ans="Čisto, brez prisotnosti bakterij, umazanije.", prav=True)
            MA(vpr=vpr, ans="Lepo urejeno, pospravljeno.", prav=False)
            MA(vpr=vpr, ans="Direktno, brez ovinkov.", prav=False)
            MA(vpr=vpr, ans="Jasno razloženo, enostavno predstavljeno.", prav=False)

            vpr = MQ(nal=obvl_krvavitve, vpr="Kaj je kompresijska obveza?")
            MA(vpr=vpr, ans="Obveza naredjena pod časovnim pritiskom.", prav=False)
            MA(vpr=vpr, ans="Obveza za večje rane, na katero pritisnemo dodaten trd predmet, da ustavimo krvavitev.", prav=True)
            MA(vpr=vpr, ans="Posebni obliži, ki nadomestijo šive pri manjših ranah in jih nato povijemo.", prav=False)
            MA(vpr=vpr, ans="Obveza narejena v kompresijski komori.", prav=False)

            vpr = MQ(nal=obvl_krvavitve, vpr="Kaj je arterija?")
            MA(vpr=vpr, ans="Žila, po kateri teče kri, napolnjena s kisikom.", prav=True)
            MA(vpr=vpr, ans="Žila, ki teče proti srcu.", prav=False)
            MA(vpr=vpr, ans="Avto znamke Opel.", prav=False)
            MA(vpr=vpr, ans="Bolezen, pri kateri doživljamo nihanje med nizkim in visokim krvnim tlakom.", prav=False)

            vpr = MQ(nal=obvl_krvavitve, vpr="Kaj je vena?")
            MA(vpr=vpr, ans="Površinska žila tik pod kožo.", prav=False)
            MA(vpr=vpr, ans="Grška boginja zdravja.", prav=False)
            MA(vpr=vpr, ans="Zgornja srčna mišica.", prav=False)
            MA(vpr=vpr, ans="Žila, ki teče prosti srcu.", prav=True)

def mk_obv_zastrupitve():
    if MchoiceTask.objects.filter(display_name="Zastrupitve",
                                  name="zastrupitve", max_points=0,
                                  category="obv").count() == 0:
        print(f"creating obv: Zastrupitve")
        with transaction.atomic():
            nal = MT(display_name="Zastrupitve", name="zastrupitve", max_points=0,
                     category="obv")
            vpr = MQ(nal=nal, vpr="Bruhanje lahko pri sumu zastrupitve izzovemo:")
            MA(vpr=vpr, ans="Kadarkoli.", prav=False)
            MA(vpr=vpr, ans="Čim prej po zaužitju strupene snovi.", prav=False)
            MA(vpr=vpr, ans="Le po posvetu z zdravnikom.", prav=True)

            vpr = MQ(nal=nal, vpr="Najpogostejše vrste zastrupitev so povezane:")
            MA(vpr=vpr, ans="Z jemanjem prepovedanih substanc.", prav=True)
            MA(vpr=vpr, ans="Z nekaterimi slabo označenimi gospodinjskimi pripomočki.", prav=False)
            MA(vpr=vpr, ans="Z visoko količino ogljikovega monoksida v zaprtih prostorih.", prav=False)

            vpr = MQ(nal=nal, vpr="Kaj moramo narediti, če sumimo, da je nekdo zastrupljen?")
            MA(vpr=vpr, ans="Takoj kličemo 112.", prav=True)
            MA(vpr=vpr, ans="Klic na 112 pokličemo le, če smo prepričani, da je zastrupitev lahko smrtna.", prav=False)
            MA(vpr=vpr, ans="Kličemo, ko se pokažejo prvi simptomi zastrupitve.", prav=False)

            vpr = MQ(nal=nal, vpr="Kateri od navedenih ukrepov ob zastrupitvi ni pravilen?")
            MA(vpr=vpr, ans="Spravimo na varno.", prav=False)
            MA(vpr=vpr, ans="Primeru izgube zavesti ga položimo v položaj za nezavestnega.", prav=False)
            MA(vpr=vpr, ans="Primeru, da je zastrupljeni pri zavesti, lahko po manjših požirkih pije navadno vodo, da razredči strup.", prav=True)

            vpr = MQ(nal=nal, vpr="Kateri od naštetih simptomov ni pogost simptom zastrupitve preko očesa?")
            MA(vpr=vpr, ans="Rdeče in razdražene oči.", prav=False)
            MA(vpr=vpr, ans="Otekanje območja okoli oči.", prav=True)
            MA(vpr=vpr, ans="Poškodbe oči in bolečina.", prav=False)

def mk_obv_stanja():
    if MchoiceTask.objects.filter(display_name="Stanja",
                                  name="stanja", max_points=0,
                                  category="obv").count() == 0:
        print(f"creating obv: Stanja")
        with transaction.atomic():
            nal = MT(display_name="Stanja", name="stanja", max_points=0,
                     category="obv")

            vpr = MQ(nal=nal, vpr="Kako pogosto lahko pri srčni kapi pod jezik poškropimo nitrolingual?")
            MA(vpr=vpr, ans="Na 5 minut.", prav=True)
            MA(vpr=vpr, ans="Na 10 minut.", prav=False)
            MA(vpr=vpr, ans="Samo 1-krat.", prav=False)

            vpr = MQ(nal=nal, vpr="Katero zdravilo lahko damo posamezniku, kadar sumimo možgansko kap?")
            MA(vpr=vpr, ans="Aspirin.", prav=False)
            MA(vpr=vpr, ans="Lekadol.", prav=False)
            MA(vpr=vpr, ans="Nobenega.", prav=True)

            vpr = MQ(nal=nal, vpr="Po koliko časa kličemo strokovno pomoč pri epileptičnem napadu?")
            MA(vpr=vpr, ans="Takoj.", prav=False)
            MA(vpr=vpr, ans="Po 2-3 minutah.", prav=True)
            MA(vpr=vpr, ans="Po 5 ali več minutah.", prav=False)

            vpr = MQ(nal=nal, vpr="Kaj lahko damo osebi v hipoglikemičnem stanju, ki je pri zavesti?")
            MA(vpr=vpr, ans="Hrano, ki vsebuje veliko ogljikovih hidratov.", prav=True)
            MA(vpr=vpr, ans="Hrano, ki vsebuje veliko proteinov.", prav=False)
            MA(vpr=vpr, ans="Hrano, ki vsebuje veliko vlaknin.", prav=False)

            vpr = MQ(nal=nal, vpr="Pri astmatičnem napadu naj bolnik zdravilo v pljučih:")
            MA(vpr=vpr, ans="Izdihnihne takoj.", prav=False)
            MA(vpr=vpr, ans="Počasi izdihne skozi nos.", prav=False)
            MA(vpr=vpr, ans="Zadrži nekaj časa.", prav=True)

def mk_obv_stanja():
    if MchoiceTask.objects.filter(display_name="Stanja",
                                  name="stanja", max_points=0,
                                  category="obv").count() == 0:
        print(f"creating obv: Stanja")
        with transaction.atomic():
            nal = MT(display_name="Stanja", name="stanja", max_points=0,
                     category="obv")

            vpr = MQ(nal=nal, vpr="Kako pogosto lahko pri srčni kapi pod jezik poškropimo nitrolingual?")
            MA(vpr=vpr, ans="Na 5 minut.", prav=True)
            MA(vpr=vpr, ans="Na 10 minut.", prav=False)
            MA(vpr=vpr, ans="Samo 1-krat.", prav=False)

            vpr = MQ(nal=nal, vpr="Katero zdravilo lahko damo posamezniku, kadar sumimo možgansko kap?")
            MA(vpr=vpr, ans="Aspirin.", prav=False)
            MA(vpr=vpr, ans="Lekadol.", prav=False)
            MA(vpr=vpr, ans="Nobenega.", prav=True)

            vpr = MQ(nal=nal, vpr="Po koliko časa kličemo strokovno pomoč pri epileptičnem napadu?")
            MA(vpr=vpr, ans="Takoj.", prav=False)
            MA(vpr=vpr, ans="Po 2-3 minutah.", prav=True)
            MA(vpr=vpr, ans="Po 5 ali več minutah.", prav=False)

            vpr = MQ(nal=nal, vpr="Kaj lahko damo osebi v hipoglikemičnem stanju, ki je pri zavesti?")
            MA(vpr=vpr, ans="Hrano, ki vsebuje veliko ogljikovih hidratov.", prav=True)
            MA(vpr=vpr, ans="Hrano, ki vsebuje veliko proteinov.", prav=False)
            MA(vpr=vpr, ans="Hrano, ki vsebuje veliko vlaknin.", prav=False)

            vpr = MQ(nal=nal, vpr="Pri astmatičnem napadu naj bolnik zdravilo v pljučih:")
            MA(vpr=vpr, ans="Izdihnihne takoj.", prav=False)
            MA(vpr=vpr, ans="Počasi izdihne skozi nos.", prav=False)
            MA(vpr=vpr, ans="Zadrži nekaj časa.", prav=True)

def mk_nnz_epipen():
    if MchoiceTask.objects.filter(display_name="Epipen", name="epipen",
                                  max_points=0, category="nnz").count() == 0:
        print(f"creating nnz: Epipen")
        with transaction.atomic():
            nal = MT(display_name="Epipen", name="epipen", max_points=0,
                     category="nnz")

            vpr = MQ(nal=nal, vpr="Epipen moramo uporabiti tudi pri lažjih alergijskih reakcijah, kot so na primer izpuščaji.",
                             kom="Uporaba Epipena je potrebna le v primeru anafilaktične reakcije, ko pride tudi do dihalne stiske, motenj zavesti in/ali prebavnih težav.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal,vpr="Po uporabi epipena nevarnosti ni več, zato nam ni treba več klicati reševalcev.",
                                                 kom="Nekaj časa po uporabi Epipena se reakcija lahko ponovi, zato je klic na 112 pri anafilaktični reakciji v vsakem primeru nujno potreben.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal,vpr="Epipen lahko uporabimo kar skozi hlače (ni potrebna uporaba na golo kožo).",
                                                 kom=" ")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

            vpr = MQ(nal=nal,vpr="Pri uporabi epipena je najpomembnejša natančnost vboda.",
                                     kom="Točna lokacija vboda ni tako pomembna. Z vbodom v zunanjo stran stegna zadenemo veliko in dobro prekrvavljeno mišico, od koder zdravilo hitro pride v kri.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal,vpr="Epipen uporabimo, če se pri alergični osebi po stiku z alergenom nenadoma pojavijo prebavne težave.",
                                                 kom=" ")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

            vpr = MQ(nal=nal,vpr="Če imaš epipen, ni potrebno odstraniti stvari, na katero je oseba alergična.",
                                                 kom="Odstranitev alergena je vedno nujen ukrep.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal,vpr="Pred uporabo je treba odstraniti moder zamašek na epipenu.",
                                                 kom=" ")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

def mk_obv_tpo():
    if MchoiceTask.objects.filter(display_name="Temeljni postopki oživaljanja", name="tpo",
                                  max_points=0, category="obv").count() == 0:
        print(f"creating obv: TPO")
        with transaction.atomic():
            nal = MT(display_name="Temeljni postopki oživaljanja", name="tpo",
                     max_points=0, category="obv")

            vpr = MQ(nal=nal, vpr="TPO izvajamo pri neodzivnih, ki ne dihajo.", kom=" ")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

            vpr = MQ(nal=nal, vpr="Oživljanje otroka začnemo s 5 vpihi.", kom=" ")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

            vpr = MQ(nal=nal, vpr="Stise in vpihe izvajamo v razmerju 30:3.", kom="Pravilno razmerje je 30:2")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal, vpr="Pri izvajanju TPO so vpihi obvezni. Če jih ne želimo izvajati, je bolje, da se tudi stisov ne lotimo.",
                                                 kom="Vpihi so priporočeni, niso pa obvezni. Najbolj ključen del oživljanja so stisi prsnega koša, zato je v primeru, da vpihov ne želimo izvajati, bolje, da se lotimo le stisov.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal, vpr="AED lahko uporabljajo le za to usposobljene osebe.",
                                                 kom="AED lahko uporabi kdorkoli. Za uporabo je popolnoma varen, če le sledimo njegovim navodilom.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

def mk_obv_splosno():
    if MchoiceTask.objects.filter(display_name="Splošno - pristop, pregled, komunikacije",
                                  name="splosno", max_points=0, category="obv").count() == 0:
        print(f"creating obv: splosno")
        with transaction.atomic():
            nal = MchoiceTask.objects.create(display_name="Splošno - pristop, pregled, komunikacije",
                                             name="splosno", max_points=0, category="obv")

            vpr = MQ(nal=nal, vpr="Po pristopu k poškodovancu preverimo varnost okolice.", kom="Varnost preverimo PRED pristopom.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal, vpr="Ocenimo, da pristop ni varen, pustimo poškodovanca in pobegnemo na varno.",
                     kom="V primeru, da ni varno, k poškodovancu ne pristopamo. Pokličemo 112 in jih obvestimo o okoliščinah.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal, vpr="Najprej ogovorimo. Če se ne odzove, ga primemo za ramena in rahlo stresemo.", kom=" ")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

            vpr = MQ(nal=nal, vpr="Primeru suma na poškodbo hrbtenice (prometne nesreče, padci z višine) poškodovanca čim manj premikamo.", kom=" ")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

            vpr = MQ(nal=nal, vpr="Se poškodovani odzove, verjetno ne potrebuje pomoči.",
                     kom="Če se poškodovani odzove, z naslednjimi vprašanji poskusimo pridobiti čimveč informacij o poškodovancu: kako se počuti in kaj se je zgodilo, ali ima kakšne alergije, bolezni in zdravila ter kdaj je nazadnje jedel. Ukrepamo v skladu z ugotovitvami.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal, vpr="Se poškodovani ne odzove, preverimo dihanje.",
                     kom="Pred preverjanjem dihanja najprej sprostimo dihalno pot - glavo zvrnemo močno nazaj.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal, vpr="Oseba diha normalno, je nezavestna. Namestimo jo v stabilni bočni položaj.", kom=" ")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

            vpr = MQ(nal=nal, vpr="Je nezavestni nameščen v stabilen bočni položaj, smo z ukrepanjem zaključili in lahko poškodovanca zapustimo.",
                     kom="Pokličemo 112 in redno spremljamo, ali nezavestni še diha.")
            MA(vpr=vpr, ans="Drži", prav=False)
            MA(vpr=vpr, ans="Ne drži", prav=True)

            vpr = MQ(nal=nal, kom=" ",
                     vpr="Oseba ne diha ali ne diha normalno (neenakomerno podihava, hrope, smrči), takoj pokličemo 112 in začnemo s temeljnimi postopki oživljanja.")
            MA(vpr=vpr, ans="Drži", prav=True)
            MA(vpr=vpr, ans="Ne drži", prav=False)

class Command(BaseCommand):
    help = "Generate QR code images in current dir"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for m in reversed((MchoiceTask, MchoiceQuestion, MchoiceAnswer)):
            m.objects.all().delete()

        mk_nnz_imobilizacija()
        mk_obv_krvavitve()
        mk_obv_zastrupitve()
        mk_obv_stanja()
        mk_nnz_epipen()
        mk_obv_tpo()
        mk_obv_splosno()
