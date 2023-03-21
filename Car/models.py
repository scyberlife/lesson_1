from django.db import models

class CarShop(models.Model):
    CAR_TYPE = (
        ('number1', "number2"),
        ('number3', "number4"),
        ('number5', "number6")

    )
    title = models.CharField("Название машины", max_length=100)
    description = models.TextField("Описание машины")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    url = models.URLField()

    def __str__(self):
        return self.title