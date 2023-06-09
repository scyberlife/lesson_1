# Generated by Django 4.1.7 on 2023-04-09 14:59

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=100, null=True, verbose_name='Номер телефона')),
                ('age', models.PositiveIntegerField(null=True, verbose_name='Ваш возраст')),
                ('user_type', models.IntegerField(choices=[(1, 'ADMIN'), (2, 'VIPClient'), (3, 'Client')], null=True, verbose_name='Тип пользователя')),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'OTHER')], null=True, verbose_name='Пол')),
                ('country', models.CharField(max_length=100, null=True, verbose_name='Ваша страна')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='Город проживания')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
