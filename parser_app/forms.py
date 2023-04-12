from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('mashina.kg', 'mashina.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)


    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'mashina.kg':
            car_parser = parser.parser()
            for i in car_parser:
                models.MashinaKg.objects.create(**i)