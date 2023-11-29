from django.shortcuts import render, HttpResponse
from App_Login.forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy

# Create your views here.

def signup(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            pass
    return render(request,'App_Login/signup.html', {'title': 'Signup . instagram','form': form})