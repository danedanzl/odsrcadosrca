from django import forms

gopts = ["", "Rešujem sam"]+[str(i) for i in range(2,11)] + ["10 - 15", "Več kot 15"]
gopts = list(zip(gopts, gopts))

sopts = ["", "6 - 11 let", "12 - 15 let", "16 - 21", "22 - 30", "31 - 45", "46 65", "66 - ..."]
sopts = list(zip(sopts, sopts))

class Register(forms.Form):
    email = forms.CharField(label="Prosili bi vas, da nam zaupate svoj e-poštni naslov. Po zaključku dogodka vam želimo poslati kratko zahvalo, vprašalnik o zadovoljstvu ter nekaj dodatnih informacij.", max_length=200,
                            widget=forms.TextInput(), required=False) # TODO validator?
    group = forms.CharField(label="Boste reševali kot skupina? Če da, koliko vas je?", max_length=30,
                            widget=forms.Select(choices=gopts), required=False)
    starost = forms.CharField(label="Koliko si star (če vas je več, kaj je najpogostejša starost v skupini)?", max_length=30,
                              widget=forms.Select(choices=sopts), required=False)
