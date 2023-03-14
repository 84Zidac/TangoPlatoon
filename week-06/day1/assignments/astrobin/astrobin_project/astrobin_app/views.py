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
    image_otd = '/api/v1/imageoftheday/?'
    limit='&limit=1'
    format='&format=json'
    # auth = OAuth1('e50a92a8cb01d03b81d214b18d5b0dc15262d04f', '5b47874454d9ec613a35365debbdd3dbb9d0fdbf', signature_method='PLAINTEXT')
    # endpoint = f"http://astrobin.com/api/v1/imageoftheday/?api_key={os.environ['api_key']}&api_secret={os.environ['secret_key']}&limit=1&format=json"
    endpoint = f"http://astrobin.com{image_otd}api_key={os.environ['api_key']}&api_secret=5b47874454d9ec613a35365debbdd3dbb9d0fdbf{limit}{format}"
    response = requests.get(endpoint)
    response_content = json.loads(response.content)
    imgURL = response_content['objects'][0]['image']
    new_endpoint = f"http://astrobin.com{imgURL}/?api_key={os.environ['api_key']}&api_secret=5b47874454d9ec613a35365debbdd3dbb9d0fdbf"
    new_response = requests.get(new_endpoint)
    new_response_content = json.loads(new_response.content)
    final_img_url = new_response_content['url_regular']
    pp.pprint(new_response_content)
    data ={
        'img':final_img_url,
    }
    return render(request, 'pages/item.html', data)

def item(request):
    item_title = request.POST.get('item')
    # print(item_title)
    auth = OAuth1(os.environ['api_key'], os.environ['secret_key'])
    endpoint = "http://astrobin.com/api/v1/imageoftheday/?format=json&limit=1"
    response = requests.get(endpoint, auth=auth)
    response_content = json.loads(response.content)
    # item_img = response_content['icon']['preview_url']
    pp.pprint(response_content)
    data ={
        
    }
    return render(request, 'pages/item.html', data)