from django import forms
from django.forms import widgets

class NNZKlic(forms.Form):
    opts1 = forms.BooleanField(required=False, initial=False)
    opts2 = forms.BooleanField(required=False, initial=False)
    opts3 = forms.BooleanField(required=False, initial=False)

    def correct(self):
        return { 'correct' : (not self.cleaned_data['opts1']
                and self.cleaned_data['opts2']
                and not self.cleaned_data['opts3']) }


opts = sorted(["",
        "mrežico", "svetilo", "hladno vodo", "30 minut", "prevelik",
        "sladoled", "Sonce", "prevroč", "opekel zaradi trenja", "15 minut",
        "zažganem", "topli čaj", "osmodil", "šoku", "zardel", "pustil počivati", "ožganega" ])
assert len(opts) == 18

s = ["Sonce", "svetilo", "opekel zaradi trenja", "šoku", "hladno vodo", "15 minut",
     "mrežico", "pustil počivati", "osmodil", "zažganem", "prevroč",
        "ožganega", "zardel", "sladoled"]


class NNZOpekline(forms.Form):
    f1  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f2  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f3  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f4  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f5  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f6  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f7  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f8  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f9  = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f10 = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f11 = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f12 = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f13 = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))
    f14 = forms.CharField(initial="", max_length=30, widget=forms.Select(choices=list(zip(opts, opts))))

    def correct(self):
        r = [self.cleaned_data[f"f{i}"] for i in range(1, len(s)+1)]
        assert len(r) == len(s)
        return { 'correct' : s == r,
                'sol': ( {f"f{i}" : s[i-1] for i in range(1, len(s)+1)}
                        |{f"c{i}" : "green" if s[i-1] == r[i-1] else "red" for i in range(1, len(s)+1)})}


class TrivialForm(forms.Form):
    pass

class OBVImobilizacija(forms.Form):
    r1 = forms.CharField(max_length=40, widget=forms.RadioSelect(choices=(('Leva fotografija','Leva fotografija'), ('Desna fotografija','Desna fotografija'))))
    r2 = forms.CharField(max_length=40, widget=forms.RadioSelect(choices=(('Leva fotografija','Leva fotografija'), ('Desna fotografija','Desna fotografija'))))

    def correct(self):
        d = { 'first' : self.cleaned_data['r1'] == 'Leva fotografija',
             'second' : self.cleaned_data['r2'] == 'Desna fotografija' }
        return d | { 'correct' : d['first'] and d['second'] }

class NNZNezavest(forms.Form):
    CHOICES = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
        (5, 'E'),
        (6, 'F'),
        (7, 'G'),
        (8, 'H'),
    )

    opts1 = forms.ChoiceField(choices=CHOICES)

    def correct(self):
        return ({'correct': self.cleaned_data['opts1'] == '3'})


class NNZKrvavitve(forms.Form):
    CHOICES = (
        (0, ''),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, 'Koraka na sliki ne smemo narediti'),
    )

    optsA = forms.ChoiceField(choices=CHOICES)
    optsB = forms.ChoiceField(choices=CHOICES)
    optsC = forms.ChoiceField(choices=CHOICES)
    optsD = forms.ChoiceField(choices=CHOICES)
    optsE = forms.ChoiceField(choices=CHOICES)
    optsF = forms.ChoiceField(choices=CHOICES)
    optsG = forms.ChoiceField(choices=CHOICES)
    optsH = forms.ChoiceField(choices=CHOICES)

    def correct(self):
        return ({ 'correct': self.cleaned_data['optsA'] == '5'
                and self.cleaned_data['optsB'] == '7'
                and self.cleaned_data['optsC'] == '2'
                and self.cleaned_data['optsD'] == '3'
                and self.cleaned_data['optsE'] == '4'
                and self.cleaned_data['optsF'] == '1'
                and self.cleaned_data['optsG'] == '7'
                and self.cleaned_data['optsH'] == '6' })


