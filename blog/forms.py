from django import forms

class PostSearchForm(forms.Form):
    q = forms.CharField()