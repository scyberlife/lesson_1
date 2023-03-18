from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=50)

    def __str__(self):
        return self.title