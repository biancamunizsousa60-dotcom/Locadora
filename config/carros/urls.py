from django.urls import path
from . import views

app_name = 'carros'

urlpatterns = [
    path('', views.CarroListView.as_view(), name='lista'),
    path('novo/', views.CarroCreateView.as_view(), name='novo'),
    ]