from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from App_Posts.models import Post, User
from App_Login.models import Follow
# Create your views here.


@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_Posts/home.html', context={
        'title': 'Home', 
        'search': search, 
        'result': result,
        'posts': posts
        })