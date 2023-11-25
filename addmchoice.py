from django.db import transaction
from naloge.models import Task, MchoiceTask, MchoiceQuestion, MchoiceAnswer


if MchoiceTask.objects.filter(display_name="Zvini in zlomi - imobilizacija",
                              name="imobilizacija", max_points=0,
                              category="nnz").count() == 0:
    print(f"creating nnz: Zvini in zlomi - imobilizacija")
    with transaction.atomic():

        zvinizlomi = MchoiceTask.objects.create(display_name="Zvini in zlomi - imobilizacija",
                                                name="imobilizacija",
                                                max_points=0, category="nnz")


        vpr1 = MchoiceQuestion.objects.create(nal=zvinizlomi, vpr="Očka Peter je "
                                              "med obiranjem drevesa poleti padel iz "
                                              "visoke lestve. Kaj moraš najprej "
                                              "narediti?")
        vpr2 = MchoiceQuestion.objects.create(nal=zvinizlomi, vpr="Ko je poskusil "
                                              "dvigniti pretežke uteži, se je Lukatu "
                                              "kar naenkrat vdala desna roka in zdaj "
                                              "ne more več premikati roke v komolcu. "
                                              "Na srečo so uteži padle mimo njega in "
                                              "ga niso dodatno poškodovale. Kaj "
                                              "narediš?")
        vpr3 = MchoiceQuestion.objects.create(nal=zvinizlomi, vpr="Na pohodu se "
                                              "Izak cel dan pritožuje, da se mu ne "
                                              "da več hoditi in da ga boli gleženj. "
                                              "Ko zvečer da nogo iz gojzarja, vidi, "
                                              "da je njegov gleženj otekel in ga "
                                              "strašansko boli že samo ob dotiku. "
                                              "Kaj se mu je najverjetneje zgodilo in "
                                              "kaj naj naredi?")


        MchoiceAnswer.objects.create(vpr=vpr1, ans="Hitro ga premakni v senco, da ne bo dehidriran.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr1, ans="Spravi ga v sedeč položaj, da se umiri od šoka pri padcu.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr1, ans="Roko mu daj v ruto pestovalko, saj ga boli.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr1, ans="Ne premikaj ga, saj ima mogoče poškodovano hrbtenico.", prav=True)

        MchoiceAnswer.objects.create(vpr=vpr2, ans="Rečeš mu, naj se spravi iz fitnesa, saj nima tu nič več iskati, če je poškodovan.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr2, ans="Komolec hladiš, ter nanj nalepiš obliž, da se bo hitreje zacelil.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr2, ans="Roko mu daš v ruto pestovalko, čeprav ga po njegovih besedah “boli ko svinja”.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr2, ans="Komolec hladiš in ga poviješ tako, da ga ne more premikati.", prav=True)

        MchoiceAnswer.objects.create(vpr=vpr3, ans="Gleženj si je zvil. Mora si ga naravnati nazaj in oteklina bo splahnela.", odg="", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr3, ans="V gleženj ga je pičila/ugriznila neka žival. Gleženj naj hladi in izjoka vso bolečino.", odg="", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr3, ans="Gleženj si je zvil. Čimbolj naj ga razgibava, kljub bolečini, saj se bo tako najhitreje spravil v normalno stanje.", odg="", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr3, ans="Gleženj si je zvil. Nanj naj si da obkladek in ga povije tako, da se ne bo premikal. Izogiba naj se hoji.", odg="", prav=True)

if MchoiceTask.objects.filter(display_name="Rane in krvavitve",
                              name="krvavitve", max_points=0,
                              category="obv").count() == 0:
    print(f"creating obv: Rane in krvavitve")
    with transaction.atomic():
        obvl_krvavitve = MchoiceTask.objects.create(display_name="Rane in krvavitve",
                                                    name="krvavitve",
                                                    max_points=0, category="obv")

        vpr = MchoiceQuestion.objects.create(nal=obvl_krvavitve, vpr="Kaj je notranja krvavitev?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Kri znotraj žil.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Krvavitev znotraj telesa, ki je lahko smrtno nevarna.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Krvavitev, ko je poškodovanec v notranjem prostoru.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=obvl_krvavitve, vpr="Kaj je tujek?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Priseljenec.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Zdravilo za pike eksotičnih mušic.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Tuj predmet v telesu.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Tuj predmet v bližini telesa.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=obvl_krvavitve, vpr="Kaj je šok?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Bolezensko stanje, ko srce ne zmore dovajati dovolj krvi vsem organom.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Reakcija, ko sosed prevara sosedo.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Reakcija na pik čebele.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Naslov pesmi Damjana Murka.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=obvl_krvavitve, vpr="Kaj je imobilizacija?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pritrditev uda, tujka ali drugega dela telesa, da mu je onemogočeno premikanje.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Povitje noge ali roke.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Odvzem prevoznega sredstva.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Zlom, ki se ne premika več.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=obvl_krvavitve, vpr="Kaj je sterilno?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Čisto, brez prisotnosti bakterij, umazanije.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Lepo urejeno, pospravljeno.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Direktno, brez ovinkov.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Jasno razloženo, enostavno predstavljeno.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=obvl_krvavitve, vpr="Kaj je kompresijska obveza?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Obveza naredjena pod časovnim pritiskom.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Obveza za večje rane, na katero pritisnemo dodaten trd predmet, da ustavimo krvavitev.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Posebni obliži, ki nadomestijo šive pri manjših ranah in jih nato povijemo.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Obveza narejena v kompresijski komori.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=obvl_krvavitve, vpr="Kaj je arterija?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Žila, po kateri teče kri, napolnjena s kisikom.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Žila, ki teče proti srcu.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Avto znamke Opel.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Bolezen, pri kateri doživljamo nihanje med nizkim in visokim krvnim tlakom.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=obvl_krvavitve, vpr="Kaj je vena?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Površinska žila tik pod kožo.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Grška boginja zdravja.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Zgornja srčna mišica.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Žila, ki teče prosti srcu.", prav=True)

if MchoiceTask.objects.filter(display_name="Zastrupitve",
                              name="zastrupitve", max_points=0,
                              category="obv").count() == 0:
    print(f"creating obv: Zastrupitve")
    with transaction.atomic():
        nal = MchoiceTask.objects.create(display_name="Zastrupitve",
                                         name="zastrupitve", max_points=0,
                                         category="obv")
        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Bruhanje lahko pri sumu zastrupitve izzovemo:")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Kadarkoli.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Čim prej po zaužitju strupene snovi.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Le po posvetu z zdravnikom.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Najpogostejše vrste zastrupitev so povezane:")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Z jemanjem prepovedanih substanc.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Z nekaterimi slabo označenimi gospodinjskimi pripomočki.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Z visoko količino ogljikovega monoksida v zaprtih prostorih.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Kaj moramo narediti, če sumimo, da je nekdo zastrupljen?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Takoj kličemo 112.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Klic na 112 pokličemo le, če smo prepričani, da je zastrupitev lahko smrtna.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Kličemo, ko se pokažejo prvi simptomi zastrupitve.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Kateri od navedenih ukrepov ob zastrupitvi ni pravilen?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Spravimo na varno.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Primeru izgube zavesti ga položimo v položaj za nezavestnega.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Primeru, da je zastrupljeni pri zavesti, lahko po manjših požirkih pije navadno vodo, da razredči strup.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Kateri od naštetih simptomov ni pogost simptom zastrupitve preko očesa?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Rdeče in razdražene oči.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Otekanje območja okoli oči.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Poškodbe oči in bolečina.", prav=False)

if MchoiceTask.objects.filter(display_name="Stanja",
                              name="stanja", max_points=0,
                              category="obv").count() == 0:
    print(f"creating obv: Stanja")
    with transaction.atomic():
        nal = MchoiceTask.objects.create(display_name="Stanja", name="stanja",
                                   max_points=0, category="obv")

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Kako pogosto lahko pri srčni kapi pod jezik poškropimo nitrolingual?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Na 5 minut.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Na 10 minut.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Samo 1-krat.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Katero zdravilo lahko damo posamezniku, kadar sumimo možgansko kap?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Aspirin.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Lekadol.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Nobenega.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Po koliko časa kličemo strokovno pomoč pri epileptičnem napadu?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Takoj.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Po 2-3 minutah.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Po 5 ali več minutah.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Kaj lahko damo osebi v hipoglikemičnem stanju, ki je pri zavesti?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Hrano, ki vsebuje veliko ogljikovih hidratov.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Hrano, ki vsebuje veliko proteinov.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Hrano, ki vsebuje veliko vlaknin.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Pri astmatičnem napadu naj bolnik zdravilo v pljučih:")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Izdihnihne takoj.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Počasi izdihne skozi nos.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Zadrži nekaj časa.", prav=True)

if MchoiceTask.objects.filter(display_name="Stanja",
                              name="stanja", max_points=0,
                              category="obv").count() == 0:
    print(f"creating obv: Stanja")
    with transaction.atomic():
        nal = MchoiceTask.objects.create(display_name="Stanja", name="stanja",
                                   max_points=0, category="obv")

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Kako pogosto lahko pri srčni kapi pod jezik poškropimo nitrolingual?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Na 5 minut.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Na 10 minut.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Samo 1-krat.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Katero zdravilo lahko damo posamezniku, kadar sumimo možgansko kap?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Aspirin.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Lekadol.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Nobenega.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Po koliko časa kličemo strokovno pomoč pri epileptičnem napadu?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Takoj.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Po 2-3 minutah.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Po 5 ali več minutah.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Kaj lahko damo osebi v hipoglikemičnem stanju, ki je pri zavesti?")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Hrano, ki vsebuje veliko ogljikovih hidratov.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Hrano, ki vsebuje veliko proteinov.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Hrano, ki vsebuje veliko vlaknin.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Pri astmatičnem napadu naj bolnik zdravilo v pljučih:")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Izdihnihne takoj.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Počasi izdihne skozi nos.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Zadrži nekaj časa.", prav=True)

