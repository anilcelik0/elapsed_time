from django import forms
from .models import TimeRecord, TimeMainTopic


class TimeRecordForm(forms.ModelForm):
    
    hour = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class":"form-control",
                "type":"date"
            }
        )
    )
    
    class Meta:
        model = TimeRecord
        fields = ('hour','date',)