from django import forms
from .models import Arendator

class ArendatorForm(forms.ModelForm):
    class Meta:
        model = Arendator
        fields = ['person', 'gos_num',
                  'box_num', 'auto',
                  'registered', 'ended']