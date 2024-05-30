from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
# Create your views here.


class RecipeViewset(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer