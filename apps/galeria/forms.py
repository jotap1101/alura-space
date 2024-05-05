from django import forms
from apps.galeria.models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        fields = ['nome', 'legenda', 'categoria', 'descricao', 'imagem', 'data_fotografia', 'user']
        labels = {
            'nome': 'Nome',
            'legenda': 'Legenda',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'imagem': 'Imagem',
            'data_fotografia': 'Data da Fotografia',
            'user': 'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%d/%m/%Y'),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }