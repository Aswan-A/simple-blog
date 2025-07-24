from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request,'posts/home.html',{"posts":posts})

def post(request, id):
    post_obj = get_object_or_404(Post, id=id)
    return render(request, "posts/post.html", {"post_dict": post_obj})
    
def redirect(request,id=None):
    if id:
      url=reverse('post',args=[id])
      return HttpResponseRedirect(url)
    else:
        url=reverse('home')
        return HttpResponseRedirect(url)

def category_view(request, category):
    filtered_posts = Post.objects.filter(category__name__iexact=category)
    return render(request,'posts/home.html',{"posts":filtered_posts})
