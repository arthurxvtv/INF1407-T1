"""
Created on 15 de out de 2024
@author: arthurxvtv
"""
from django import forms
from ReviewApp.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["user", "game_name", "stars"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(ReviewForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["user"].initial = user
            self.fields["user"].disabled = True
        self.fields["stars"].widget.attrs.update({'min': 0, 'max': 5})
