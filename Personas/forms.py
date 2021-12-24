from django import forms


class clienteForm(forms.Form):
    iden = forms.IntegerField()
    nombre = forms.CharField()
    apellidos = forms.CharField()
    direccion = forms.CharField()
    correo = forms.EmailField()

class autorForm(forms.Form):
    pseudonimo = forms.CharField()
    direccion = forms.CharField()
    correo = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)