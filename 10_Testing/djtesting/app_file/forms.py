from django import forms
from .models import *


class UploadPostForm(forms.ModelForm):

    class Meta:
        model = AppFile
        fields = ('file', )



