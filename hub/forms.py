from django import forms
from .models import StudentWebPage

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = StudentWebPage
        fields = ['title', 'author', 'file']