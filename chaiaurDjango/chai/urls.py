from django.urls import path, include
from . import views

# The url now looks like http://localhost:8000/chai
urlpatterns = [
    path('', views.all_chai, name='all_chai')
]
