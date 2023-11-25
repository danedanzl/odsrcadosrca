from django.db import transaction
from naloge.models import Task, MchoiceTask, MchoiceQuestion, MchoiceAnswer


with transaction.atomic():

    zvinizlomi = MchoiceTask.objects.create(display_name="Zvini in zlomi - imobilizacija",
                                            name="imobilizacija",
                                            max_points=3, category="nnz")


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

