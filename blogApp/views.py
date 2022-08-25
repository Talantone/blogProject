from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.utils import timezone
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwner, IsOwnerOrReadOnly, ReadOnly
from .serializers import BlogSerializer, AuthorSerializer, CategorySerializer, TagSerializer
from .models import BlogPost, Category, Tag


class PostAPIList(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = BlogPost.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = self.queryset.filter(publish_date__lte=datetime.datetime.now())
            return queryset
        else:
            queryset = self.queryset.filter(publish_date__lte=datetime.datetime.now(), for_logged_users=False)
            return queryset


class PostAPICreate(generics.CreateAPIView):
    serializer_class = BlogSerializer
    queryset = BlogPost.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        stuff = get_object_or_404(BlogPost, slug=slug)
        return stuff


class AuthorApiList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (ReadOnly,)


class CategoryAPIList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (ReadOnly,)

class TagAPIList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (ReadOnly,)

