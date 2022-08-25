from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostAPIList.as_view(), name='posts'),
    path('posts/create/', views.PostAPICreate.as_view()),
    path("posts/<slug:slug>/", views.PostAPIUpdate.as_view()),
    path('authors/', views.AuthorApiList.as_view()),
    path('categories/', views.CategoryAPIList.as_view()),
    path('tags/', views.TagAPIList.as_view()),

]
