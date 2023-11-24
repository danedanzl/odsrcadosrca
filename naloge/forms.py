from django import forms

class NNZKlic(forms.Form):
    opts1 = forms.BooleanField(required=False, initial=False)
    opts2 = forms.BooleanField(required=False, initial=False)
    opts3 = forms.BooleanField(required=False, initial=False)

    def correct(self):
        return (not self.cleaned_data['opts1']
                and self.cleaned_data['opts2']
                and not self.cleaned_data['opts3'])
