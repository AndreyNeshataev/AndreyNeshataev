from django import forms
from django.forms import Textarea
from .models import *


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = News
        fields = ['title', 'slug', 'article', 'activity_flag', 'tags']
        widgets = {
            'title': forms.Textarea(attrs={'class': 60, 'rows': 2}),
            'article': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'tags': forms.SelectMultiple(attrs={'cols': 60, 'rows': 1}),
        }


class CommentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comments
        fields = ('commentary', 'author')
        widgets = {
            'author': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
            'commentary': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
            }
