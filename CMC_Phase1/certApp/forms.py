from django import forms
from certApp.models import Certificate

class CertificateForm(forms.ModelForm):   #ModelForm connects form and model
    class Meta:
        model = Certificate
        fields = '__all__'
