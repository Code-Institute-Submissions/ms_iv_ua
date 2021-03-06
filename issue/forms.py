from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('subj', 'desc')
        labels = {
            'subj':'Issue Title *',
            'desc':'Detailed Issue Description *',
        }
        widgets = {
            'subj':forms.TextInput(attrs={
                'class':'form-control ua-required',
                'aria-describedby':'issue title',
                'placeholder':'Issue title',
                'minlength':'1',
                'maxlength':'80',
            }),
            'desc':forms.Textarea(attrs={
                'class':'form-control ua-required char-countdown',
                'aria-describedby':'issue description',
                'placeholder':'Enter detailed issue description',
                'cols':70, 'rows':10,
                'minlength':'1',
                'maxlength':'1000',
            }),
        }
