from django import forms
from .models import Management

class ManageForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = '__all__'
        