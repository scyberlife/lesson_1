from django import forms
from . import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarShop
        fields = '__all__'


class CommentForm(forms.ModelForm):
    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )
    rate_stars = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    class Meta:
        model = models.CommentPeople
        fields = ['text', 'rate_stars', 'car_choice_comment']