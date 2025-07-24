from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render
from django.urls import reverse
from .data import posts


def home(request):
    return render(request,'posts/home.html',{"posts":posts})

def post(request,id):
    valid_id=False
    for post in posts:
        if id == post['id']:
            post_dict=post
            valid_id=True
            break
        
    if valid_id:  
        return render(request,"posts/post.html",{"post_dict":post_dict})
    else:
        raise Http404()
def redirect(request,id=None):
    if id:
      url=reverse('post',args=[id])
      return HttpResponseRedirect(url)
    else:
        url=reverse('home')
        return HttpResponseRedirect(url)

def category_view(request, category):
    filtered_posts = [post for post in posts if post["category"].lower() == category.lower()]
    return render(request,'posts/home.html',{"posts":filtered_posts})
