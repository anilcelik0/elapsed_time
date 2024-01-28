from django import forms
from .models import QuestionRecord, QuestionMainTopic


class QuestionRecordForm(forms.ModelForm):
    
    question_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    correct_answer = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        ),
        required=False
    )
    
    wrong_answer = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        ),
        required=False
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
        model = QuestionRecord
        fields = ('question_count','correct_answer','wrong_answer','date',)