class OBVOpekline(forms.Form):
    opts1 = forms.BooleanField(required=False, initial=False)
    opts2 = forms.BooleanField(required=False, initial=False)
    opts3 = forms.BooleanField(required=False, initial=False)
    opts4 = forms.BooleanField(required=False, initial=False)
    opts5 = forms.BooleanField(required=False, initial=False)
    opts6 = forms.BooleanField(required=False, initial=False)
    opts7 = forms.BooleanField(required=False, initial=False)
    opts8 = forms.BooleanField(required=False, initial=False)
    opts9 = forms.BooleanField(required=False, initial=False)
    opts10 = forms.BooleanField(required=False, initial=False)

    def correct(self):
        return ({ 'correct': self.cleaned_data['opts1']
                and not self.cleaned_data['opts2']
                and not self.cleaned_data['opts3']
                and not self.cleaned_data['opts4']
                and self.cleaned_data['opts5']
                and not self.cleaned_data['opts6']
                and self.cleaned_data['opts7']
                and not self.cleaned_data['opts8']
                and self.cleaned_data['opts9']
                and self.cleaned_data['opts10']})


class OBVPolozaji(forms.Form):
    CHOICES = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
        (5, 'E'),
    )

    opts1 = forms.ChoiceField(choices=CHOICES)
    opts2 = forms.ChoiceField(choices=CHOICES)
    opts3 = forms.ChoiceField(choices=CHOICES)

    def correct(self):
        return ({ 'correct': self.cleaned_data['opts1'] == '4'
                and self.cleaned_data['opts2'] == '2'
                and self.cleaned_data['opts3'] == '1'})


alergchoices = [
    (0, 'težko dihanje'),
    (1, 'tiščoča bolečina za prsnico'),
    (2, 'slabost in bruhanje'),
    (3, 'hud glavobol'),
    (4, 'koprivnica (kožni izpuščaj)'),
]
koraki = [
    '-------------',
    'odstranimo modro varovalo',
    'pokličemo 112',
    'epipen z oranžnim koncem zapičimo v stegno, lahko kar skozi hlače',
]
korakchoices = tuple(map(lambda a: (a, a), koraki))
class OBVAlergije(forms.Form):
    simpt = forms.MultipleChoiceField(choices=alergchoices,
                                      widget=widgets.CheckboxSelectMultiple)

    korak1 = forms.ChoiceField(choices=korakchoices, required=False)
    korak2 = forms.ChoiceField(choices=korakchoices, required=False)
    korak3 = forms.ChoiceField(choices=korakchoices, required=False)

    def correct(self):
        from django.template.loader import get_template
        kor_templ = get_template('naloge/alerg_sol_korak.html')

        def kor_check(cans, uans, num, Num):
            return kor_templ.render({
                'cans': cans,
                'uans': uans,
                'num': num,
                'Num': Num,
                })

        cd = self.cleaned_data
        pravisimpt = list(range(0, 5, 2))
        simpt = [((str(i) in cd['simpt']) == (i in pravisimpt), simptom, i in pravisimpt) for (i, simptom) in alergchoices]
        return { 'correct' :
                { 'simpt': simpt,
                 'korak1': kor_check('odstranimo modro varovalo', cd['korak1'], 'prvi', 'Prvi'),
                 'korak2': kor_check('epipen z oranžnim koncem zapičimo v stegno, lahko kar skozi hlače', cd['korak2'], 'drugi', 'Drugi'),
                 'korak3': kor_check('pokličemo 112', cd['korak3'], 'tretji', 'Tretji'),
                 },
                }


