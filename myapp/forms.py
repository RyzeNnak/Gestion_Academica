from django import forms

class EjemploForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)