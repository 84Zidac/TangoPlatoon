from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
import json
import pprint
import os
from dotenv import load_dotenv

load_dotenv()

pp=pprint.PrettyPrinter(indent=2, depth=2)
# Create your views here.
def home(request):
    return render(request, 'pages/noun_form.html')

def item(request):
    item_title = request.POST.get('item')
    # print(item_title)
    auth = OAuth1(os.environ['api_key'], os.environ['secret_key'])
    endpoint = f"http://api.thenounproject.com/icon/{item_title}"
    response = requests.get(endpoint, auth=auth)
    response_content = json.loads(response.content)
    item_img = response_content['icon']['preview_url']
    # pp.pprint(item_img)
    data ={
        'item_title' : item_title,
        'img' : item_img
    }
    return render(request, 'pages/item.html', data)