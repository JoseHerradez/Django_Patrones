from django import forms
from carrusel.breadcrumbs.models import Breadcrumbs

class BreadcrumbsForm(forms.ModelForm):
    class Meta:
        model = Breadcrumbs
        fields = ('title', 'count', 'timer', 'circular', 'auto',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'timer': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        #image = forms.ImageField(widget=forms.ImageField)
        fields = ('title', 'description', 'url', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }
