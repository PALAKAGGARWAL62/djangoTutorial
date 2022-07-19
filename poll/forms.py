'''
HTML Forms - basic form which can help us to take user inputs
Django Forms - Data doesn't directly go in db
Model Forms - data directly goes in db
'''
from django import forms
from django.forms import ModelForm, Textarea
from .models import Fruit

class NameForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    address = forms.CharField(label='Your Address', max_length=100)
    email = forms.EmailField(label='Email id', help_text = 'Enter valid email id')
    
class FruitForm(ModelForm):

    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name':Textarea(attrs={'cols':80, 'row':20,},)
        }

