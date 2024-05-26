# mainapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm
from django.http import HttpResponseNotAllowed

def admin_connection(request):
    reservations = Reservation.objects.all()
    return render(request, 'mainapp/admin_connection.html', {'reservations': reservations})
def home(request):
    return render(request, 'mainapp/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'mainapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'mainapp/login.html', {'form': form})

#def logout_view(request):
 #   if request.method == 'POST':
  #      logout(request)
   #     return redirect('home')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    elif request.method == 'GET':
        # If accessed via GET request, redirect to the home page
        return redirect('home')
    else:
        # Return a method not allowed response for other request methods
        return HttpResponseNotAllowed(['POST', 'GET'])

@login_required
def dashboard(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'mainapp/dashboard.html', {'reservations': reservations})

@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('dashboard')
    else:
        form = ReservationForm()
    return render(request, 'mainapp/reserve.html', {'form': form})

def salma(request):
    return render(request,'mainapp/salma.html')
