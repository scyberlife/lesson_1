from django.urls import path
from . import views

urlpatterns = [
    path('car_lists/', views.ParserCarView.as_view(), name='car_lists'),
    path('parser_car/', views.ParserFormView.as_view(), name='start_parsing'),

]