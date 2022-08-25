from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BlogPost, Category, Tag


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("title", "slug", "category", "tags", "author", "content", "image", "publish_date", "for_logged_users")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", "slug")
