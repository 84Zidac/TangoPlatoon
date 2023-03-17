from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    students = Student.objects.all().values()
    data = {
        'students' : students
    }
    return render(request, "pages/index.html", data)


@csrf_exempt
def new_student(request):
    try:
        body = json.loads(request.body)
        student = Student.objects.create(name = body['name'], email = body['email'])
        student.save()
        return JsonResponse({'success' : True})
    except Exception as e:
        print(e)
        return JsonResponse({'success' : False})
    
# def student_info(request, id):
    # return render(request, 'pages/studentInfo.html', data)