'''
HTML Forms - basic form which can help us to take user inputs
Django Forms - Data doesn't directly go in db
Model Forms - data directly goes in db
'''
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    address = forms.CharField(label='Your Address', max_length=100)

