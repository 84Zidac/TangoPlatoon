from django.shortcuts import render
from datetime import datetime
import random



users = {}
# Create your views here.
def increment_count(request):
    if not request.COOKIES.get('user_id'):
        user_id_number = str(random.randint(100000,999999))
    else:
        user_id_number = request.COOKIES.get('user_id')
    if not request.session.get('count'):
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    users[user_id_number] = request.session['count']
    response = render(request, 'main.html', {
        'count': request.session.get('count'),
    })
    response.set_cookie('user_id', user_id_number)
    print(users)
    return response