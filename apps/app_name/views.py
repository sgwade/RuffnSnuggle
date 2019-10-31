from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import *
from django.http import JsonResponse

def index(request):
    return render(request, "app_name/index.html")

def caring(request):
    if "user_id" in request.session:
        context = {
            "user" : Users.objects.get(id = request.session["user_id"])
        }
        return render(request, "app_name/caring.html", context)
    else:
        return redirect("/")

def all_dogs(request):
    if "user_id" in request.session:
        context = {
            "user" : Users.objects.get(id = request.session["user_id"]),
            "all_the_dogs" : Pets.objects.filter(animal="dog")
        }
        return render(request, "app_name/all_dogs.html", context)
    else:
        return redirect("/")

def all_cats(request):
    if "user_id" in request.session:
        context = {
            "user" : Users.objects.get(id = request.session["user_id"]),
            "all_the_cats" : Pets.objects.filter(animal="cat")
        }
        return render(request, "app_name/all_cats.html", context)
    else:
        return redirect("/")

def log_or_reg(request):
    return render(request, "app_name/log_or_reg.html")

def dashboard(request):
    if "user_id" in request.session:
        context = {
            "user" : Users.objects.get(id = request.session["user_id"]),
            "all_liked_pets" : Users.objects.get(id = request.session["user_id"]).liked_animals.all()
        }
        return render(request, "app_name/dashboard.html", context)
    else:
        return redirect("/")

def this_animal(request, pets_id):
    if "user_id" in request.session:
        context = {
            "user" : Users.objects.get(id = request.session["user_id"]),
            "pet" : Pets.objects.get(id = pets_id),
            "user" : Users.objects.get(id = request.session["user_id"])
        }
        return render(request, "app_name/this_animal.html", context)
    else:
        return redirect("/")

def favorites(request, pets_id, user_id):
    if "user_id" in request.session:
        this_pet = Pets.objects.get(id=pets_id)
        this_user = Users.objects.get(id = request.session["user_id"])
        this_pet.users_who_like.add(this_user)
        return redirect("/dashboard")
    else:
        return redirect("/")

def delete(request, pets_id):
    if "user_id" in request.session:
        this_pet = Pets.objects.get(id= pets_id)
        this_user = Users.objects.get(id = request.session["user_id"])
        this_pet.users_who_like.remove(this_user)
        return redirect("/dashboard")
    else:
        return redirect("/")

def subappt(request):
    if "user_id" in request.session:
        errors = Appointment.objects.schedule_visit_validator(request.POST)
        if len(errors) > 0:
            response = JsonResponse({"error" : "Invalid date, please try again."})
            response.status_code = 403
            return response
        else:
            response = JsonResponse({"success" : "Appointment made! See you soon!"})
            response.status_code = 200
            Appointment.objects.create(user = Users.objects.get(id = request.session["user_id"]), pet = Pets.objects.get(id = request.POST["this_pet"]), date = request.POST["appt"])
            return response
    else:
        return redirect("/")

def alert(request):
    if "user_id" in request.session:
        return render("alert")
    else:
        return redirect("/")








##############################################################################################
#LOGIN AND REG
def register_process(request):
# Make sure user is logged out/not in session
# Validate for form errors
    try:
        request.session.clear()
    except:
        pass
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/signin_page")
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
#see if password matches password confirmation
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            this_user = Users.objects.create(first_name = first_name, last_name = last_name, email = email, password = password)
            request.session['user_id'] = this_user.id
            errors["success"] = "Successfully registered (or logged in)!"
            return redirect('/dashboard')
        else:
            messages.error(request, "Your passwords must match.")
            return redirect ("/signin_page")

def login_process(request):
# Make sure user is logged out/not in session
    try:
        request.session.clear()
    except:
        pass
    errors = Users.objects.log_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/signin_page")
    else:
        logged_user = Users.objects.get(email=request.POST['email'])
        request.session["user_id"] = logged_user.id
        return redirect('/dashboard')

def logout(request):
#log user out
    request.session.clear()
    return redirect("/signin_page")