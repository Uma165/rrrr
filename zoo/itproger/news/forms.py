from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm (ModelForm):
    class Meta:
        model=Articles
        fields = ['kind', 'name', 'full_text', 'date']

        widgets = {
            "kind": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название зверя'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя зверя'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                 'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о зверьке'
            })
        }