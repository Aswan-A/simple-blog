from .models import Post

def categories(request):
    categories = sorted(set(Post.objects.values_list("category__name", flat=True)))
    return {"categories": categories}
