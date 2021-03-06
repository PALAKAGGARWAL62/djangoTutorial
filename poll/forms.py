'''
HTML Forms - basic form which can help us to take user inputs
Django Forms - Data doesn't directly go in db
Model Forms - data directly goes in db
'''
from cProfile import label
from django import forms
from django.forms import ModelForm, Textarea, formset_factory
from .models import Article, Fruit, Publication

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

class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

ArticleFormSet = formset_factory(ArticleForm, extra=2)

