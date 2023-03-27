from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_sign_up, name='signup'),
    path('signin/', views.user_sign_in, name= 'signin'),
    path('curruser/', views.curr_user, name= 'curruser'),
    path('signout/', views.user_sign_out, name= 'signout'),
    path("", views.sign_up, name="signup_form"),
    path("sign_in/", views.sign_in, name="signin_form"),
    path("tasks/", views.user_tasks, name='tasks')
]
