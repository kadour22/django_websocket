from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.AddEmployerView.as_view())
]
