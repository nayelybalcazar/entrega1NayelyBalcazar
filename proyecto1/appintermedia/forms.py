from django import forms

class ProductoFormulario(forms.Form):

    nombre=forms.CharField()
    color=forms.CharField()
    talla=forms.IntegerField()