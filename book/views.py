from django.shortcuts import render
from . import models


def book_view(request):
    books = models.Post.objects.all()
    return render(request, 'index.html', {'books': books})