from django.urls import path
from . import views
urlpatterns=[
    path('home/', views.home,name='home'),
    path('<int:id>/',views.post,name='post'),
    path('category/<str:category>/', views.category_view, name='category'),
]