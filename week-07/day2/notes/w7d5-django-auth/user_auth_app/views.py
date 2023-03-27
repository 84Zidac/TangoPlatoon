from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

def sign_up(request):
    return render(request, "pages/sign_up.html")

def sign_in(request):
    return render(request, "pages/sign_in.html")

@api_view(["POST"])
def user_sign_up(request):
    print(request.user)
    email = request.data['email']
    password = request.data['password']
    name = request.data['name']
    super_user = False
    staff = False
    if 'super' in request.data:
        super_user = request.data['super']
    if 'staff' in request.data:
        staff = request.data['staff']
    try:
        new_user = App_User.objects.create_user(username = email, email = email, name = name, password = password, is_superuser = super_user, is_staff = staff)
        new_user.save()
        return JsonResponse({"success":f"{name}, your user was created"})
    except Exception as e:
        print(e)
        return JsonResponse({"success": False})


@api_view(["POST"])
def user_sign_in(request):
    email = request.data['email']
    password = request.data['password']
    print(request._request)
    user = authenticate(username = email , password = password)
    if user is not None and user.is_active:
        try:
            login(request._request, user)
            return JsonResponse({'signin':True})
        except Exception as e:
            print(e)
            return JsonResponse({'signin':False})
    return JsonResponse({'signin':False})


@api_view(["GET"])
def curr_user(request):
    if request.user.is_authenticated:
        print(request.user)
        #                    format       query                     options
        user_info = serialize("json",  [request.user], fields = ['name', 'email'])
        user_info_workable = json.loads(user_info)
        return JsonResponse({"user_info": user_info_workable[0]})
    else:
        return JsonResponse({"user":None})
    
    
api_view(['POST'])
def user_sign_out(request):
    try:
        logout(request)
        return JsonResponse({"signout":True})
    except Exception as e:
        print(e)
        return JsonResponse({"signout":False})
        
        
        
@api_view(["GET","POST"])
def user_tasks(request):
    if request.method == 'GET':
        tasks = list(Task.objects.filter(user = request.user).values())
        return render(request, "pages/tasks.html", {"tasks":tasks})
    elif request.method == 'POST':
        new_task = Task.objects.create(title = request.data['title'], description = request.data['description'], user = request.user)
        new_task.save()
        return JsonResponse({'success' : True})
        