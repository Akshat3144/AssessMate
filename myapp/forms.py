from django import forms
from .models import UploadedFile

class Fileform(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)