post = [
    ('Zaščiti ga pred mrazom, prizadete dele telesa postopoma ogrevaj.', ''),
    ('Ne spodbujaj gibanja, aktivno ga grej z nečim toplim.', 'Ko se podhlajeno telo ne ogreva več z drgetanjem, ga grejemo le še pasivno, ne več z gibanjem.'),
    ('Spodbujaj ga, da se giblje in po požirkih pije tople in sladke napitke, da se pogreje. Poskrbi, da ima oblečena suha in topla oblačila ter da je na toplem in v zavetrju.', 'Dokler je podhlajeni pri zavesti in se njegovo telo poskuša ogreti z drgetanjem, ga najbolj učinkovito z navedenimi ukrepi.'),
    ('Sprosti tesna mesta obleke, naj pije topel napitek. Prizadete dele telesa ogrevaj z namakanjem v topli vodi za 30 min.', ''),
]
simpt = [
    'Prizadeti je premražen, pri zavesti in dregeta.',
    'Prizadeti je premražen, zaspan in otopel.',
    'Prizadeti ima ozeblino (koža je bleda, svetleča, razpokana in manj občutljiva na mraz).',
    'Prizadeti ima omrzlino (koža je bleda, modrikasta, nastanejo lahko mehurji).',
]
simpt_display = [
        ('Če je', 'prizadeti premražen, pri zavesti in dregeta'),
        ('Če je', 'prizadeti premražen, zaspan in otopel'),
        ('Če ima', 'prizadeti ozeblino (koža je bleda, svetleča, razpokana in manj občutljiva na mraz)'),
        ('Če ima', 'prizadeti omrzlino (koža je bleda, modrikasta, nastanejo lahko mehurji)'),
]
choices = tuple(map(lambda a: (a[0], a[0]), [('---------------', '')] + post))

class OBVMraz(forms.Form):

    posk1 = forms.ChoiceField(label=simpt[0], choices=choices, required=False)
    posk2 = forms.ChoiceField(label=simpt[1], choices=choices, required=False)
    posk3 = forms.ChoiceField(label=simpt[2], choices=choices, required=False)
    posk4 = forms.ChoiceField(label=simpt[3], choices=choices, required=False)

    def correct(self):

        post_orig = [
            'Spodbujaj ga, da se giblje in po požirkih pije tople in sladke napitke, da se pogreje. Poskrbi, da ima oblečena suha in topla oblačila ter da je na toplem in v zavetrju.',
            'Ne spodbujaj gibanja, aktivno ga grej z nečim toplim.',
            'Zaščiti ga pred mrazom, prizadete dele telesa postopoma ogrevaj.',
            'Sprosti tesna mesta obleke, naj pije topel napitek. Prizadete dele telesa ogrevaj z namakanjem v topli vodi za 30 min.',
        ]
        post_display = [
            ('ga spodbujaj, da se giblje in po požirkih pije tople in sladke napitke, da se pogreje. Poskrbi, da ima oblečena suha in topla oblačila ter da je na toplem in v zavetrju', 'Dokler je podhlajeni pri zavesti in se njegovo telo poskuša ogreti z drgetanjem, je to tako najbolj učinkovito.'),
            ('ne spodbujaj gibanja, aktivno ga grej z nečim toplim', 'Ko se podhlajeno telo ne ogreva več z drgetanjem, ga grejemo le še pasivno, ne več z gibanjem.'),
            ('ga zaščiti pred mrazom in prizadete dele telesa postopoma ogrevaj', ''),
            ('sprosti tesna mesta obleke in naj pije topel napitek. Prizadete dele telesa ogrevaj z namakanjem v topli vodi za 30 min', ''),
        ]

        from django.template.loader import get_template
        posk_templ = get_template('naloge/mraz_sol_posk.html')

        def kor_check(i, uans):
            tip = "prav" if post_orig[i] == uans else "prazno" if uans == '---------------' else "narobe"
            return posk_templ.render({
                'tip': tip,
                'simpt': simpt_display[i],
                'cans': post_display[i][0],
                'razl': post_display[i][1],
                'uans': uans,
                })

        cd = self.cleaned_data
        ret = { 'correct' : { f'posk{i+1}': kor_check(i, cd[f'posk{i+1}']) for i in range(4) }, }
        return ret
