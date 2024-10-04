'''
Created on 8 de out de 2019
@author: meslin
'''
from django import forms
from ReviewApp.models import Review


class ReviewForm(forms.ModelForm):
    """cala a boca pylint."""

    class Meta:


        model = Review
        fields = '__all__'
