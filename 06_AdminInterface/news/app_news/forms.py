from django import forms

from .models import *


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = News
        fields = ['title', 'article', 'activity_flag']
        widgets = {
            'title': forms.Textarea(attrs={'cols': 60, 'rows': 2}),
            'article': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class CommentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comments
        fields = ['user_name', 'commentary']
        widgets = {
            'user_name': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
            'commentary': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
            }
