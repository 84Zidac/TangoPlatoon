from django.urls import path
from . import views

urlpatterns = [
        # ex: /polls/
    path('', views.index),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote),
]