if MchoiceTask.objects.filter(display_name="Epipen", name="epipen",
                              max_points=0, category="nnz").count() == 0:
    print(f"creating nnz: Epipen")
    with transaction.atomic():
        nal = MchoiceTask.objects.create(display_name="Epipen", name="epipen",
                                         max_points=0, category="nnz")

        vpr = MchoiceQuestion.objects.create(nal=nal,
                                             vpr="Epipen moramo uporabiti tudi pri lažjih alergijskih reakcijah, kot so na primer izpuščaji.",
                                             kom="Uporaba Epipena je potrebna le v primeru anafilaktične reakcije, ko pride tudi do dihalne stiske, motenj zavesti in/ali prebavnih težav.")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal,vpr="Po uporabi epipena nevarnosti ni več, zato nam ni treba več klicati reševalcev.",
                                             kom="Nekaj časa po uporabi Epipena se reakcija lahko ponovi, zato je klic na 112 pri anafilaktični reakciji v vsakem primeru nujno potreben.")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal,vpr="Epipen lahko uporabimo kar skozi hlače (ni potrebna uporaba na golo kožo).",
                                             kom=" ")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal,vpr="Pri uporabi epipena je najpomembnejša natančnost vboda.",
                                             kom="Točna lokacija vboda ni tako pomembna. Z vbodom v zunanjo stran stegna zadenemo veliko in dobro prekrvavljeno mišico, od koder zdravilo hitro pride v kri.")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal,vpr="Epipen uporabimo, če se pri alergični osebi po stiku z alergenom nenadoma pojavijo prebavne težave.",
                                             kom=" ")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal,vpr="Če imaš epipen, ni potrebno odstraniti stvari, na katero je oseba alergična.",
                                             kom="Odstranitev alergena je vedno nujen ukrep.")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal,vpr="Pred uporabo je treba odstraniti moder zamašek na epipenu.",
                                             kom=" ")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=False)

