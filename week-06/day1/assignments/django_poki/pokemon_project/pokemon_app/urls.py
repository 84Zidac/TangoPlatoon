from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_pokes/', views.get_pokes, name='get_pokes')
]
