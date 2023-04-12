from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('car_list/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('add_car/', views.CreateCarView.as_view(), name='add_car'),
    path('car_list/<int:pk>/update/', views.UpdateCarView.as_view(), name='update'),
    path('car_list/<int:pk>/delete/', views.DeleteCarView.as_view(), name='delete'),
    path('car_list/<int:pk>/add_comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('search/', views.Search.as_view(), name='search'),
]