if MchoiceTask.objects.filter(display_name="Temeljni postopki oživaljanja", name="tpo",
                              max_points=0, category="obv").count() == 0:
    print(f"creating obv: TPO")
    with transaction.atomic():
        nal = MchoiceTask.objects.create(display_name="Temeljni postopki oživaljanja", name="tpo",
                                         max_points=0, category="obv")

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="TPO izvajamo pri neodzivnih, ki ne dihajo.", kom=" ")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Oživljanje otroka začnemo s 5 vpihi.", kom=" ")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=True)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=False)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Stise in vpihe izvajamo v razmerju 30:3.", kom="Pravilno razmerje je 30:2")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="Pri izvajanju TPO so vpihi obvezni. Če jih ne želimo izvajati, je bolje, da se tudi stisov ne lotimo.",
                                             kom="Vpihi so priporočeni, niso pa obvezni. Najbolj ključen del oživljanja so stisi prsnega koša, zato je v primeru, da vpihov ne želimo izvajati, bolje, da se lotimo le stisov.")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=True)

        vpr = MchoiceQuestion.objects.create(nal=nal, vpr="AED lahko uporabljajo le za to usposobljene osebe.",
                                             kom="AED lahko uporabi kdorkoli. Za uporabo je popolnoma varen, če le sledimo njegovim navodilom.")
        MchoiceAnswer.objects.create(vpr=vpr, ans="Pravilna.", prav=False)
        MchoiceAnswer.objects.create(vpr=vpr, ans="Napačna.", prav=True)
