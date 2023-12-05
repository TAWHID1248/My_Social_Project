from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from App_Posts.models import Post, User

# Create your views here.


@login_required
def home(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_Posts/home.html', context={'title': 'Home', 'search': search, 'result': result})