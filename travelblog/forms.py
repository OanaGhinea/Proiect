from django import forms
from .models import Postare, Tipuri

# choices = [('calatorii', 'calatorii'),('curiozitati', 'curiozitati'),('divertisment' , 'divertisment')]
alegeri = Tipuri.objects.all().values_list('nume','nume')
lista_alegeri = []

for obiect in alegeri:
    lista_alegeri.append(obiect)
class FormularePostare(forms.ModelForm):
    class Meta:
        model = Postare
        fields = ('titlu','titlu_nav','tipuri','autor','cuprins', 'imagine_blog')
        widgets = {
            'titlu': forms.TextInput(attrs={'class':'form-control'}),
            'titlu_nav': forms.TextInput(attrs={'class': 'form-control'}),
            'cuprins': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'tipuri': forms.Select(choices=lista_alegeri,attrs={'class': 'form-control'}),

        }

class EditPostare(forms.ModelForm):
    class Meta:
        model = Postare
        fields = ('titlu','titlu_nav','cuprins')
        widgets = {
            'titlu': forms.TextInput(attrs={'class':'form-control'}),
            'titlu_nav': forms.TextInput(attrs={'class': 'form-control'}),
            'cuprins': forms.Textarea(attrs={'class': 'form-control'}),

        }