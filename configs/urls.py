from django.urls import path, include

urlpatterns = [
    path('pizzas', include('apps.pizzas.urls'))
]
