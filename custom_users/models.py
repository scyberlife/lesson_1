from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    ADMIN = 1
    VIPClient = 2
    CLIENT = 3

    USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (VIPClient, 'VIPClient'),
        (CLIENT, 'Client')
    )

    MALE = 1
    FEMALE = 2
    OTHER = 3

    GENDER_TYPE = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER')
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    phone_number = models.CharField('Номер телефона', max_length=100, null=True)
    age = models.PositiveIntegerField('Ваш возраст',null=True)
    user_type = models.IntegerField('Тип пользователя', choices=USER_TYPE, null=True)
    gender = models.IntegerField('Пол', choices=GENDER_TYPE, null=True)
    country = models.CharField('Ваша страна', max_length=100, null=True)
    city = models.CharField('Город проживания', max_length=100, null=True)