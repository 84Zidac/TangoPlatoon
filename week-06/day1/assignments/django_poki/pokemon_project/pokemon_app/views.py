from django.shortcuts import render
import requests
import json
# import pprint
import os
import random

# pp=pprint.PrettyPrinter(indent=2, depth=2)
# Create your views here.
def get_pokemons(name):
    master_poki = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(master_poki)
    response_content= json.loads(response.content)
    poki_img = response_content['sprites']['front_default']
    poki_name = response_content['name']
    type = response_content['types'][0]['type']['name']
    type_url = response_content['types'][0]['type']['url']
    type_response = requests.get(type_url)
    type_content = json.loads(type_response.content)
    same_type_list = (type_content['pokemon'])
    # print (same_type_list)
    num_w_same_type = (len(type_content['pokemon']))
    # pp.pprint(type_url)
    data = {
        'poki_img_1': poki_img,
        'poki_name_1': poki_name,
        'poki_type' : type,
    }
    counter = 2
    while counter < 6:
        randnum = random.randint(1,num_w_same_type)
        add_poki = f"https://pokeapi.co/api/v2/pokemon/{same_type_list[randnum]['pokemon']['name']}/"
        add_response=requests.get(add_poki)
        add_response_content = json.loads(add_response.content)
        add_img = add_response_content['sprites']['front_default']
        data[f'poki_img_{counter}'] = add_img
        counter +=1
    
    return data
        
    
def home(request):
    randnum = random.randint(1,1008)
    data = get_pokemons(randnum)
    return render(request, 'pages/form.html', data)
    
def get_pokes(request):
    if request.POST.get('input_pokemon') == '':
        randnum = random.randint(1,1008)
        poki_name = randnum
    else: 
        poki_name = request.POST.get('input_pokemon')
    data = get_pokemons(poki_name)
    return render(request, 'pages/get_poks.html',data)



        
    