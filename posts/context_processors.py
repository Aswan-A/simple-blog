from .data import posts

def categories(request):
    categories = sorted({post["category"] for post in posts})
    return {"categories": categories}
