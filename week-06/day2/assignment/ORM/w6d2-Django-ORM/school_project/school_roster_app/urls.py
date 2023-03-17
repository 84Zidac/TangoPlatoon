from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.new_student, name= 'new_student'),
    # path('student_info/<int:id>/, views.student_info),
]
