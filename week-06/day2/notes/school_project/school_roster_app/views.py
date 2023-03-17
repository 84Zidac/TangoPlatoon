from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    student1=Students()
    students = Students.objects.all().values
    print(students)
    data = {
        'students': students
    }
    return render(request, 'pages/index.html', data)


@csrf_exempt
def new_student(request):
    body = json.loads(request.body)
    student = Students.objects.create(name = body['name'], email = body['email'])
    student.save()
    return JsonResponse({'success': False})