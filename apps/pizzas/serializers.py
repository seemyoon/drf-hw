from rest_framework import serializers

from apps.pizzas.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('id', 'name', 'price', 'description', 'weight')
