from django.urls import path, include

from users import views

urlpatterns = [
    path('', views.authentication, name='authentication'),
    path('success', views.success, name='success')
    ]
