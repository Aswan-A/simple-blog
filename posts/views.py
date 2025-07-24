from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render
from django.urls import reverse

posts=[
  {
    "id": 1,
    "title": "Introduction to Web Development",
    "content": "Web development involves building and maintaining websites. It includes web design, web publishing, and database management."
  },
  {
    "id": 2,
    "title": "Let's explore Javascript",
    "content": "Javascript is interpreted, high-level, general-purpose programming language. Widely used in the fields of web development."
  },
  {
    "id": 3,
    "title": "Django: The best web framework",
    "content": "Django is used by almost every big tech company like Facebook, Google, YouTube, Instagram, etc."
  }
]
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

