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
print(opts)
print(list(zip(opts,opts)))
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
        print(len(s), len(r), r)
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
        print(self.cleaned_data['r1'])
        print(self.cleaned_data['r2'])
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
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
        (5, 'E'),
        (6, 'F'),
        (7, 'G'),
        (8, 'H'),
        (9, 'I'),
    )

    opts1 = forms.ChoiceField(choices=CHOICES)
    opts2 = forms.ChoiceField(choices=CHOICES)
    opts3 = forms.ChoiceField(choices=CHOICES)
    opts4 = forms.ChoiceField(choices=CHOICES)
    opts5 = forms.ChoiceField(choices=CHOICES)
    opts6 = forms.ChoiceField(choices=CHOICES)

    def correct(self):
        return ({ 'correct': self.cleaned_data['opts1'] == '6'
                and self.cleaned_data['opts2'] == '3'
                and self.cleaned_data['opts3'] == '4'
                and self.cleaned_data['opts4'] == '9'
                and self.cleaned_data['opts5'] == '1'
                and self.cleaned_data['opts6'] == '8'})


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
