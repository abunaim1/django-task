from rest_framework import viewsets
from . import models, serializers


class IngredientsViewset(viewsets.ModelViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer