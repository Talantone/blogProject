from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from . import models


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsOwnerOrReadOnly(permissions.BasePermission):  # Permission for Owner-only updating of model objects

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or request.user == obj.author)

class ReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method is SAFE_METHODS
