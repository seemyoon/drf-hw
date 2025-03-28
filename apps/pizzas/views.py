from urllib.request import Request

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pizzas.filter import filter_pizzas
from apps.pizzas.models import PizzaModel
from apps.pizzas.serializers import PizzaSerializer


class PizzaListCreateView(ListCreateAPIView):
    serializer_class = PizzaSerializer
    def get_queryset(self):
        req = self.request
        return filter_pizzas(req.query_params)

class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'delete']