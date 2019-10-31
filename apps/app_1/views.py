from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from random import randint
from apps.app_name.models import *
# Create your views here.



def game_home(request):
    random_num = randint(5,10)
    rand_num_arr=[]
    for i in range(random_num):
        rand_num_arr.append(i)
    rand_width_arr=[]
    for i in range(random_num):
        x = randint(50, 100)
        rand_width_arr.append(x)
        print (rand_width_arr)
    rand_color_arr = []
    for i in range(random_num):
        x = randint(1, 3)
        rand_color_arr.append(x)
        print (rand_color_arr)
    rand_margin_arr=[]
    for i in range(random_num):
        x = randint(1,150)
        rand_margin_arr.append(x)
        print(rand_margin_arr)
    context = {
        'arr_len' : len(rand_width_arr),
    }
    for i in rand_num_arr:   
        x = str(i)+'width'
        context[x] = rand_width_arr[i]
        y = str(i)+'color'
        context[y] = rand_color_arr[i]
        z = str(i)+'margin'
        context[z] = rand_color_arr[i]
    print(context)
    return render(request, 'app_1/index.html', context)

def animal(request):
    return render(request, 'app_1/animal.html')

def animal_size(request, animal):
    context = {
        'animal' : animal,
    }
    return render(request, 'app_1/animal_size.html', context)

def animal_age(request, animal, size):
    context = {
        'animal' : animal,
        'size' : size
    }
    return render(request, 'app_1/animal_age.html', context)

def animal_energy(request, animal, size, age):
    context = {
        'animal' : animal,
        'size' : size,
        'age' : age
    }
    return render(request, 'app_1/animal_energy.html', context)

def animal_friendly(request, animal, size, age, energy):
    context = {
        'animal' : animal,
        'size' : size,
        'age' : age,
        'energy' : energy,
    }
    return render(request, 'app_1/animal_friendly.html', context)

def find_animal(request, animal, size, age, energy, friendly):
    context = {
        'animal' : animal,
        'size' : size,
        'age' : age,
        'energy' : energy,
        'friendly' : friendly,
    }
    # return redirect('/game/process_result', context)
    return render(request, 'app_1/find_animal.html', context)

def process_result(request):
    if "user_id" in request.session:
        try:
            context = {
                "user" : Users.objects.get(id = request.session["user_id"]),
            }
            print('gonna look for things')
            print(request.POST)
            filter_pet = Pets.objects.filter(age=request.POST['age_from_form'], animal=request.POST['animal_from_form'], size=request.POST['size_from_form'], energy=request.POST['energy_from_form'], friendly=request.POST['friendly_from_form'])
            
            filter_pet[0]
            this_pet = filter_pet[0].id
            this_pet = int(this_pet)
            print('we look for animals')
            print(filter_pet[0])
            return redirect(f"this_animal/{this_pet}")
        except:
            return render(request, 'app_1/animal_not_found.html', context)
    else:
        return redirect("/")

        