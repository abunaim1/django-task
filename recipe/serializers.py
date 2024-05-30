from rest_framework import serializers
from .models import Recipe, Ingredient, Rating, Comment

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'