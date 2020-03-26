from django.urls import path

from . import views

app_name = 'leaves'
urlpatterns = [
    path('leave/', views.leave, name='leave'),
    path('liu/', views.liu, name='liu'),
]