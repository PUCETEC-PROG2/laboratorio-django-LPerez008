from django import forms
from .models import Pokemon, Trainer    #añadir un (.) antes de models


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels={
            'name': 'Nombre',
            'type': 'Tipo',
            'weight': 'Peso',
            'height': 'Altura',
            'trainer': 'Entrenador',
            'picture': 'Imagen',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'type': forms.Select(attrs={'class' : 'form-control'}),
            'weight': forms.NumberInput(attrs={'class' : 'form-control'}),
            'height' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'trainer' : forms.Select(attrs={'class': 'form-control'}),
            'picture' : forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'birth_date' : 'Fecha de nacimiento',
            'level' : 'Nivel',
            'picture' : 'Imagen',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type' : 'date', 'class' : 'form-control'}),
            'level' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'picture' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
