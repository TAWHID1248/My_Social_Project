from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from App_Login.forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from App_Login.models import UserProfile
from App_Login.forms import EditProfile

# Create your views here.

def signup(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponse(reverse('App_Login:login'))
    return render(request,'App_Login/signup.html', {'title': 'Signup . instagram','form': form})

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

    return render(request,'App_Login/login.html', {'title': 'Login','form': form})


def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)

    return render(request,'App_Login/edit_profile.html', {'title': 'Edit Profile', 'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))