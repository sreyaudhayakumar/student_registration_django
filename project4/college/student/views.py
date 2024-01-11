from django.shortcuts import render,redirect,get_object_or_404
from .models import Person
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
import os

def Home(request):
    return render(request,'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        age = request.POST['age']
        place = request.POST['place']
        address = request.POST['address']
        course = request.POST['course']
        email = request.POST['email']
        image = request.FILES['image']
        user = Person(username=username,password=password,firstname=firstname,lastname=lastname,gender=gender,age=age,place=place,address=address, course= course,email=email,photo=image )
        auth_user = User(username=username,first_name=firstname,last_name=lastname,email=email)
        auth_user.set_password(password)
        auth_user.save()
        user.save()
        return HttpResponse('<script>alert("registered successfully"),window.location="/login";</script>')
    return render(request, 'register.html')

def home_page(request):
    return render(request,'home_page.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        request.session['user_id'] = username
        if user is not None and  user.is_superuser==1:
            return redirect('/Admin_home')
        elif user is not None and user.is_superuser==0:
            return redirect('/home_page')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login')

    return render(request, 'login.html')

def Admin_Home(request):
    return render(request,'admin_Home.html')
def lgout(request):
    logout(request)
    return redirect(login)

def edit_profile(request):
    id = request.session['user_id']
    auth_user = Person.objects.get(username=id)

    if request.method == "POST":
        auth_user.username = request.POST['username']
        auth_user.firstname = request.POST['firstname']
        auth_user.lastname = request.POST['lastname']
        auth_user.gender = request.POST['gender']
        auth_user.age = request.POST['age']
        auth_user.address = request.POST['address']
        auth_user.course = request.POST['course']
        auth_user.phone = request.POST['phone']
        auth_user.email = request.POST['email']

        if 'image' in request.FILES:
            if auth_user.photo:
                os.remove(auth_user.photo.path)
            auth_user.photo = request.FILES['image']

        auth_user.save()
        return HttpResponse("UPDATED SUCCESSFULLY")

    return render(request, 'edit_profile.html', {'user': auth_user})
