# Generated by Django 4.1.7 on 2023-03-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название машины')),
                ('description', models.TextField(verbose_name='Описание машины')),
                ('image', models.ImageField(upload_to='')),
                ('car_type', models.CharField(choices=[('number1', 'number2'), ('number3', 'number4'), ('number5', 'number6')], max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('cost', models.PositiveIntegerField()),
                ('url', models.URLField()),
            ],
        ),
    ]
