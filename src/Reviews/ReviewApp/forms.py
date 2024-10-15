"""
Created on 15 de out de 2024
@author: arthurxvtv
"""
from django import forms
from ReviewApp.models import Review


class ReviewForm(forms.ModelForm):
    """summary."""

    class Meta:


        model = Review
        fields = '__all__'
