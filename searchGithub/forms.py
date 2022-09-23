from re import search
from django import forms

searchKeyword = ""

class NameForm(forms.Form):
    searchKeyword = forms.CharField(label='Search for keyword:', max_length=100)