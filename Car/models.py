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
    video = models.URLField(null=True)
    service_available = models.BooleanField(default=False)
    service_description = models.TextField(default=False)
    service_cost = models.PositiveIntegerField(default=False)

    def __str__(self):
        return self.title

class CommentCar(models.Model):
    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )
    car_choice_comment = models.ForeignKey(CarShop, on_delete=models.CASCADE, related_name="comment_object")
    text = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=RATING)

def __str__(self):
    return self.rate_stars


class CommentPeople(models.Model):
    RATING_CHOICES = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )
    car_choice_comment = models.ForeignKey(CarShop, on_delete=models.CASCADE, related_name="comment_people", null=True)
    text = models.TextField(null=True)
    rate_stars = models.CharField(null=True, max_length=5, choices=RATING_CHOICES)