from django.urls import path
from . import views

urlpatterns =[
    path('homee', views.home, name="homee"),
    path('service', views.service, name="service")
]