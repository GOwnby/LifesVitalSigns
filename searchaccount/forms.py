from django import forms

class SearchForm(forms.Form):
    username = forms.CharField(label='Search User', max_length=100)
