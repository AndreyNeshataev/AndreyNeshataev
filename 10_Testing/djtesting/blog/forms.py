from django import forms
from .models import *


class PostForm(forms.ModelForm):
    photos = forms.FileField(required=False, label='Загрузить Фотографии',
                             widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title', 'article',  'tags', 'photos', 'published']  # 'slug' 'photo',
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'article': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Tag
        fields = ('title', 'slug')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


