from django import forms

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
